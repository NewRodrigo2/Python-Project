# ejemplo
import customtkinter as ctk
from pathlib import Path
import shutil
import re
import tiktoken
import pyperclip  # pip install pyperclip

# Configuración inicial de la ventana
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Generador de Texto Optimizado")
app.geometry("600x600")

# Ruta base de tus scripts
ruta_base = Path(r"F:\Python\Python Project\prueba")
archivo_salida = Path("memoria_optimizada.txt")

def generar_memoria_optimizada(ruta_archivo: Path, salida_readme: Path = archivo_salida, modelo: str = "gpt-4"):
    """
    Procesa un archivo Python y genera un README.md optimizado:
    - Detecta clases, métodos y atributos
    - Elimina redundancias (open/json repetidos)
    - Simplifica fragmentos de código
    - Normaliza formato uniforme
    - Cuenta tokens con tiktoken
    """
    contenido = ruta_archivo.read_text(encoding="utf-8")
    lineas = contenido.splitlines()

    resultado = [f"# Memoria dinámica optimizada\n\n## {ruta_archivo.name}\n"]

    clase_actual = None
    atributos = set()
    acciones = set()

    for linea in lineas:
        linea = linea.strip()

        # Detectar clases
        match_clase = re.match(r"class\s+(\w+)", linea)
        if match_clase:
            clase_actual = match_clase.group(1)
            resultado.append(f"\n### {clase_actual}")
            atributos.clear()
            acciones.clear()
            continue

        # Detectar métodos
        match_metodo = re.match(r"def\s+(\w+)", linea)
        if match_metodo and clase_actual:
            metodo = match_metodo.group(1)
            if metodo == "__init__":
                resultado.append(f"- __init__ → inicializa atributos principales")
            else:
                resultado.append(f"- {metodo} → acción definida")
            continue

        # Detectar atributos
        if "self." in linea and "=" in linea and clase_actual:
            atributo = linea.split("=")[0].strip()
            if atributo not in atributos:
                atributos.add(atributo)
                resultado.append(f"- Atributo: {atributo}")

        # Simplificar llamadas a open/json (una sola vez por clase)
        if "open(" in linea and "open" not in acciones:
            resultado.append("- Usa open → lectura/escritura de archivos")
            acciones.add("open")
        if "json.load" in linea and "json.load" not in acciones:
            resultado.append("- Usa json.load → carga datos")
            acciones.add("json.load")
        if "json.dump" in linea and "json.dump" not in acciones:
            resultado.append("- Usa json.dump → guarda datos")
            acciones.add("json.dump")

    texto_final = "\n".join(resultado)
    salida_readme.write_text(texto_final, encoding="utf-8")

    # Contar tokens
    enc = tiktoken.encoding_for_model(modelo)
    tokens = enc.encode(texto_final)
    print(f"Memoria optimizada generada en {salida_readme}")
    print(f"El README.md optimizado usa {len(tokens)} tokens")

    return texto_final, len(tokens)

def generar_texto(nombre_archivo: str):
    """
    Genera texto optimizado para el archivo indicado y lo guarda en memoria_optimizada.txt
    """
    ruta = ruta_base / nombre_archivo
    if ruta.exists():
        texto_final, total_tokens = generar_memoria_optimizada(ruta)
        print(texto_final)
        print(f"Total tokens: {total_tokens}")
    else:
        print(f"No se encontró {ruta}")

def copiar_archivo():
    """
    Copia el archivo generado y además mantiene su contenido en el portapapeles.
    """
    destino = Path("memoria_copia.txt")
    if archivo_salida.exists():
        shutil.copy(archivo_salida, destino)
        contenido = archivo_salida.read_text(encoding="utf-8")
        pyperclip.copy(contenido)
        print(f"Archivo copiado a {destino}")
        print("Contenido de memoria_optimizada.txt copiado al portapapeles.")
    else:
        print("No existe archivo para copiar.")

# Botones
btn1 = ctk.CTkButton(app, text="Generar logic.py", command=lambda: generar_texto("logic.py"))
btn2 = ctk.CTkButton(app, text="Generar main.py", command=lambda: generar_texto("main.py"))
btn3 = ctk.CTkButton(app, text="Generar menu_gral.py", command=lambda: generar_texto("menu_gral.py"))
btn4 = ctk.CTkButton(app, text="Generar menu_admin.py", command=lambda: generar_texto("menu_admin.py"))
btn5 = ctk.CTkButton(app, text="Copiar archivo.txt", command=copiar_archivo)
btn6 = ctk.CTkButton(app, text="Botón sin función")

# Ubicación con grid
btn1.grid(row=0, column=0, padx=10, pady=10)
btn2.grid(row=0, column=1, padx=10, pady=10)
btn3.grid(row=1, column=0, padx=10, pady=10)
btn4.grid(row=1, column=1, padx=10, pady=10)
btn5.grid(row=2, column=0, padx=10, pady=10)
btn6.grid(row=2, column=1, padx=10, pady=10)

app.mainloop()
