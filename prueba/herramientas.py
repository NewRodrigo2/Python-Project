'''
13/07/26 13:45

'''
import os
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

#................................................................................
CARPETA_DATOS = r"C:\Users\danie\Documents\Python Project\prueba\datos"
ARCHIVO_DATOS = os.path.join(CARPETA_DATOS, "inventario.json")
ARCHIVO_CONTROL = os.path.join(CARPETA_DATOS, "control.json")   # >>>>>>>>>>>>>>>>>>  Agregando un nuevo archivo 
ARCHIVO_TEX = os.path.join(CARPETA_DATOS, "autos_ordenados.txt")
#................................................................................
control = [] 
inventario = [] 


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

def guardar_inventario():
    """Guarda el estado actual del inventario en el archivo JSON."""
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
           json.dump(inventario, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"\n{COLOR_ERROR}Error al guardar el archivo: {e}{COLOR_RESET}")

def guarda_control():                          # >>>>>>>>>>>>>>>>>>>> guardando archivo control.json 
    try:
        with open(ARCHIVO_CONTROL, "w", encoding="utf-8") as archivo_control:
           json.dump(control, archivo_control, indent=4, ensure_ascii=False)     
    except Exception as b:     
        print(f"\n{COLOR_ERROR}Error al guardar el archivo de control: {b}{COLOR_RESET}")          

def menu_util():
    label1 = ("1.- crear archivo nuevo \n")
    label2 = ("2.- agregar personal nuevo \n")
    label3 = ("3. En proceso \n")
    label4 = ("4. En proceso \n")
    label5 = ("5. En proceso \n")
    label9 = ("9.- agregar personal nuevo \n")
    label10 = ("Seleccione una opcion .... \n")
    while True:
        limpiar_pantalla()
        dibu_enca("PANEL DE ADMINISTRACIÓN", 80, "=")
        print(f"{AMARILLO}{label1:^{80}}")
        print(f"{AMARILLO}{label2:^{80}}")
        print(f"{AMARILLO}{label3:^{80}}")
        print(f"{AMARILLO}{label4:^{80}}")
        print(f"{AMARILLO}{label5:^{80}}")
        print(f"{AMARILLO}{label9:^{80}}{COLOR_RESET}")
        opcion = input(f"\n{COLOR_EXITO}{label10:^{80}}{COLOR_RESET}")
          
        if opcion == "1":
            # guardar_inventario_personal(personal)
            None
        elif opcion == "2"  or opcion == "":     
            # agregar_personal()
            None
        elif opcion == "9"  or opcion == "":
            break
        else:
            print(f"\n{COLOR_ERROR}Opción no válida.{COLOR_RESET}")
            row_space()
            

          


if __name__ == "__main__":
    # Asegúrate de tener definidas las funciones crear_a, leer_a, etc.
    menu_util()