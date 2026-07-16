# MODIFICADO EL 16/07/26
# 
# penidientes: terminar de agregar el nuevo personal al diccionario new_personal
# verificar el diccionario en archivo personal.json
# append para pasar a new_diccionario o a personal ??
#  

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

personal = [{
    "id_emp": "1",
    "nombre": "Jose Perez Jimenez",
    "area": "mantenimiento",
    "hrs_cont": 40,
    "hrs_trab": 99,
    "sueldo": 9,
    "ausencias": 9,
    "pasword": "qwer"
}
]

def guardar_inventario_personal(archi):
    """Guarda el estado actual del inventario en el archivo JSON."""
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
           json.dump(archi, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"\n{COLOR_ERROR}Error al guardar el archivo: {e}{COLOR_RESET}")

    input("estoy trabajando ten paciencia   Enter.... para continuar....")
    input("archivo creado .....   Entre para continuar")


new_personal = {}
def abre_inventario_personal():
    global new_personal

    # 2. Manejo de ARCHIVO_DATOS (personal)
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            new_personal = json.load(archivo)
        print("✓ Archivo inventario.json cargado con éxito.")
    else:
        print("⚠ No se encontró inventario.json. Usando datos por defecto.")
        h.guardar_inventario()

def agregar_personal():
    h.limpiar_pantalla()
    h.dibu_enca("Agregando nuevo persolal", 80,"#")
    op = input (f'\n desea agregar nuevo empleado   s/n')
    nuevo_id = max([auto["id"] for auto in new_personal]) + 1 if new_personal else 1
    if op == 's':
        abre_inventario_personal()
        id = input ('Id:  ' )
        nom = input ('Nombre:  ' )
        area = input ('Area:  ' )
        hcot = input ('Horas contratadas:  ' )
        htra = input ('Horas Trabajadas:  ' )
        sdo = input ('Sueldo: ')
        aus = input ('Ausencias: ')
        pas = input ('Password: ')

        new_personal['id_emp']= id
        new_personal['nombre']= nom
        new_personal['area']= area
        new_personal['hrs_cont']= hcot
        new_personal['hrs_trab']= htra
        new_personal['sueldo']= sdo
        new_personal['ausencias']= aus
        new_personal['pasword']= pas
    new_personal.append(nuevo_auto)
    c = input ('Datos correctos ?.... s/n')
    if c == 's':
        guardar_inventario_personal(new_personal)
        h.row_space()

def menu_util():
    while True: 
        h.limpiar_pantalla()
        h.dibu_enca("CONTROL DE  PERSONAL ", 80,"#")
        print ('1.- crear archivo nuevo')
        print ('2.- agregar personal nuevo')
        print ('3.- salir ..')

        op2 = input ('Seleccione una opcion')
        if op2 == '1':
            guardar_inventario_personal(personal)
        if op2 == '2':
            agregar_personal()
        elif op2 == '3':
            break

if __name__ == "__main__":
    menu_util()
