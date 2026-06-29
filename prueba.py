# ESTE ARCHIVO FUE MODIFICADO EL 27/06/26 
# C:\Users\danie\Documents\Python Project> git switch secund_pba_branch.py
#  modificaciones en 
# 1.- Se actualizo def cargar_inventario / ya funciona la ruta 
# 2.- En proceso de modificar guarda_control(). 
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

def dibu_enca(titu, ancho, simbolo, color_text="\033[94m"):
    print(f"{color_text}{simbolo * ancho}\033[0m ")
    print(f"{color_text}{titu:^{ancho}}\033[0m")
    print(f"{color_text}{simbolo * ancho}\033[0m ")

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
    dibu_enca("INVENTARIO DE AUTOS", 70, "=")                                          #  dibujando enca
    print(f"{'ID':<4} | {'Marca':<12} | {'Modelo':<12} | {'Precio/Día':<12} | Estado")
    print("-" * 69)

    for auto in inventario:
        estado = f"{COLOR_EXITO}Disponible{COLOR_RESET}" if auto["disponible"] else f"{COLOR_ERROR}Rentado{COLOR_RESET}"
        # print(f"[{auto['id']}] {auto['marca']} {auto['modelo']} - ${auto['precio_dia']}/día ({estado}) rentado por {COLOR_ADMIN}{auto['dias']} dias{COLOR_RESET}")
        print(f"[{auto['id']:<2}] | {auto['marca']:<12} | {auto['modelo']:<12} | ${auto['precio_dia']:<11} | {COLOR_ERROR}{estado}{COLOR_RESET}")

def mostrar_informe():                                                                  # >>>>>>>> def para mostrar el informe 
    print(f"\n{COLOR_TITULO}=================================================")
    print("------- INFORME DE AUTOS  -------")
    print(f"================================================={COLOR_RESET} ")
    for auto_c in control:
        estado = f"{COLOR_EXITO}Disponible{COLOR_RESET}" if auto_c["disponible"] else f"{COLOR_ERROR}{estado}{COLOR_RESET}"
        print(f"[{auto_c['id']}] {auto_c['venta_total']} {auto_c['fecha_renta']} {auto_c['dias']}{COLOR_RESET}")        

def mostrar_inv_disp():
    print(f"\n{COLOR_TITULO}{'=' * 69}")
    print("------- INVENTARIO DE AUTOS DISPONIBLES -------")
    print(f"{'=' * 69}{COLOR_RESET} ")
    print(f"{'ID':<4} | {'Marca':<12} | {'Modelo':<12} | {'Precio/Día':<12} | Estado")
    print("-" * 69)
    sum_disp = 0              # inicializa variable
    for auto in inventario:
        if auto["disponible"]:
            estado = f"{COLOR_EXITO}Disponible{COLOR_RESET}" if auto["disponible"] else f"{COLOR_ERROR}Rentado{COLOR_RESET}"
            print(f"[{auto['id']:<2}] | {auto['marca']:<12} | {auto['modelo']:<12} | ${auto['precio_dia']:<11} | {COLOR_ERROR}estado{COLOR_RESET}")
            # print(f"[{auto['id']}] {auto['marca']} {auto['modelo']} - ${auto['precio_dia']}/día ({estado})")
            sum_disp = sum_disp + 1
    print (f"\n{COLOR_ADMIN} Total de autos en la lista: {sum_disp}{COLOR_RESET}")


def mostrar_inv_no_disp():
    print(f"{COLOR_TITULO}{'=' * 69}")
    print("                 INVENTARIO DE AUTOS NO DISPONIBLES")
    print(f"{'=' * 69}{COLOR_RESET}")
    
    # Encabezado de la tabla alineado
    # ID ocupa 4 espacios, Marca 12 espacios, Modelo 12 espacios
    print(f"{'ID':<4} | {'Marca':<12} | {'Modelo':<12} | {'Precio/Día':<12} | Estado")
    print(f"{COLOR_ADMIN}{'=' * 69}{COLOR_RESET}")
    
    sum_disp = 0
    for auto in inventario:
        if not auto["disponible"]:
            # Usamos marcadores de posición fijos (<12 significa alineado a la izquierda con 12 espacios)
            # Nota: El estado se imprime al final para que los códigos ANSI de color no rompan la alineación
            print(f"[{auto['id']:<2}] | {auto['marca']:<12} | {auto['modelo']:<12} | ${auto['precio_dia']:<11} | {COLOR_ERROR}Rentado{COLOR_RESET}")
            sum_disp += 1
            
    print("-" * 69)
    print(f"{COLOR_ADMIN} Total de autos rentados: {sum_disp}{COLOR_RESET}\n")
 

