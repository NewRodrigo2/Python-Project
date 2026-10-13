import re
from pathlib import Path
import tiktoken

def generar_memoria_optimizada(ruta_archivo: str, salida_readme: str = "README.md", modelo: str = "gpt-4"):
    """
    Procesa un archivo Python y genera un README.md optimizado:
    - Detecta clases, métodos y atributos
    - Elimina redundancias (open/json repetidos)
    - Simplifica fragmentos de código (sin with open(...) ni json.dump(...))
    - Normaliza formato uniforme
    - Cuenta tokens con tiktoken
    """

    contenido = Path(ruta_archivo).read_text(encoding="utf-8")
    lineas = contenido.splitlines()

    resultado = ["# Memoria dinámica optimizada\n"]

    clase_actual = None
    atributos = set()
    acciones = set()  # para evitar repetir open/json en la misma clase

    for linea in lineas:
        linea = linea.strip()

        # Detectar clases
        match_clase = re.match(r"class\s+(\w+)", linea)
        if match_clase:
            clase_actual = match_clase.group(1)
            resultado.append(f"\n## {clase_actual}")
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

    # Guardar en README.md
    texto_final = "\n".join(resultado)
    Path(salida_readme).write_text(texto_final, encoding="utf-8")

    # Contar tokens
    enc = tiktoken.encoding_for_model(modelo)
    tokens = enc.encode(texto_final)
    print(f"Memoria optimizada generada en {salida_readme}")
    print(f"El README.md optimizado usa {len(tokens)} tokens")

    return texto_final, len(tokens)


# Ejemplo de uso
if __name__ == "__main__":
    texto_final, total_tokens = generar_memoria_optimizada("f:/Python/Python Project/prueba/logic.py")
    print(texto_final)
    print(f"Total tokens: {total_tokens}")
