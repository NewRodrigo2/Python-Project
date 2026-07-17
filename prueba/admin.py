'''
13/07/26 13:45

'''
import customtkinter as ctk
import renta as rta
import herramientas as h
import os
import json

# 1. Configuración estética de CustomTkinter
ctk.set_appearance_mode("Dark")  # Forzamos un modo oscuro muy elegante
ctk.set_default_color_theme("blue") 

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
            h.guarda_control()
            print(f"\n{COLOR_EXITO}✓ Registro eliminado correctamente del archivo JSON.{COLOR_RESET}")
        else:
            print("\nOperación cancelada por el usuario.")
    else:
        print(f"{COLOR_ERROR}El ticket N° {id_ticket} no existe.{COLOR_RESET}")
        
    input("\nPresione Enter para continuar...")

def informe_rentas():
    h.cargar_inventario()    
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
                h.guardar_inventario()
                
                print(f"\n{COLOR_EXITO}¡Vehículo registrado con éxito! Asignado ID: [{nuevo_id}]{COLOR_RESET}")
                h.row_space()
                
            except ValueError:
                print(f"\n{COLOR_ERROR}Error: El precio debe ser un número válido.{COLOR_RESET}")
                h.row_space()

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
        opcion = input(f"\n{COLOR_EXITO}             Seleccione una opción  o enter para salir   {COLOR_RESET}")
          
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

# class LoginApp(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         # 2. Configuración de la Ventana de Login
#         self.title("Administracion")
#         self.geometry("450x550")
#         self.resizable(False, False)

#         # 3. Creación de los Componentes (Widgets)
#         self.crear_interfaz_login()

#     def crear_interfaz_login(self):
#         # --- TÍTULO PRINCIPAL ---
#         self.lbl_bienvenido = ctk.CTkLabel(
#             self, 
#             text="ADMINISTRACION", 
#             font=ctk.CTkFont(size=24, weight="bold")
#         )
#         self.lbl_bienvenido.pack(pady=(40, 20))

#         # --- CONTENEDOR CENTRAL (FRAME) ---
#         self.frame_login = ctk.CTkFrame(self)
#         self.frame_login.pack(pady=10, padx=30, fill="both", expand=True)

#         # --- SELECCIÓN DE ROL / PUESTO ---
#         self.lbl_rol = ctk.CTkLabel(
#             self.frame_login,  # <-- DEBE DECIR self.frame_login
#             text="Seleccione una opcion:",
#             font=ctk.CTkFont(size=14, weight="bold")
#         )
#         self.lbl_rol.pack(pady=(25, 5), padx=30, anchor="w")

#         self.roles_disponibles = ["Administrador","Financieros", "Financieros", "Supervisor"]
#         self.cmb_rol = ctk.CTkComboBox(
#             self.frame_login,  # <-- DEBE DECIR self.frame_login
#             values=self.roles_disponibles,
#             width=320,
#             state="readonly"
#         )
#         self.cmb_rol.set("Administrador")
#         self.cmb_rol.pack(pady=5, padx=30)

#         # --- CAMPO: USUARIO ---
#         self.lbl_usuario = ctk.CTkLabel(
#             self.frame_login,  
#             text="Nombre de Usuario o ID:",
#             font=ctk.CTkFont(size=14, weight="bold")
#         )
#         self.lbl_usuario.pack(pady=(20, 5), padx=30, anchor="w")

#         self.txt_usuario = ctk.CTkEntry(
#             self.frame_login, 
#             width=320, 
#             placeholder_text="Ej. juan.perez"
#         )
#         self.txt_usuario.pack(pady=5, padx=30)

#         # --- CAMPO: CONTRASEÑA ---
#         self.lbl_password = ctk.CTkLabel(
#             self.frame_login,  
#             text="Contraseña:",
#             font=ctk.CTkFont(size=14, weight="bold")
#         )
#         self.lbl_password.pack(pady=(20, 5), padx=30, anchor="w")

#         self.txt_password = ctk.CTkEntry(
#             self.frame_login,  
#             width=320, 
#             placeholder_text="••••••••", 
#             show="•"
#         )
#         self.txt_password.pack(pady=5, padx=30)

#         # --- BOTÓN DE ENTRADA ---
#         self.btn_ingresar = ctk.CTkButton(
#             self.frame_login,  # <-- DEBE DECIR self.frame_login
#             text="Ingresar al Sistema", 
#             width=200,
#             height=40,
#             font=ctk.CTkFont(size=15, weight="bold"),
#             command=self.procesar_login
#         )
#         self.btn_ingresar.pack(pady=(40, 20))


#     # 4. Lógica del Botón
#     def procesar_login(self):
#         rol_seleccionado = self.cmb_rol.get()
#         usuario = self.txt_usuario.get()
#         password = self.txt_password.get()

#         # [Validación Temporal en Consola]
#         print(f"\n[INTENTO DE LOGIN]")
#         print(f"Rol: {rol_seleccionado} | Usuario: {usuario} | Clave: {password}")

#         # Aquí es donde en la siguiente clase llamaremos a tus otros scripts para validar
#         # Ejemplo provisional de bienvenida:
#         if usuario != "" and password != "":
#             print(f"¡Acceso Concedido como {rol_seleccionado}!")
#             # Limpiamos los campos
#             self.txt_usuario.delete(0, 'end')
#             self.txt_password.delete(0, 'end')
#         else:
#             print("Error: Campos vacíos")
#         if rol_seleccionado ==  "Mostrador":
#             menu_administrador()                         # cambiar por def



if __name__ == "__main__":
    # app = LoginApp()
    # app.mainloop()
    menu_administrador()

