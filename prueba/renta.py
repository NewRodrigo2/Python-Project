# MODIFICADO EL 13/07/26  11:19 am
# C:\Users\danie\Documents\Python Project> git switch secund_pba_branch.py

import os
import json
import msvcrt  # Librería nativa de Windows para capturar teclas al instante
import customtkinter as ctk
import renta as rta

from datetime import datetime
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
#................................................................................
# RUTA SOLICITADA: Se usa os.path.join para evitar problemas con las barras invertidas en Windows
# CARPETA_DATOS = r"D:\programacion\python"
CARPETA_DATOS = r"C:\Users\danie\Documents\Python Project\prueba\datos"
# CARPETA_DATOS = os.path.abspath(r"E:\Python\Python Project\datos")
ARCHIVO_DATOS = os.path.join(CARPETA_DATOS, "inventario.json")
ARCHIVO_CONTROL = os.path.join(CARPETA_DATOS, "control.json")   # >>>>>>>>>>>>>>>>>>  Agregando un nuevo archivo 
ARCHIVO_TEX = os.path.join(CARPETA_DATOS, "autos_ordenados.txt")
#................................................................................

# === SOLUCIÓN USB: RUTA AUTOMATIZADA ===
# Detecta dinámicamente dónde está corriendo este archivo en tu memoria USB
#CARPETA_PROYECTO = os.path.dirname(os.path.abspath(__file__))

# Crea de forma limpia una carpeta llamada "datos" dentro del directorio del script
#CARPETA_DATOS = os.path.join(CARPETA_PROYECTO, "datos")
#ARCHIVO_DATOS = os.path.join(CARPETA_DATOS, "inventario.json")

CLAVE_ADMIN = "admin123" # Contraseña para la opción oculta

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
sp = ('=' * 10)     

    
def cargar_inventario():
    """Lee los archivos JSON de inventario y control. Si no existen, los crea."""
    global inventario  
    global control     

    try:
        # 1. Asegurar que la carpeta contenedora exista
        if not os.path.exists(CARPETA_DATOS):
            os.makedirs(CARPETA_DATOS)
            print(f"Creando carpeta de datos: {CARPETA_DATOS}")
            h.row_space()

        # 2. Manejo de ARCHIVO_DATOS (Inventario)
        if os.path.exists(ARCHIVO_DATOS):
            with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
                inventario = json.load(archivo)
            print("✓ Archivo inventario.json cargado con éxito.")
        else:
            inventario = INVENTARIO_DEFECTO
            print("⚠ No se encontró inventario.json. Usando datos por defecto.")
            h.guardar_inventario()

        # 3. Manejo de ARCHIVO_CONTROL (Control de renta)
        if os.path.exists(ARCHIVO_CONTROL):
            with open(ARCHIVO_CONTROL, "r", encoding="utf-8") as archivo_control:
                control = json.load(archivo_control)
            if len(control) > 0 and "c_marca" not in control[0]:
                control.pop(0)
            print("✓ Archivo control.json cargado con éxito.")
        else:
            control = AUTO_CONTROL  # Inicializa con tu estructura base de control
            print("⚠ No se encontró control.json. Inicializando datos de control.")
            h.guarda_control()
            h.row_space()

    except Exception as e:
        # Respaldo de emergencia en caso de fallo catastrófico de lectura/escritura
        inventario = INVENTARIO_DEFECTO
        control = AUTO_CONTROL
        print(f"\n{COLOR_ERROR}Error crítico al cargar archivos ({e}). Usando datos temporales.{COLOR_RESET}")
        h.row_space()





