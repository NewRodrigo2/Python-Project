import os
from pathlib import Path

# 1. Obtienes la unidad (ej: "F:")
ruta_actual = os.getcwd() 
unidad = os.path.splitdrive(ruta_actual)[0] 

# 2. Creamos la ruta de la carpeta usando Path correctamente
# Agregamos una barra invertida al disco para que Path reconozca que es la raíz (ej: "F:\")
print(unidad)
op = input ("Enter para continuar")
if  unidad == "C:":
    CARPETA_DATOS = Path(unidad + "\\") / "Users" / "danie" / "Documents" / "Python Project" / "prueba" / "datos"
elif unidad =="F:":
    CARPETA_DATOS = Path(unidad + "\\") /"Python" / "Python Project" /"prueba"\"datos"


# 3. CONSEJO: Usa Path también para el archivo, es más limpio y evita mezclar os y pathlib
ARCHIVO_DATOS = CARPETA_DATOS / "personal.json"
ARCHIVO_DATOS = os.path.join(CARPETA_DATOS, "personal.json")


print(f"Carpeta: {CARPETA_DATOS}")
print(f"Archivo: {ARCHIVO_DATOS}")

op = input ("Enter para continuar")
