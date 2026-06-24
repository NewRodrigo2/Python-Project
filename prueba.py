# estoy probando como controlar los branch, ya que perdi una vez todo mi trabajo
# 24/06/26 12:17
import os
import json

# Constantes para los colores en la terminal (Códigos ANSI)
COLOR_TITULO = "\033[94m"  # Azul
COLOR_EXITO = "\033[92m"   # Verde
COLOR_ERROR = "\033[91m"   # Rojo
COLOR_ADMIN = "\033[95m"   # Morado (Para el menú de administrador)
COLOR_RESET = "\033[0m"    # Volver al color normal

# RUTA SOLICITADA: Se usa os.path.join para evitar problemas con las barras invertidas en Windows
CARPETA_DATOS = r"D:\programacion\python"
ARCHIVO_DATOS = os.path.join(CARPETA_DATOS, "inventario.json")

# Contraseña para la opción oculta
CLAVE_ADMIN = "admin123"

# Inventario inicial por defecto (solo se usa si el archivo JSON no existe)
INVENTARIO_DEFECTO = [
    {"id": 1, "marca": "Toyota", "modelo": "Yaris", "precio_dia": 45, "disponible": True, "dias": 0, "km": 0, "venta": 0},
    {"id": 2, "marca": "Nissan", "modelo": "Versa", "precio_dia": 50, "disponible": True, "dias": 0, "km": 0, "venta": 0},
    {"id": 3, "marca": "Chevrolet", "modelo": "Aveo", "precio_dia": 40, "disponible": False, "dias": 0, "km": 0, "venta": 0}
]

inventario = [] #  Arreglo vacio

def cargar_inventario():
    """Lee el archivo JSON. Si la carpeta o el archivo no existen, los crea."""
    global inventario  # define que se use la varible creada fuera de esta funcion
    try:
        # Crea la carpeta D:\programacion\python si no existe en el disco duro
        if not os.path.exists(CARPETA_DATOS):
            os.makedirs(CARPETA_DATOS)
            
        if os.path.exists(ARCHIVO_DATOS):
            with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
                inventario = json.load(archivo)
        else:
            inventario = INVENTARIO_DEFECTO
            guardar_inventario()
    except Exception as e:
        # Si hay un error de permisos o disco, usa el defecto de forma temporal
        inventario = INVENTARIO_DEFECTO

def guardar_inventario():
    """Guarda el estado actual del inventario en el archivo JSON."""
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump(inventario, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"\n{COLOR_ERROR}Error al guardar el archivo: {e}{COLOR_RESET}")

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def row_space():
    print(".")
    print(".")
    wait = input(f"\n {COLOR_TITULO}ENTER PARA CONTINUAR ..{COLOR_RESET} ")

def mostrar_inventario():
    print(f"\n{COLOR_TITULO}=================================================")
    print("------- INVENTARIO DE AUTOS -------")
    print(f"\n ================================================={COLOR_RESET} ")
    for auto in inventario:
        estado = f"{COLOR_EXITO}Disponible{COLOR_RESET}" if auto["disponible"] else f"{COLOR_ERROR}Rentado{COLOR_RESET}"
        print(f"[{auto['id']}] {auto['marca']} {auto['modelo']} - ${auto['precio_dia']}/día ({estado}) rentado por {auto['dias']}")

def mostrar_inv_disp():
    print(f"\n{COLOR_TITULO}=================================================")
    print("------- INVENTARIO DE AUTOS DISPONIBLES -------")
    print(f"\n ================================================={COLOR_RESET} ")
    sum_disp = 0
    for auto in inventario:
        if auto["disponible"]:
            estado = f"{COLOR_EXITO}Disponible{COLOR_RESET}" if auto["disponible"] else f"{COLOR_ERROR}Rentado{COLOR_RESET}"
            print(f"[{auto['id']}] {auto['marca']} {auto['modelo']} - ${auto['precio_dia']}/día ({estado})")
            sum_disp = sum_disp + 1
    print (f"\n{COLOR_ADMIN} Total de autos en la lista: {sum_disp}{COLOR_RESET}")


def mostrar_inv_no_disp():
    print(f"\n{COLOR_TITULO}=================================================")
    print("------- INVENTARIO DE AUTOS NO DISPONIBLES -------")
    print(f"\n ================================================={COLOR_RESET} ")
    sum_disp = 0
    for auto in inventario:
        if not auto["disponible"]:
            estado = f"{COLOR_EXITO}Disponible{COLOR_RESET}" if auto["disponible"] else f"{COLOR_ERROR}Rentado{COLOR_RESET}"
            print(f"[{auto['id']}] {auto['marca']} {auto['modelo']} - ${auto['precio_dia']}/día ({estado})")
            sum_disp = sum_disp + 1
    print (f"\n{COLOR_ADMIN} Total de autos en la lista: {sum_disp}{COLOR_RESET}")    


