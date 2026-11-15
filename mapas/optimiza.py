import re
from pathlib import Path
import tiktoken

def generar_memoria_optimizada(ruta_archivo: str, salida_readme: str = "README.md", modelo: str = "gpt-4"):
    """
    Procesa un archivo Python y genera un README.md optimizado:
    - Detecta clases, métodos, atributos y múltiples 'command=' con el resto de la línea
    """

    contenido = Path(ruta_archivo).read_text(encoding="utf-8")
    lineas = contenido.splitlines()

    resultado = ["# Memoria dinámica optimizada\n"]

    clase_actual = None
    metodo_actual = None
    acciones = set()  # para open/json (se mantienen con filtro opcional)

    for num_linea, linea in enumerate(lineas, start=1):
        linea_limpia = linea.strip()

        # Detectar clases
        match_clase = re.match(r"class\s+(\w+)", linea_limpia)
        if match_clase:
            clase_actual = match_clase.group(1)
            metodo_actual = None
            resultado.append(f"\n## {clase_actual} (línea {num_linea})")
            acciones.clear()
            continue

        # Detectar métodos
        match_metodo = re.match(r"def\s+(\w+)", linea_limpia)
        if match_metodo and clase_actual:
            metodo_actual = match_metodo.group(1)
            if metodo_actual == "__init__":
                resultado.append(f"- {metodo_actual} (línea {num_linea}) → inicializa atributos principales")
            else:
                resultado.append(f"- {metodo_actual} (línea {num_linea}) → acción definida")
            continue

        # Detectar atributos dentro de un método
        if "self." in linea_limpia and "=" in linea_limpia and clase_actual and metodo_actual:
            atributo = linea_limpia.split("=")[0].strip()
            if not atributo.startswith("-"):
                linea_attr = f"  - Atributo: {atributo} (línea {num_linea})"
                if linea_attr not in resultado:
                    resultado.append(linea_attr)

        # Detectar TODOS los command= y capturar el resto de la línea (sin restricciones de conjunto)
        if "command=" in linea_limpia and clase_actual:
            resultado.append(f"  - Command: {linea_limpia} (línea {num_linea})")

        # Simplificar llamadas a open/json (con filtro de una sola vez por clase)
        if "open(" in linea_limpia and "open" not in acciones:
            resultado.append(f"- Usa open (línea {num_linea}) → lectura/escritura de archivos")
            acciones.add("open")
        if "json.load" in linea_limpia and "json.load" not in acciones:
            resultado.append(f"- Usa json.load (línea {num_linea}) → carga datos")
            acciones.add("json.load")
        if "json.dump" in linea_limpia and "json.dump" not in acciones:
            resultado.append(f"- Usa json.dump (línea {num_linea}) → guarda datos")
            acciones.add("json.dump")

    # Guardar en README.md
    texto_final = "\n".join(resultado)
    Path(salida_readme).write_text(texto_final, encoding="utf-8")

    # Contar tokens
    enc = tiktoken.encoding_for_model(modelo)
    tokens = enc.encode(texto_final)
    print(f"Memoria optimizada generada en {salida_readme}")
    print(f"El archivo optimizado usa {len(tokens)} tokens")

    return texto_final, len(tokens)

# Ejemplo de uso
if __name__ == "__main__":
    carpeta_prueba = Path("C:/Users/Rodrigo/Documents/GitHub/Python-Project/prueba")
    
    for archivo_py in carpeta_prueba.glob("*.py"):
        print(f"\nAnalizando: {archivo_py.name}")
        generar_memoria_optimizada(str(archivo_py), salida_readme=f"memoria_{archivo_py.stem}.md")