def mostrar_inventario():
    h.dibu_enca("INVENTARIO DE AUTOS", 70, "═")                                          #  dibujando enca
    print(f"{'ID':<4} | {'Marca':<12} | {'Modelo':<12} | {'Precio/Día':<12} | Estado")
    print("-" * 69)

    for auto in inventario:
       estado = f"{COLOR_EXITO}Disponible{COLOR_RESET}" if auto["disponible"] else f"{COLOR_ERROR}Rentado{COLOR_RESET}"
       # print(f"[{auto['id']}] {auto['marca']} {auto['modelo']} - ${auto['precio_dia']}/día ({estado}) rentado por {COLOR_ADMIN}{auto['dias']} dias{COLOR_RESET}")
       print(f"[{auto['id']:<2}] | {auto['marca']:<12} | {auto['modelo']:<12} | ${auto['precio_dia']:<11} | {COLOR_ERROR}{estado}{COLOR_RESET}")


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
    label = 'NVENTARIO DE AUTOS NO DISPONIBLES'
    print(f"{COLOR_TITULO}{'=' * 69}")
    print(f"{label:^{69}}")
    print(f"{'=' * 69}{COLOR_RESET}")
    
    # Encabezado de la tabla alineado
    # ID ocupa 4 espacios, Marca 12 espacios, Modelo 12 espacios
    print(f"{'ID':<4} | {'Marca':<12} | {'Modelo':<12} | {'Precio/Día':<12} | Presupuesto inicial")
    print(f"{COLOR_ADMIN}{'=' * 69}{COLOR_RESET}")
    
    sum_disp = 0
    for auto in inventario:
        if not auto["disponible"]:
            # Usamos marcadores de posición fijos (<12 significa alineado a la izquierda con 12 espacios)
            # Nota: El estado se imprime al final para que los códigos ANSI de color no rompan la alineación
            print(f"[{auto['id']:<2}] | {auto['marca']:<12} | {auto['modelo']:<12} | ${auto['precio_dia']:<11} | {COLOR_EXITO}{auto['venta']:<11} |{COLOR_RESET}")
            sum_disp += 1
            
    print("-" * 69)
    print(f"{COLOR_ADMIN} Total de autos rentados: {sum_disp}{COLOR_RESET}\n")
 
def rentar_auto():
    mostrar_inv_disp()
    pres_ini = 0
        
    try:
        print(f"{"=" * 50}")
        id_renta = int(input("\nIngrese el ID del auto que desea RENTAR:.. "))
        dias_p_renta = int(0)
        dias_p_renta = int(input(f"\nDias que desea rentar:..  "))
        for auto in inventario:
            if auto["id"] == id_renta:
                if auto["disponible"]:
                    auto["disponible"] = False
                    auto["dias"] = dias_p_renta
                    auto["venta"] = (dias_p_renta*auto["precio_dia"])
                    auto["km"] = 0
                    h.guardar_inventario()
                    pres_ini = dias_p_renta * auto['precio_dia']
                    print(f"\n{COLOR_EXITO}¡Éxito! Ha rentado el {auto['marca']} {auto['modelo']}.{COLOR_RESET}")
                    print(f"\n{COLOR_EXITO}Presupuesto estimado: ${pres_ini:,.2f}{COLOR_RESET}")
                    h.row_space()
                    return
                else:
                    h.limpiar_pantalla()
                    print(f"\n{COLOR_ERROR}Lo sentimos, este auto ya está rentado.{COLOR_RESET}")
                    h.row_space()
                    return
        h.limpiar_pantalla()
        print(f"\n{COLOR_ERROR}El ID introducido no existe.{COLOR_RESET}")
        h.row_space()
    except ValueError:
        print(f"\n{COLOR_ERROR}Por favor, introduzca un número válido.{COLOR_RESET}")
        h.row_space()
        
def regresar_auto():
    global inventario
    global control
    label = "¿Cuántos kilómetros recorrió?  .. "
    label2 = "Ingrese el ID del auto a regresar: ..  "
    
    h.limpiar_pantalla()
    # print(f"{COLOR_TITULO}=== REGRESAR AUTO RENTADO (NUEVA TRANSACCIÓN) ==={COLOR_RESET}\n")
    
    rentados = [auto for auto in inventario if not auto["disponible"]]
    if not rentados:
        print(f"{COLOR_ERROR}No hay autos rentados en este momento.{COLOR_RESET}")
        input("\nPresione Enter para continuar...")
        return

    mostrar_inv_no_disp()                             # Mostrar la lista usando tu enfoque estilizado
    
    try:
        id_regresar = int(input(f" \n {COLOR_EXITO}{label2:^{30}}{COLOR_RESET}"))
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
            dias = int(input(f"\n¿Cuántos días UTILIZO el {auto_encontrado['marca']} {auto_encontrado['modelo']}?  "))
            km_nuevos = int(input(f"\n  {CIAN_BRILLANTE}{label:^{30}}{COLOR_RESET}"))
            if dias <= 0 or km_nuevos < 0:
                print(f"{COLOR_ERROR}Valores inválidos. No se admiten números negativos o días en 0.{COLOR_RESET}")
                input("\nPresione Enter para continuar...")
                return
            
 
        except ValueError:
            d_dias = 0
            print(f"{COLOR_ERROR}Entrada inválida. Ingrese números enteros.{COLOR_RESET}")
            input("\nPresione Enter para continuar...")
            return

        # 3. Calcular costos
        if auto_encontrado["dias"] < dias:
                d_dias = dias
        else:
                d_dias = auto_encontrado["dias"]

        print (f"los dias iniciales son .. {auto_encontrado["dias"]}")
        print (f"los dias finales   son .. {dias}")
        print (f"por lo tanto el combro debe ser sobre .. {d_dias}" )
        print ("Mas un dolar por kilometro ...", km_nuevos)                
        costo_total = auto_encontrado["precio_dia"] * d_dias + km_nuevos
        print ("Presupuesto actualizado es: ...", costo_total)
        h.row_space()

        fecha_actual = datetime.now().strftime("%d/%m/%Y")

        # 4. Actualizar estado en INVENTARIO (Estado actual)
        auto_encontrado["disponible"] = True
        auto_encontrado["dias"] = d_dias
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
        h.guardar_inventario()
        h.guarda_control()

        print(f"\n{COLOR_EXITO}¡Auto regresado con éxito!{COLOR_RESET}")
        print(f"Ticket N°: {num_transaccion} | Total cobrado: {COLOR_EXITO}${costo_total:,.2f}{COLOR_RESET}")
        
    else:
        print(f"{COLOR_ERROR}El ID ingresado no corresponde a un vehículo rentado.{COLOR_RESET}")
        
    input("\nPresione Enter para continuar...")