def rentar_auto():
    mostrar_inv_disp()
    try:
        id_renta = int(input("\nIngrese el ID del auto que desea RENTAR: "))
        dias_p_renta = int(input("\nDias que desea rentar:"))
       
        for auto in inventario:
            if auto["id"] == id_renta:
                if auto["disponible"]:
                    auto["disponible"] = False
                    auto["dias"] = dias_p_renta
                    auto["venta"] = (dias_p_renta*auto["precio_dia"])
                    auto["km"] = 0
                    # auto["venta"] = 0
                    guardar_inventario()
                    limpiar_pantalla()
                    print(f"\n{COLOR_EXITO}¡Éxito! Ha rentado el {auto['marca']} {auto['modelo']}.{COLOR_RESET}")
                    print(f"\n{COLOR_EXITO}Presupuesto estimado en dias / costo por dia: ${dias_p_renta * auto['precio_dia']}{COLOR_RESET}")
                    row_space()
                    return
                else:
                    limpiar_pantalla()
                    print(f"\n{COLOR_ERROR}Lo sentimos, este auto ya está rentado.{COLOR_RESET}")
                    row_space()
                    return
        limpiar_pantalla()
        print(f"\n{COLOR_ERROR}El ID introducido no existe.{COLOR_RESET}")
        row_space()
    except ValueError:
        print(f"\n{COLOR_ERROR}Por favor, introduzca un número válido.{COLOR_RESET}")
        
def regresar_auto():
    mostrar_inv_no_disp()
    try:
        id_regresa = int(input("\nIngrese el ID del auto que desea REGRESAR: "))
        km_recorridos = float(input("Ingrese los kilómetros recorridos en este viaje: "))
        for auto in inventario:
            if auto["id"] == id_regresa:
                if not auto["disponible"]: 
                    limpiar_pantalla()                  
                    print(f"total a pagar es de: $ {auto['dias'] * auto['precio_dia'] + auto['km']}")
                    print(f"\n{COLOR_EXITO}¡Éxito! Auto regresado exitosamente: {auto['marca']} {auto['modelo']}.{COLOR_RESET}")
                    row_space()        #  enter para continuar
                    auto["disponible"] = True
                    auto["km"] = km_recorridos
                    auto["venta"] = auto['dias'] * auto['precio_dia'] + km_recorridos
                    auto["dias"] = 0
                    auto["km"] = 0
                    guardar_inventario()
                    return
                else:
                    limpiar_pantalla()
                    print(f"\n{COLOR_ERROR}Este auto  (no está rentado).{COLOR_RESET}")
                    # row_space()
                    return
                    
        limpiar_pantalla()
        print(f"\n{COLOR_ERROR}El ID introducido no existe.{COLOR_RESET}")
        row_space()
                    
    except ValueError:
        print(f"\n{COLOR_ERROR}Por favor, introduzca un número válido.{COLOR_RESET}")
        row_space()

# =============================================================================================
# SECCIÓN OCULTA: ADMINISTRACIÓN
# =============================================================================================
def menu_administrador():
    """Submenú protegido para agregar vehículos nuevos."""
    while True:
        limpiar_pantalla()
        print(f"{COLOR_ADMIN}=================================")
        print("    PANEL DE ADMINISTRACIÓN      ")
        print(f"================================={COLOR_RESET}")
        print("1. Agregar nuevo auto al inventario")
        print("9. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción (1-2): ")
        
        if opcion == "1":
            limpiar_pantalla()
            print(f"{COLOR_ADMIN}========================================")
            print("----- REGISTRAR NUEVO VEHÍCULO ----")
            print(f"========================================{COLOR_RESET}")
            try:
                marca = input("Marca del auto: ").strip()
                modelo = input("Modelo del auto: ").strip()
                precio = float(input("Precio de renta por día ($): "))
                dias = 0
                km = 0
                venta = 0
                
                if marca == "" or modelo == "":
                    print(f"\n{COLOR_ERROR}La marca y el modelo no pueden estar vacíos.{COLOR_RESET}")
                    row_space()
                    continue
                
                # Autogenerar el ID buscando el número más alto actual + 1
                nuevo_id = max([auto["id"] for auto in inventario]) + 1 if inventario else 1
                
                nuevo_auto = {
                    "id": nuevo_id,
                    "marca": marca,
                    "modelo": modelo,
                    "precio_dia": precio,
                    "disponible": True,
                    "dias": dias,
                    "km": km,
                    "venta": venta
                }
                
                inventario.append(nuevo_auto)
                guardar_inventario()
                
                print(f"\n{COLOR_EXITO}¡Vehículo registrado con éxito! Asignado ID: [{nuevo_id}]{COLOR_RESET}")
                row_space()
                
            except ValueError:
                print(f"\n{COLOR_ERROR}Error: El precio debe ser un número válido.{COLOR_RESET}")
                row_space()
                
        elif opcion == "9":
            break
        else:
            print(f"\n{COLOR_ERROR}Opción no válida.{COLOR_RESET}")
            row_space()

# ===========================================================================================================

def menu_principal():
    cargar_inventario()
    while True:
        limpiar_pantalla()
        print(f"{COLOR_TITULO}\n=====================================")
        print("   BIENVENIDO A MI CARRITO EN RENTA   ")
        print(f"====================================={COLOR_RESET}")
        print("1. Ver autos disponibles")
        print("2. Rentar un auto")
        print("3. Entregar un auto")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "1":
            limpiar_pantalla()
            mostrar_inventario()
            row_space()
        elif opcion == "2":
            limpiar_pantalla()
            rentar_auto()
        elif opcion == "3":
            limpiar_pantalla()
            regresar_auto()
        elif opcion == "4":
            limpiar_pantalla()
            print(f"\n{COLOR_EXITO}¡Gracias por usar Mi Carrito en Renta! Hasta pronto.{COLOR_RESET}\n")
            break
        # TRUCO: Si el usuario escribe la contraseña secreta, entra al menú administrador
        elif opcion == CLAVE_ADMIN:
            menu_administrador()
        else:
            limpiar_pantalla()
            print(f"\n{COLOR_ERROR}Opción no válida. Intente de nuevo.{COLOR_RESET}")
            row_space()

if __name__ == "__main__":
    menu_principal()
