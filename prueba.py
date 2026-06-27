# ESTE ARCHIVO FUE MODIFICADO EL 24/06/26 con modificaciones en 
# 1.- creando nuevo diccionario 
# CREADO EN LA USB   ---> BUSCAR LA MENERA DE PASARLO A LA COMPUTADORA VIA GIT O Github
# por eso la ruta del .json se debe de modificar
# haciendo un cambio ya que git dice que no existe el script
import os
import json
from datetime import datetime

# Constantes para los colores en la terminal (Códigos ANSI)
COLOR_TITULO = "\033[94m"  # Azul
COLOR_EXITO = "\033[92m"   # Verde
COLOR_ERROR = "\033[91m"   # Rojo
COLOR_ADMIN = "\033[95m"   # Morado (Para el menú de administrador)
COLOR_RESET = "\033[0m"    # Volver al color normal

#................................................................................
# RUTA SOLICITADA: Se usa os.path.join para evitar problemas con las barras invertidas en Windows
CARPETA_DATOS = r"D:\programacion\python"
# CARPETA_DATOS = os.path.abspath(r"E:\Python\Python Project\datos")
ARCHIVO_DATOS = os.path.join(CARPETA_DATOS, "inventario.json")
ARCHIVO_CONTROL = os.path.join(CARPETA_DATOS, "control.json")   # >>>>>>>>>>>>>>>>>>  Agregando un nuevo archivo 
#................................................................................

# === SOLUCIÓN USB: RUTA AUTOMATIZADA ===
# Detecta dinámicamente dónde está corriendo este archivo en tu memoria USB
#CARPETA_PROYECTO = os.path.dirname(os.path.abspath(__file__))

# Crea de forma limpia una carpeta llamada "datos" dentro del directorio del script
#CARPETA_DATOS = os.path.join(CARPETA_PROYECTO, "datos")
#ARCHIVO_DATOS = os.path.join(CARPETA_DATOS, "inventario.json")


CLAVE_ADMIN = "admin123" # Contraseña para la opción oculta

# Inventario inicial por defecto (solo se usa si el archivo JSON no existe)
INVENTARIO_DEFECTO = [
    {"id": 1, "marca": "Toyota", "modelo": "Yaris", "precio_dia": 45, "disponible": True, "dias": 0, "km": 0, "venta": 0},
    {"id": 2, "marca": "Nissan", "modelo": "Versa", "precio_dia": 50, "disponible": True, "dias": 0, "km": 0, "venta": 0},
    {"id": 3, "marca": "Chevrolet", "modelo": "Aveo", "precio_dia": 40, "disponible": False, "dias": 0, "km": 0, "venta": 0}
]
 # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> manejando fechas , creando diccionario 
fecha_renta = "01/01/2026"
# fecha_obj = datetime.strptime(fecha_renta, "%d/%m/%Y").date()
AUTO_CONTROL = [
    {
        "c_id": 1, "km_recorridos": 0, 
        "c_venta_total": 0, 
        "c_fecha_renta":fecha_renta,
        "c_dias": 0
        } 
]
control = []          # >>>>>>>>>>>>>>>>>>>>>>>> 
inventario = []      #  Arreglo vacio

def cargar_inventario():
    """Lee los archivos JSON de inventario y control. Si no existen, los crea."""
    global inventario  
    global control     

    try:
        # 1. Asegurar que la carpeta contenedora exista
        if not os.path.exists(CARPETA_DATOS):
            os.makedirs(CARPETA_DATOS)
            print(f"Creando carpeta de datos: {CARPETA_DATOS}")
            row_space()

        # Diagnóstico temporal de archivos existentes
        print(f"\nVerificando carpeta: {CARPETA_DATOS}")
        print("Archivos encontrados:", os.listdir(CARPETA_DATOS))
        row_space()

        # 2. Manejo de ARCHIVO_DATOS (Inventario)
        if os.path.exists(ARCHIVO_DATOS):
            with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
                inventario = json.load(archivo)
            print("✓ Archivo inventario.json cargado con éxito.")
        else:
            inventario = INVENTARIO_DEFECTO
            print("⚠ No se encontró inventario.json. Usando datos por defecto.")
            guardar_inventario()

        # 3. Manejo de ARCHIVO_CONTROL (Control de renta)
        if os.path.exists(ARCHIVO_CONTROL):
            with open(ARCHIVO_CONTROL, "r", encoding="utf-8") as archivo_control:
                control = json.load(archivo_control)
            print("✓ Archivo control.json cargado con éxito.")
        else:
            control = AUTO_CONTROL  # Inicializa con tu estructura base de control
            print("⚠ No se encontró control.json. Inicializando datos de control.")
            guarda_control()
            row_space()

    except Exception as e:
        # Respaldo de emergencia en caso de fallo catastrófico de lectura/escritura
        inventario = INVENTARIO_DEFECTO
        control = AUTO_CONTROL
        print(f"\n{COLOR_ERROR}Error crítico al cargar archivos ({e}). Usando datos temporales.{COLOR_RESET}")
        row_space()


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
    print(f"================================================={COLOR_RESET} ")
    for auto in inventario:
        estado = f"{COLOR_EXITO}Disponible{COLOR_RESET}" if auto["disponible"] else f"{COLOR_ERROR}Rentado{COLOR_RESET}"
        print(f"[{auto['id']}] {auto['marca']} {auto['modelo']} - ${auto['precio_dia']}/día ({estado}) rentado por {COLOR_ADMIN}{auto['dias']} dias{COLOR_RESET}")

