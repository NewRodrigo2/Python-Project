# MODIFICADO EL 10/07/26  11:19
# C:\Users\danie\Documents\Python Project> git switch secund_pba_branch.py
import os
import json
import msvcrt  # Librería nativa de Windows para capturar teclas al instante
from datetime import datetime

''' de mis script'''
import herramientas  as h


# Constantes para los colores en la terminal (Códigos ANSI)
COLOR_TITULO = "\033[94m"  # Azul
COLOR_EXITO = "\033[92m"   # Verde
COLOR_ERROR = "\033[91m"   # Rojo
COLOR_ADMIN = "\033[95m"   # Morado (Para el menú de administrador)
COLOR_RESET = "\033[0m"    # Volver al color normal
AMARILLO = "\033[33m"
CIAN = "\033[36m"
CIAN_BRILLANTE = "\033[96m"
BG_CIAN = "\033[46m"

CARPETA_DATOS = r"C:\Users\danie\Documents\Python Project\prueba\datos"
ARCHIVO_DATOS = os.path.join(CARPETA_DATOS, "personal.json")
# ARCHIVO_CONTROL = os.path.join(CARPETA_DATOS, "control.json")   # >>>>>>>>>>>>>>>>>>  Agregando un nuevo archivo 
# ARCHIVO_TEX = os.path.join(CARPETA_DATOS, "autos_ordenados.txt")

personal = {
    "id_emp": "1",
    "nombre": "Jose Perez Jimenez",
    "area": "mantenimiento",
    "hrs_cont": 40,
    "hrs_trab": 99,
    "sueldo": 9,
    "ausencias": 9
}

def guardar_inventario():
    """Guarda el estado actual del inventario en el archivo JSON."""
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
           json.dump(personal, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"\n{COLOR_ERROR}Error al guardar el archivo: {e}{COLOR_RESET}")

def menu_util():
    input("estoy trabajando ten paciencia   Entre para continuar")
    guardar_inventario()
    input("archivo creado .....   Entre para continuar")


if __name__ == "__main__":
    menu_util()
