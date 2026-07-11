# MODIFICADO EL 10/07/26  11:19
# C:\Users\danie\Documents\Python Project> git switch secund_pba_branch.py
import os
import json
import msvcrt  # Librería nativa de Windows para capturar teclas al instante

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
            guardar_inventario()

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
            guarda_control()
            h.row_space()

    except Exception as e:
        # Respaldo de emergencia en caso de fallo catastrófico de lectura/escritura
        inventario = INVENTARIO_DEFECTO
        control = AUTO_CONTROL
        print(f"\n{COLOR_ERROR}Error crítico al cargar archivos ({e}). Usando datos temporales.{COLOR_RESET}")
        h.row_space()

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

def mostrar_inventario():
    h.dibu_enca("INVENTARIO DE AUTOS", 70, "═")                                          #  dibujando enca
    print(f"{'ID':<4} | {'Marca':<12} | {'Modelo':<12} | {'Precio/Día':<12} | Estado")
    print("-" * 69)

    for auto in inventario:
       estado = f"{COLOR_EXITO}Disponible{COLOR_RESET}" if auto["disponible"] else f"{COLOR_ERROR}Rentado{COLOR_RESET}"
       # print(f"[{auto['id']}] {auto['marca']} {auto['modelo']} - ${auto['precio_dia']}/día ({estado}) rentado por {COLOR_ADMIN}{auto['dias']} dias{COLOR_RESET}")
       print(f"[{auto['id']:<2}] | {auto['marca']:<12} | {auto['modelo']:<12} | ${auto['precio_dia']:<11} | {COLOR_ERROR}{estado}{COLOR_RESET}")

def mostrar_informe():
    h.limpiar_pantalla()
    # Control de codigo, plan: conocer el tamano del archivo .......................
    tamano = int(len(control) / 10)
    tamano += 1
    cont_lineas = 0
    a = 1
    space = '    ' 
    def sub_enca():
        print(f"{space}{'Tikect':<7}|{'ID ':<3} | {'Marca':<12} | {'Modelo':<12} | {'Km recorridos':<12} | {'Venta':<6} |"
            f"{'Fecha de renta':<14} | {'Dias':<4}"
        )
        print("-" * 95)

    for auto in control:
        if cont_lineas == 0:
            h.limpiar_pantalla()
            h.dibu_enca("INFORME  DE AUTOS RENTADOS", 95, "═")                       #  dibujando enca
            sub_enca()

        print(
        f"{space}{auto['transaccion_id']:^7}|{auto['c_id']:<3} | {auto['c_marca']:<12} | {auto['c_modelo']:<12} | "
        f"{auto['km_recorridos']:^12} | {auto['c_venta_total']:<6} | {auto['c_fecha_renta']:^14} | "
        f"{auto['c_dias']:<4}")                                       
                
        cont_lineas += 1
        if cont_lineas == 10:
            # sub_enca()
            print (f"{COLOR_EXITO}Pagina {a} de {tamano} {COLOR_RESET}")
            h.row_space()
            # h.limpiar_pantalla()
            cont_lineas = 0
            a += 1

    h.row_space()
    h.limpiar_pantalla()

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
                    guardar_inventario()
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
        guardar_inventario()
        guarda_control()

        print(f"\n{COLOR_EXITO}¡Auto regresado con éxito!{COLOR_RESET}")
        print(f"Ticket N°: {num_transaccion} | Total cobrado: {COLOR_EXITO}${costo_total:,.2f}{COLOR_RESET}")
        
    else:
        print(f"{COLOR_ERROR}El ID ingresado no corresponde a un vehículo rentado.{COLOR_RESET}")
        
    input("\nPresione Enter para continuar...")

def agrega_auto():
            h.limpiar_pantalla()
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
                    h.row_space()
                    # continue
                
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
                h.row_space()
                
            except ValueError:
                print(f"\n{COLOR_ERROR}Error: El precio debe ser un número válido.{COLOR_RESET}")
                h.row_space()

def eliminar_renta_admin():
    global control
    h.limpiar_pantalla()
    print(f"{COLOR_ERROR}=== ELIMINAR REGISTRO DE CONTROL (ACCIÓN CRÍTICA) ==={COLOR_RESET}\n")
    
    if not control:
        print(f"{COLOR_ERROR}No hay registros para eliminar.{COLOR_RESET}")
        input("\nPresione Enter para continuar...")
        return

    try:
        id_ticket = int(input("Ingrese el N° de Ticket que desea BORRAR permanentemente: "))
    except ValueError:
        print(f"{COLOR_ERROR}Entrada inválida.{COLOR_RESET}")
        input("\nPresione Enter para continuar...")
        return

    ticket_encontrado = None
    for renta in control:
        if renta["transaccion_id"] == id_ticket:
            ticket_encontrado = renta
            break

    if ticket_encontrado:
        print(f"\n{COLOR_ERROR}¿Está seguro de eliminar la renta del {ticket_encontrado['c_marca']} por ${ticket_encontrado['c_venta_total']}?{COLOR_RESET}")
        confirmar = input("Escriba 'SI' para confirmar el borrado: ").strip().upper()
        
        if confirmar == "SI" or confirmar == "SÍ":
            # Eliminar de la lista de Python
            control.remove(ticket_encontrado)
            # Guardar la lista limpia en el archivo .json
            guarda_control()
            print(f"\n{COLOR_EXITO}✓ Registro eliminado correctamente del archivo JSON.{COLOR_RESET}")
        else:
            print("\nOperación cancelada por el usuario.")
    else:
        print(f"{COLOR_ERROR}El ticket N° {id_ticket} no existe.{COLOR_RESET}")
        
    input("\nPresione Enter para continuar...")

