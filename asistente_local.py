"""Asistente local para consultar el proyecto con Ollama."""

import ast
import json
import os
import re
import threading
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk


ROOT = Path(__file__).resolve().parent
MEMORY = ROOT / ".asistente"
MODEL = "qwen3:4b-instruct"
OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
IGNORED_DIRS = {".git", ".asistente", "venv", ".venv", "__pycache__", "node_modules"}
MAX_SOURCE_CHARS = 5000
ROUTES = {
    "Automática": None,
    "Aplicación prueba": ("prueba/main.py", "prueba/menu_gral.py", "prueba/logic.py"),
}

DEFAULT_INSTRUCTIONS = """# Instrucciones permanentes

- Responde siempre en español y de forma breve y clara.
- Por defecto, responde en un máximo de dos párrafos breves. Amplía la respuesta solo si el usuario lo solicita.
- Al explicar un error, primero describe qué significa y después recomienda una solución.
- No generes código a menos que el usuario lo solicite explícitamente.
- Añade ejemplos extra solo si el usuario los solicita.
- Basa las respuestas sobre este proyecto en el mapa actualizado y en los archivos citados.
- Si el mapa o el código no permiten confirmar algo, dilo con claridad.
"""


def ensure_memory_files():
    MEMORY.mkdir(exist_ok=True)
    templates = {
        "INSTRUCCIONES.md": DEFAULT_INSTRUCTIONS,
        "PROGRESO.md": "# Progreso\n\nActualiza esta nota cuando se complete un avance importante.\n",
        "PENDIENTES.md": "# Pendientes\n\n- [ ] Agrega aquí los próximos pasos.\n",
        "ERRORES.md": "# Errores conocidos\n\nRegistra aquí errores confirmados, su causa y su estado.\n",
        "RESPUESTAS.md": "# Respuestas guardadas\n\nUsa el botón **Guardar y copiar** para guardar una pregunta y su respuesta.\n",
    }
    for name, content in templates.items():
        path = MEMORY / name
        if not path.exists():
            path.write_text(content, encoding="utf-8")


def relative(path):
    return path.relative_to(ROOT).as_posix()


def scan_project():
    entries = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = sorted(d for d in dirs if d not in IGNORED_DIRS)
        for filename in sorted(files):
            if not filename.endswith(".py"):
                continue
            path = Path(base) / filename
            if path == Path(__file__):
                continue
            rel = relative(path)
            try:
                source = path.read_text(encoding="utf-8-sig")
                tree = ast.parse(source, filename=rel)
                records = []
                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                        kind = "clase" if isinstance(node, ast.ClassDef) else "función"
                        parent = next((c.name for c in ast.walk(tree)
                                       if isinstance(c, ast.ClassDef) and node in c.body), None)
                        if parent and kind == "función":
                            kind = "método de " + parent
                        doc = ast.get_docstring(node)
                        records.append((node.lineno, kind, node.name, doc))
                records.sort()
                entries.append({"path": rel, "source": source, "symbols": records, "error": None})
            except (OSError, SyntaxError, UnicodeError) as exc:
                entries.append({"path": rel, "source": "", "symbols": [], "error": str(exc)})
    return entries


def render_map(entries):
    now = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    out = ["# Mapa del proyecto Python", "", f"Generado: {now}",
           "", f"Archivos Python encontrados: {len(entries)}", ""]
    for entry in entries:
        out.extend([f"## `{entry['path']}`", ""])
        if entry["error"]:
            out.extend([f"**Error de análisis:** `{entry['error']}`", ""])
            continue
        if not entry["symbols"]:
            out.extend(["No se detectaron clases ni funciones.", ""])
        for line, kind, name, doc in entry["symbols"]:
            description = f" — {doc.splitlines()[0]}" if doc else ""
            out.append(f"- Línea {line}: **{kind}** `{name}`{description}")
        out.append("")
    return "\n".join(out)


def keywords(text):
    stop = {"para", "como", "que", "con", "una", "por", "del", "las", "los", "este", "esta", "quiero", "puedes", "explica"}
    return {word for word in re.findall(r"[a-zA-Z_][\w]{2,}", text.lower()) if word not in stop}


def is_inventory_query(question):
    return bool(re.search(
        r"\b(lista|listar|enumera|nombra|cu[aá]les|que|qué)\b.{0,35}\b(clases?|class|funciones?|m[eé]todos?)\b|"
        r"\b(clases?|class|funciones?|m[eé]todos?)\b.{0,35}\b(lista|listar|enumera|nombres?)\b",
        question.lower(),
    ))