def mostrar_informe():                                                                  # >>>>>>>> def para mostrar el informe 
    print(f"\n{COLOR_TITULO}=================================================")
    print("------- INFORME DE AUTOS  -------")
    print(f"================================================={COLOR_RESET} ")
    for auto_c in control:
        estado = f"{COLOR_EXITO}Disponible{COLOR_RESET}" if auto_c["disponible"] else f"{COLOR_ERROR}Rentado{COLOR_RESET}"
        print(f"[{auto_c['id']}] {auto_c['venta_total']} {auto_c['fecha_renta']} {auto_c['dias']}{COLOR_RESET}")        

def mostrar_inv_disp():
    print(f"\n{COLOR_TITULO}=================================================")
    print("------- INVENTARIO DE AUTOS DISPONIBLES -------")
    print(f"================================================={COLOR_RESET} ")
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
    print(f"================================================={COLOR_RESET} ")
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
        row_space()
        
def regresar_auto():
    mostrar_inv_no_disp()
    try:
        id_regresa = int(input("\nIngrese el ID del auto que desea REGRESAR: "))
        km_recorridos = float(input("Ingrese los kilómetros recorridos en este viaje: "))
        for auto in inventario:
            if auto["id"] == id_regresa:
                if not auto["disponible"]: 

                    auto["disponible"] = True
                    auto["km"] = km_recorridos
                    auto["venta"] = auto['dias'] * auto['precio_dia'] + km_recorridos

                    limpiar_pantalla()
                    print (f"\nkilometros recorridos" , km_recorridos)
                    print(f"\ntotal a pagar es de: $ {auto['venta']}  por  {auto['dias']} dias de uso")
                    auto["dias"] = 0
                    auto["km"] = 0
                    print(f"\n{COLOR_EXITO}¡Éxito! Auto regresado exitosamente: {auto['marca']} {auto['modelo']}.{COLOR_RESET}")
                    # lineas de control para conocer los valores de las variables 
                    print ("c_id")
                    print ("c_venta")
                    row_space()                      #  enter para continuar
                    guardar_inventario()
                    return
                else:
                    limpiar_pantalla()
                    print(f"\n{COLOR_ERROR}Este auto  (no está rentado).{COLOR_RESET}")
                    row_space()
                    return
                    
        limpiar_pantalla()
        print(f"\n{COLOR_ERROR}El ID introducido no existe.{COLOR_RESET}")
        row_space()
                    
    except ValueError:
        print(f"\n{COLOR_ERROR}Por favor, introduzca un número válido.{COLOR_RESET}")
        row_space()

# ===========================================================================================================
# SECCIÓN OCULTA: ADMINISTRACIÓN
# ===========================================================================================================
def menu_administrador():
    """Submenú protegido para agregar vehículos nuevos."""
    while True:
        limpiar_pantalla()
        print(f"{COLOR_ADMIN}=================================")
        print("    PANEL DE ADMINISTRACIÓN      ")
        print(f"================================={COLOR_RESET}")
        print("1. Agregar nuevo auto al inventario")
        print("2. Ver informe de autos ")
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

        elif opcion == "2":
            print ("Informe de autos rentados")

                
        elif opcion == "9":    # ----------------  9 
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