def informe_rentas():
    cargar_inventario()    
    from collections import defaultdict

    # 1. Agrupamos los datos (como en el paso anterior)
    autos_por_id = defaultdict(list)
    for registro in control:
        id_actual = registro.get("c_id")
        if id_actual is not None:  # Evita errores si algún registro no tiene id
            autos_por_id[id_actual].append(registro)

    # 2. Abrimos el archivo de texto para escribir ('w' significa write)
    with open(ARCHIVO_TEX, "w", encoding="utf-8") as archivo:
        
        # 3. Usamos sorted() para recorrer los IDs en orden: 1, 2, 3...
        for c_id in sorted(autos_por_id.keys()):
            primer_auto = autos_por_id[c_id][0]
            marca = primer_auto.get("c_marca", "Desconocida")   
            modelo = primer_auto.get("c_modelo", "Desconocido" )                           
            archivo.write(f"=========================================================================\n")
            archivo.write(f" REGISTROS PARA ID: {c_id}     {marca}       {modelo} \n")
            archivo.write(f"==========================================================================\n")
            archivo.write(f" {'Tiket':^8} | {'Dias':^5} | {'Kilometrol':^10}  | {'Fecha':^11}  |  {'Venta'} \n")
            archivo.write(f"==========================================================================\n")
            
            # 4. Escribimos cada auto que pertenece a este ID
            tot_venta = tot_km = 0
            for auto in autos_por_id[c_id]:
                linea = (
                    f" {auto.get('transaccion_id'):^8} |"
                    f" {auto.get('c_dias'):^5} | "
                    f" {auto.get('km_recorridos'):^10,.1f} | "
                    f" {auto.get('c_fecha_renta'):<11} | "
                    f" $ {auto.get('c_venta_total'):<,.2f}\n"
                )
                archivo.write(linea)
                tot_venta += auto.get("c_venta_total", 0)
                tot_km += auto.get("km_recorridos", 0)
            archivo.write("\n")  # Espacio en blanco entre grupos de IDs
            archivo.write(f" Kilometro recorridos: {tot_km:,.2f}   Venta total: $ {tot_venta:,.2f}")
            archivo.write("\n")  # Espacio en blanco entre grupos de IDs
            archivo.write("\n")  # Espacio en blanco entre grupos de IDs

    input ("¡Archivo 'autos_ordenados.txt' creado con éxito!    .... enter para continuar")
 
def menu_administrador():
    """Submenú protegido para agregar vehículos nuevos."""
    label1 = ("1. Agregar nuevo auto al inventario \n")
    label2 = ("2. Ver listado de rentas realizadas \n")
    label3 = ("3. Eliminar un tikect del control   \n")
    label4 = ("4. Informe de  Rentas               \n")
    label5 = ("5. Utilerias                        \n")
    label9 = ("9. Volver al menú principal         \n")
    while True:
        h.limpiar_pantalla()
        h.dibu_enca("PANEL DE ADMINISTRACIÓN", 80, "=")
        print(f"{AMARILLO}{label1:^{80}}")
        print(f"{AMARILLO}{label2:^{80}}")
        print(f"{AMARILLO}{label3:^{80}}")
        print(f"{AMARILLO}{label4:^{80}}")
        print(f"{AMARILLO}{label5:^{80}}")
        print(f"{AMARILLO}{label9:^{80}}{COLOR_RESET}")
        opcion = input(f"\n{COLOR_EXITO}                    Seleccione una opción (1-2):    {COLOR_RESET}")
          
        if opcion == "1":
            agrega_auto()
        elif opcion == "2":
            mostrar_informe()
        elif opcion == "3":
             eliminar_renta_admin()
        elif opcion == "4":
             informe_rentas()
        elif opcion == "5":
             None
        elif opcion == "9"  or opcion == "":    # ----------------  9 
            break
        else:
            print(f"\n{COLOR_ERROR}Opción no válida.{COLOR_RESET}")
            h.row_space()


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
            elif seleccionada == 2:  # Opción 3
                h.limpiar_pantalla()
                regresar_auto()
            elif seleccionada == 3:  # Opción 4 (Salir)
                h.limpiar_pantalla()
                print(f"\n{COLOR_EXITO}¡Gracias por usar Mi Carrito en Renta! Hasta pronto.{COLOR_RESET}\n")
                break

        # 5. EL TRUCO PARA EL MENÚ DE ADMINISTRADOR OCULTO
        # Si el usuario presiona una tecla normal, podemos validar si es el inicio de tu CLAVE_ADMIN
        # (Para no complicarlo, si escribe en el teclado directamente, capturamos texto normal)
        elif tecla.decode('utf-8', errors='ignore') == "a": # Ejemplo si tu clave inicia con 'a'
            # Aquí podrías detonar tu menu_administrador()
            menu_administrador()


if __name__ == "__main__":
    menu_principal()