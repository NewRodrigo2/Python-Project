import os
from pathlib import Path
import json
from datetime import datetime

COLOR_TITULO = "\033[94m"  # Azul
COLOR_EXITO = "\033[92m"   # Verde
COLOR_ERROR = "\033[91m"   # Rojo
COLOR_ADMIN = "\033[95m"   # Morado (Para el menú de administrador)
COLOR_RESET = "\033[0m"    # Volver al color normal
AMARILLO = "\033[33m"
CIAN = "\033[36m"
CIAN_BRILLANTE = "\033[96m"
BG_CIAN = "\033[46m"

#.............................................................................
ruta_actual = os.getcwd() 
unidad = os.path.splitdrive(ruta_actual)[0] 
if unidad == "C:":
    CARPETA_DATOS = Path(unidad + "\\") / "Users" / "danie" / "Documents" / "Python Project" / "prueba" / "datos"
else:
    CARPETA_DATOS = Path(unidad + "\\") / "Python" / "Python Project" / "prueba" / "datos"

# 3. CONSEJO: Usa Path también para el archivo, es más limpio y evita mezclar os y pathlib
ARCHIVO_DATOS = CARPETA_DATOS / "inventario.json"
ARCHIVO_CONTROL = CARPETA_DATOS / "control.json"
ARCHIVO_TEX = CARPETA_DATOS / "autos_ordenados.txt"
PERSONAL = CARPETA_DATOS / "personal.json"  # <-- Esta es la línea clave
#................................................................................

control = [] 
# inventario = [] 

def dibu_enca(titu, ancho, simbolo, color_text="\033[94m"):
    espacios = '    '
    print (espacios)
    print(f"{color_text}{simbolo * ancho}\033[0m ")
    print(f"{color_text}{titu:^{ancho}}\033[0m")
    print(f"{color_text}{simbolo * ancho}\033[0m ")

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def row_space():
    label = "ENTER PARA CONTINUAR ..."
    wait = input(f"\n {AMARILLO}{label:^{50}}{COLOR_RESET} ")

def guardar_inventario(inventario):
    """Guarda el estado actual del inventario en el archivo JSON."""
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
           input("DEBUG: abriendo archivo inventario")
           json.dump(inventario, archivo, indent=4, ensure_ascii=False)
           input("DEBUG: agregando al archivo inventario")
    except Exception as e:
        print(f"\n{COLOR_ERROR}Error al guardar el archivo: {e}{COLOR_RESET}")

def guarda_control():                          # >>>>>>>>>>>>>>>>>>>> guardando archivo control.json 
    try:
        with open(ARCHIVO_CONTROL, "w", encoding="utf-8") as archivo_control:
           json.dump(control, archivo_control, indent=4, ensure_ascii=False)     
    except Exception as b:     
        print(f"\n{COLOR_ERROR}Error al guardar el archivo de control: {b}{COLOR_RESET}")          
