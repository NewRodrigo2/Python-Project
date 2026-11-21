import re
from pathlib import Path
from datetime import datetime

import tiktoken


def generar_memoria_optimizada(
    ruta_archivo: str,
    salida_readme: str = "README.md",
    modelo: str = "gpt-4"
):
    """
    Procesa un archivo Python y genera un README.md optimizado:
    - Detecta clases, métodos, atributos y múltiples command=
    - Añade nombre y fecha del archivo analizado
    """

    ruta = Path(ruta_archivo)

    contenido = ruta.read_text(encoding="utf-8")
    lineas = contenido.splitlines()

    fecha_generacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    resultado = [
        "# Memoria dinámica optimizada\n",
        f"**Archivo analizado:** {ruta.name}",
        f"**Fecha de generación:** {fecha_generacion}\n"
    ]

    clase_actual = None
    metodo_actual = None

    acciones = set()

    for num_linea, linea in enumerate(lineas, start=1):

        linea_limpia = linea.strip()

        # Detectar clases
        match_clase = re.match(r"class\s+(\w+)", linea_limpia)

        if match_clase:
            clase_actual = match_clase.group(1)
            metodo_actual = None

            resultado.append(
                f"\n## {clase_actual} (línea {num_linea})"
            )

            acciones.clear()
            continue

        # Detectar métodos
        match_metodo = re.match(r"def\s+(\w+)", linea_limpia)

        if match_metodo and clase_actual:

            metodo_actual = match_metodo.group(1)

            if metodo_actual == "__init__":
                resultado.append(
                    f"- Método: {linea_limpia} (línea {num_linea}) → inicializa atributos principales"
                )
            else:
                resultado.append(
                    f"- Método: {linea_limpia} (línea {num_linea})"
                )

            continue

        # Detectar atributos
        if (
            "self." in linea_limpia
            and "=" in linea_limpia
            and clase_actual
            and metodo_actual
        ):

            atributo = linea_limpia.split("=")[0].strip()

            if not atributo.startswith("-"):

                linea_attr = (
                    f" - Atributo: {atributo} (línea {num_linea})"
                )

                if linea_attr not in resultado:
                    resultado.append(linea_attr)

        # Detectar command=
        if "command=" in linea_limpia and clase_actual:
            resultado.append(
                f" - Command: {linea_limpia} (línea {num_linea})"
            )

        # Detectar open()
        if "open(" in linea_limpia and "open" not in acciones:

            resultado.append(
                f"- Usa open (línea {num_linea}) → lectura/escritura de archivos"
            )

            acciones.add("open")

        # Detectar json.load()
        if "json.load" in linea_limpia and "json.load" not in acciones:

            resultado.append(
                f"- Usa json.load (línea {num_linea}) → carga datos"
            )

            acciones.add("json.load")

        # Detectar json.dump()
        if "json.dump" in linea_limpia and "json.dump" not in acciones:

            resultado.append(
                f"- Usa json.dump (línea {num_linea}) → guarda datos"
            )

            acciones.add("json.dump")

    texto_final = "\n".join(resultado)

    Path(salida_readme).write_text(
        texto_final,
        encoding="utf-8"
    )

    enc = tiktoken.encoding_for_model(modelo)
    tokens = enc.encode(texto_final)

    print(f"Memoria optimizada generada en {salida_readme}")
    print(f"El archivo optimizado usa {len(tokens)} tokens")

    return texto_final, len(tokens)