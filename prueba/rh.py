''' 
Modificar estructura de la ruta
'''
import os
import json
import msvcrt                  # Librería nativa de Windows para capturar teclas al instante
from datetime import datetime
from pathlib import Path
import herramientas  as h

COLOR_TITULO = "\033[94m"  # Azul
COLOR_EXITO = "\033[92m"   # Verde
COLOR_ERROR = "\033[91m"   # Rojo
COLOR_ADMIN = "\033[95m"   # Morado (Para el menú de administrador)
COLOR_RESET = "\033[0m"    # Volver al color normal
AMARILLO = "\033[33m"
CIAN = "\033[36m"
CIAN_BRILLANTE = "\033[96m"
BG_CIAN = "\033[46m"

ruta_actual = os.getcwd() 
unidad = os.path.splitdrive(ruta_actual)[0] 
if unidad == "C:":
    CARPETA_DATOS = Path(unidad + "\\") / "Users" / "danie" / "Documents" / "Python Project" / "prueba" / "datos"
else:
    CARPETA_DATOS = Path(unidad + "\\") / "Python" / "Python Project" / "prueba" / "datos"

# 3. CONSEJO: Usa Path también para el archivo, es más limpio y evita mezclar os y pathlib
ARCHIVO_DATOS = CARPETA_DATOS / "personal.json"

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

new_personal = []
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
    global new_personal
    h.limpiar_pantalla()
    h.dibu_enca("Agregando nuevo personal", 80, "#")
    
    op = input('\n¿Desea agregar nuevo empleado? s/n: ').lower()
    
    if op == 's':
        # 1. Primero cargamos lo que ya existe en el archivo JSON
        abre_inventario_personal() 
        
        # 2. Calculamos el siguiente ID automáticamente basado en "id_emp"
        # Convertimos a entero para poder usar max(), ya que en tu JSON está como texto "1"
        if new_personal:
            nuevo_id = max([int(emp["id_emp"]) for emp in new_personal]) + 1
        else:
            nuevo_id = 1
            
        print(f'Asignando ID automático: {nuevo_id}')
        nom = input('Nombre: ')
        area = input('Area: ')
        
        # Nota: Es recomendable guardar los números como enteros/flotantes en JSON, no como texto
        hcot = int(input('Horas contratadas: '))
        htra = int(input('Horas Trabajadas: '))
        sdo = float(input(f'Sueldo: '))
        aus = int(input('Ausencias: '))
        pas = input('Password: ')
        
        # 3. Creamos un diccionario EXCLUSIVO para el empleado nuevo
        empleado_nuevo = {
            "id_emp": str(nuevo_id), # Lo volvemos texto para mantener tu formato original
            "nombre": nom,
            "area": area,
            "hrs_cont": hcot,
            "hrs_trab": htra,
            "sueldo": sdo,
            "ausencias": aus,
            "pasword": pas
        }
        
        c = input('¿Datos correctos? s/n: ').lower()
        if c == 's':
            # 4. LA CLAVE DE LA LÓGICA: Añadimos el nuevo diccionario a la lista global
            new_personal.append(empleado_nuevo)
            
            # 5. Guardamos la lista completa actualizada en el JSON
            guardar_inventario_personal(new_personal)
            print(f"{COLOR_EXITO}¡Personal agregado y guardado con éxito!{COLOR_RESET}")
            
        h.row_space()

def menu_util():
    label1 = ("1.- crear archivo nuevo \n")
    label2 = ("2.- agregar personal nuevo \n")
    label3 = ("3. Sueldos \n")
    label9 = ("9. Salir del programa \n")
    label10 = ("Seleccione una opcion .... \n")
    while True: 
        h.limpiar_pantalla()
        h.dibu_enca("CONTROL DE  PERSONAL ", 80,"#")
        print(f"{AMARILLO}{label1:^{80}}")
        print(f"{AMARILLO}{label2:^{80}}")
        print(f"{AMARILLO}{label9:^{80}}{COLOR_RESET}")
        op2 = input ('Seleccione una opcion  ')
        if op2 == '1':
            guardar_inventario_personal(personal)
        if op2 == '2':
            agregar_personal()
        elif op2 == '9':
            h.limpiar_pantalla()
            break

if __name__ == "__main__":
    menu_util()