def menu_principal():
    cargar_inventario()
    veces = 15
    
    # 1. Definimos las opciones en una lista
    opciones = [
        "1. Ver autos disponibles",
        "2. Rentar un auto",
        "3. Entregar un auto",
        "4. Salir"
    ]
    seleccionada = 0  # El índice de la opción que inicia resaltada (la primera)

    while True:
        h.limpiar_pantalla()
        h.dibu_enca("BIENVENIDO A MI CARRITO EN RENTA", 70, "=")
        print("\n")
        
        # 2. Dibujamos el menú dinámicamente
        for i, opcion_texto in enumerate(opciones):
            if i == seleccionada:
                # Si es la opción actual, le ponemos una flecha física y color (puedes usar tu código de COLOR_EXITO)
                print(f"{' ' * veces} -> \033[1;36m{opcion_texto}\033[0m") 
            else:
                # Si no está seleccionada, se imprime normal con los espacios
                print(f"{' ' * (veces + 4)}{opcion_texto}")
            print("\n") # Mantenemos tus espacios entre renglones

        print(f"\n {' ' * veces}Usa las flechas [↑/↓] y presiona [Enter]")

        # 3. CAPTURA DE TECLAS EN MILISEGUNDOS
        # msvcrt.getch() lee la tecla que presionó el usuario al instante
        tecla = msvcrt.getch()

        # En Windows, las flechas del teclado envían dos impulsos: un 0 o 224, y luego el código real
        if tecla in (b'\x00', b'\xe0'): 
            tecla_flecha = msvcrt.getch() # Leemos el segundo impulso para saber qué flecha fue
            
            if tecla_flecha == b'H':  # Código físico de la Flecha Arriba
                # Restamos 1, pero si estamos en la opción 0, saltamos a la última para que sea un menú infinito
                seleccionada = len(opciones) - 1 if seleccionada == 0 else seleccionada - 1
            
            elif tecla_flecha == b'P':  # Código físico de la Flecha Abajo
                # Sumamos 1, pero si pasamos la última, regresamos a la primera opción
                seleccionada = 0 if seleccionada == len(opciones) - 1 else seleccionada + 1

        # 4. EVALUACIÓN DE LA SELECCIÓN AL PRESIONAR ENTER
        elif tecla == b'\r':  # b'\r' es el código del Enter (Carriage Return)
            
            if seleccionada == 0:  # Opción 1
                h.limpiar_pantalla()
                mostrar_inventario()
                h.row_space()
            elif seleccionada == 1:  # Opción 2
                h.limpiar_pantalla()
                rentar_auto()
                h.row_space()
            elif seleccionada == 2:  # Opción 3
                h.limpiar_pantalla()
                regresar_auto()
                h.row_space()
            elif seleccionada == 3:  # Opción 4 (Salir)
                h.limpiar_pantalla()
                print(f"\n{COLOR_EXITO}¡Gracias por usar Mi Carrito en Renta! Hasta pronto.{COLOR_RESET}\n")
                h.row_space()
                break

        # 5. EL TRUCO PARA EL MENÚ DE ADMINISTRADOR OCULTO
        # Si el usuario presiona una tecla normal, podemos validar si es el inicio de tu CLAVE_ADMIN
        # (Para no complicarlo, si escribe en el teclado directamente, capturamos texto normal)
        elif tecla.decode('utf-8', errors='ignore') == "a": # Ejemplo si tu clave inicia con 'a'
            # Aquí podrías detonar tu menu_administrador()
            print(" libre para una opcion oculta")
            h.row_space()


if __name__ == "__main__":
    menu_principal()