def rentar_auto():
    mostrar_inv_disp()
    try:
        id_renta = int(input("\nIngrese el ID del auto que desea RENTAR: "))
        dias_p_renta = int(0)
        for auto in inventario:
            if auto["id"] == id_renta:
                if auto["disponible"]:
                    auto["disponible"] = False
                    auto["dias"] = dias_p_renta
                    auto["venta"] = (dias_p_renta*auto["precio_dia"])
                    auto["km"] = 0
                    guardar_inventario()
                    dias_p_renta = int(input("\nDias que desea rentar:"))
                    print(f"\n{COLOR_EXITO}¡Éxito! Ha rentado el {auto['marca']} {auto['modelo']}.{COLOR_RESET}")
                    print(f"\n{COLOR_EXITO}Presupuesto estimado: ${dias_p_renta * auto['precio_dia']}{COLOR_RESET}")
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
    global inventario
    global control
    
    limpiar_pantalla()
    # print(f"{COLOR_TITULO}=== REGRESAR AUTO RENTADO (NUEVA TRANSACCIÓN) ==={COLOR_RESET}\n")
    
    # 1. Filtrar solo autos rentados
    rentados = [auto for auto in inventario if not auto["disponible"]]
    if not rentados:
        print(f"{COLOR_ERROR}No hay autos rentados en este momento.{COLOR_RESET}")
        input("\nPresione Enter para continuar...")
        return

    # Mostrar la lista usando tu enfoque estilizado
    mostrar_inv_no_disp()
    
    try:
        id_regresar = int(input(" \n      Ingrese el ID del auto a regresar:"))
    except ValueError:
        print(f"{COLOR_ERROR}ID inválido. Debe ser un número.{COLOR_RESET}")
        input("\n      Presione Enter para continuar...")
        return

    # 2. Buscar el auto en el inventario general
    auto_encontrado = None
    for auto in inventario:
        if auto["id"] == id_regresar and not auto["disponible"]:
            auto_encontrado = auto
            break

    if auto_encontrado:
        try:
            dias = int(input(f"\n¿Cuántos días UTILIZO el {auto_encontrado['marca']}?"))
            km_nuevos = int(input("\n¿Cuántos kilómetros recorrió?"))
            if dias <= 0 or km_nuevos < 0:
                print(f"{COLOR_ERROR}Valores inválidos. No se admiten números negativos o días en 0.{COLOR_RESET}")
                input("\nPresione Enter para continuar...")
                return
        except ValueError:
            print(f"{COLOR_ERROR}Entrada inválida. Ingrese números enteros.{COLOR_RESET}")
            input("\nPresione Enter para continuar...")
            return

        # 3. Calcular costos
        costo_total = auto_encontrado["precio_dia"] * dias
        fecha_actual = datetime.now().strftime("%d/%m/%Y")

        # 4. Actualizar estado en INVENTARIO (Estado actual)
        auto_encontrado["disponible"] = True
        auto_encontrado["dias"] += dias
        auto_encontrado["km"] += km_nuevos
        auto_encontrado["venta"] += costo_total

        # 5. CREAR UN REGISTRO NUEVO E INDEPENDIENTE EN CONTROL (Historial Permanente)
        num_transaccion = len(control) + 1  # Auto-incrementa el número de ticket
        
        nueva_renta = {
            "transaccion_id": num_transaccion,
            "c_id": auto_encontrado["id"],
            "c_marca": auto_encontrado["marca"],
            "c_modelo": auto_encontrado["modelo"],
            "km_recorridos": km_nuevos,
            "c_venta_total": costo_total,
            "c_fecha_renta": fecha_actual,
            "c_dias": dias
        }
        control.append(nueva_renta) # Agrega la nueva fila al final de la lista

        # 6. Guardar en los dos archivos JSON
        guardar_inventario()
        guarda_control()

        print(f"\n{COLOR_EXITO}¡Auto regresado con éxito!{COLOR_RESET}")
        print(f"Ticket N°: {num_transaccion} | Total cobrado: {COLOR_EXITO}${costo_total}{COLOR_RESET}")
        
    else:
        print(f"{COLOR_ERROR}El ID ingresado no corresponde a un vehículo rentado.{COLOR_RESET}")
        
    input("\nPresione Enter para continuar...")


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
        dibu_enca("BIENVENIDO A MI CARRITO EN RENTA", 70, "=")
        # print(f"{COLOR_TITULO}\n=====================================")
        # print("   BIENVENIDO A MI CARRITO EN RENTA   ")
        # print(f"====================================={COLOR_RESET}")
        print(f"\n1. Ver autos disponibles")
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