def build_context(question, entries, route_paths=None):
    inventory_query = is_inventory_query(question)
    terms = keywords(question)
    ranked = []
    for entry in entries:
        if entry["error"]:
            continue
        haystack = (entry["path"] + " " + entry["source"]).lower()
        score = sum(haystack.count(term) for term in terms)
        if score:
            ranked.append((score, entry))
    ranked.sort(key=lambda pair: (-pair[0], pair[1]["path"]))
    if route_paths:
        entries_by_path = {entry["path"]: entry for entry in entries}
        route_entries = [entries_by_path[path] for path in route_paths if path in entries_by_path]
        missing = [path for path in route_paths if path not in entries_by_path]
        normalized_question = question.lower().replace("\\", "/")
        explicitly_named = [
            entry for entry in route_entries
            if entry["path"].lower() in normalized_question
            or entry["path"].split("/")[-1].lower() in normalized_question
        ]
        if explicitly_named:
            selected = explicitly_named
        else:
            route_scores = []
            for entry in route_entries:
                score = sum((entry["path"] + " " + entry["source"]).lower().count(term)
                            for term in terms)
                if score:
                    route_scores.append((score, entry))
            route_scores.sort(key=lambda pair: (-pair[0], pair[1]["path"]))
            selected = [entry for _, entry in route_scores[:2]]
    else:
        selected = [entry for _, entry in ranked[:3]]
        missing = []
    source_context = []
    for entry in ([] if inventory_query else selected):
        source = (entry["source"] if route_paths and len(selected) == 1
                  else entry["source"][:MAX_SOURCE_CHARS])
        source_context.append(f"ARCHIVO {entry['path']}:\n```python\n{source}\n```")
    note_context = []
    for name in (() if inventory_query else ("PROGRESO.md", "PENDIENTES.md", "ERRORES.md")):
        path = MEMORY / name
        note_context.append(f"{name}:\n{path.read_text(encoding='utf-8')[:1000]}")
    map_text = (MEMORY / "MAPA_PROYECTO.md").read_text(encoding="utf-8")
    if route_paths:
        map_sections = []
        for path in route_paths:
            marker = f"## `{path}`"
            start = map_text.find(marker)
            if start >= 0:
                end = map_text.find("\n## `", start + len(marker))
                map_sections.append(map_text[start:end if end >= 0 else None].strip())
        map_context = "\n\n".join(map_sections)
        if missing:
            map_context += "\n\nNo se encontraron estos archivos: " + ", ".join(missing)
        source_note = ("La ruta limita la búsqueda a: " + ", ".join(route_paths) + ". " +
                       ("Consulta de inventario: usa únicamente el mapa actualizado, sin enviar código fuente."
                        if inventory_query else
                        "Se incluyó código fuente solo de los archivos más relacionados con la pregunta."))
    else:
        if inventory_query:
            mentioned_files = re.findall(r"[\w/-]+\.py\b", question.lower().replace("\\", "/"))
            matching_sections = []
            for filename in mentioned_files:
                marker = f"## `{filename}`"
                start = map_text.lower().find(marker.lower())
                if start >= 0:
                    end = map_text.find("\n## `", start + len(marker))
                    matching_sections.append(map_text[start:end if end >= 0 else None].strip())
            map_context = "\n\n".join(matching_sections) if matching_sections else map_text[:3500]
            source_note = "Consulta de inventario: se usa el mapa, sin código fuente ni notas."
        else:
            map_context = map_text[:6000]
            source_note = ""
    return ("MAPA DEL PROYECTO:\n" + map_context +
            "\n\n" + source_note + "\n\nCÓDIGO FUENTE INCLUIDO:\n" +
            ("\n\n".join(source_context) if source_context else "No se identificó un archivo relacionado por palabras clave.") +
            "\n\nNOTAS:\n" + "\n\n".join(note_context))


class LocalAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Asistente local de Python")
        self.root.geometry("900x680")
        self.busy = False
        self.last_question = ""
        self.last_question_time = ""
        self.last_answer = ""
        self.last_answer_time = ""
        ensure_memory_files()
        self.make_ui()
        self.refresh_map(show_message=False)

    def make_ui(self):
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        bar = ttk.Frame(self.root, padding=10)
        bar.grid(row=0, column=0, sticky="ew")
        ttk.Label(bar, text=f"Modelo local: {MODEL}").pack(side="left")
        ttk.Label(bar, text="Ruta:").pack(side="left", padx=(12, 4))
        self.route_var = tk.StringVar(value="Automática")
        self.route_selector = ttk.Combobox(
            bar, textvariable=self.route_var, values=tuple(ROUTES), state="readonly", width=22
        )
        self.route_selector.pack(side="left")
        ttk.Button(bar, text="Actualizar mapa", command=self.refresh_map).pack(side="right", padx=(6, 0))
        self.save_button = ttk.Button(bar, text="Guardar y copiar", command=self.save_and_copy, state="disabled")
        self.save_button.pack(side="right")
        self.output = tk.Text(self.root, wrap="word", state="disabled", padx=12, pady=10)
        self.output.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 8))
        self.output.tag_configure("user", foreground="#185abc", spacing1=8)
        self.output.tag_configure("assistant", spacing1=8, spacing3=10)
        bottom = ttk.Frame(self.root, padding=(10, 0, 10, 10))
        bottom.grid(row=2, column=0, sticky="ew")
        bottom.columnconfigure(0, weight=1)
        self.prompt = tk.Text(bottom, height=4, wrap="word")
        self.prompt.grid(row=0, column=0, sticky="ew", padx=(0, 8))
        self.prompt.bind("<Control-Return>", self.submit_event)
        self.send_button = ttk.Button(bottom, text="Preguntar", command=self.submit)
        self.send_button.grid(row=0, column=1, sticky="ns")
        ttk.Label(bottom, text="Ctrl+Enter envía la consulta.").grid(row=1, column=0, sticky="w", pady=(4, 0))

    def append(self, who, text, tag):
        self.output.configure(state="normal")
        self.output.insert("end", f"{who}:\n{text}\n\n", tag)
        self.output.see("end")
        self.output.configure(state="disabled")

    @staticmethod
    def current_time():
        return datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")

    def save_and_copy(self):
        if not self.last_answer:
            return
        target = MEMORY / "RESPUESTAS.md"
        try:
            with target.open("a", encoding="utf-8") as saved:
                saved.write(f"\n## Respuesta del {self.last_answer_time}\n\n")
                saved.write(f"**Pregunta ({self.last_question_time}):**\n\n{self.last_question}\n\n")
                saved.write(f"**Respuesta ({self.last_answer_time}):**\n\n{self.last_answer}\n\n---\n")
        except OSError as exc:
            messagebox.showerror("No se pudo guardar", f"No pude escribir en {target}.\n\n{exc}")
            return
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.last_answer)
            self.root.update_idletasks()
        except tk.TclError as exc:
            messagebox.showwarning(
                "Respuesta guardada",
                f"Guardé la pregunta y respuesta en:\n{target}\n\nNo pude copiarla al portapapeles.\n{exc}",
            )
            return
        messagebox.showinfo(
            "Respuesta guardada y copiada",
            f"Guardé la pregunta y respuesta en:\n{target}\n\nLa respuesta ya está copiada; puedes pegarla en ChatGPT.",
        )

    def refresh_map(self, show_message=True):
        entries = scan_project()
        target = MEMORY / "MAPA_PROYECTO.md"
        target.write_text(render_map(entries), encoding="utf-8")
        self.entries = entries
        if show_message:
            messagebox.showinfo("Mapa actualizado", f"Actualizado con {len(entries)} archivos Python.\n\n{target}")

    def submit_event(self, _event):
        self.submit()
        return "break"

    def submit(self):
        question = self.prompt.get("1.0", "end").strip()
        if not question or self.busy:
            return
        self.prompt.delete("1.0", "end")
        self.last_question = question
        self.last_question_time = self.current_time()
        self.last_answer = ""
        self.last_answer_time = ""
        self.save_button.configure(state="disabled")
        self.append(f"Tú · {self.last_question_time}", question, "user")
        route_name = self.route_var.get()
        self.busy = True
        self.send_button.configure(state="disabled")
        threading.Thread(target=self.ask_worker, args=(question, route_name), daemon=True).start()

    def ask_worker(self, question, route_name):
        try:
            self.refresh_map(show_message=False)
            instructions = (MEMORY / "INSTRUCCIONES.md").read_text(encoding="utf-8")
            route_paths = ROUTES.get(route_name)
            inventory_query = is_inventory_query(question)
            context = build_context(question, self.entries, route_paths)
            payload = {"model": MODEL, "stream": False, "think": False, "messages": [
                {"role": "system", "content": instructions + "\n\n" + context},
                {"role": "user", "content": question}],
                "options": {"temperature": 0.3,
                            "num_predict": 110 if inventory_query else 220,
                            "num_ctx": 4096 if inventory_query else 8192}}
            request = urllib.request.Request(OLLAMA_URL, data=json.dumps(payload).encode("utf-8"),
                                             headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(request, timeout=240) as response:
                result = json.loads(response.read().decode("utf-8"))
                answer = result.get("message", {}).get("content", "").strip()
                if not answer:
                    answer = ("Ollama respondió sin texto visible. Revisa que esté actualizado y que el modelo "
                              f"{MODEL} esté disponible; vuelve a intentarlo después de reiniciar Ollama.")
        except urllib.error.HTTPError as exc:
            details = exc.read().decode("utf-8", errors="replace").strip()
            answer = f"Ollama respondió con HTTP {exc.code} ({exc.reason})."
            if details:
                answer += f"\nDetalle: {details[:700]}"
        except urllib.error.URLError as exc:
            answer = f"No pude conectar con Ollama en 127.0.0.1:11434. Detalle: {exc.reason}"
        except TimeoutError:
            answer = ("Ollama tardó más de 240 segundos en responder. La solicitud se agotó; "
                      "prueba una pregunta más concreta o consulta las clases usando el mapa actualizado.")
        except Exception as exc:
            answer = f"Ocurrió un problema al consultar el proyecto: {exc}"
        self.root.after(0, self.finish_answer, answer)

    def finish_answer(self, answer):
        self.last_answer = answer
        self.last_answer_time = self.current_time()
        self.append(f"IA local · {self.last_answer_time}", answer, "assistant")
        self.busy = False
        self.send_button.configure(state="normal")
        self.save_button.configure(state="normal")


if __name__ == "__main__":
    LocalAssistant(tk.Tk()).root.mainloop()
