import json 
import customtkinter as ctk
import renta as rta
import os
from pathlib import Path
import herramientas  as h
import admin as admin

ruta_actual = os.getcwd() 
unidad = os.path.splitdrive(ruta_actual)[0] 
if unidad == "C:":
    CARPETA_DATOS = Path(unidad + "\\") / "Users" / "danie" / "Documents" / "Python Project" / "prueba" / "datos"
else:
    CARPETA_DATOS = Path(unidad + "\\") / "Python" / "Python Project" / "prueba" / "datos"

# 3. CONSEJO: Usa Path también para el archivo, es más limpio y evita mezclar os y pathlib
RCHIVO_DATOS = CARPETA_DATOS / "inventario.json"
ARCHIVO_CONTROL = CARPETA_DATOS / "control.json"
ARCHIVO_TEX = CARPETA_DATOS / "autos_ordenados.txt"
PERSONAL = CARPETA_DATOS / "personal.json"  # <-- Esta es la línea clave


class DashboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 2. Configuración de la Ventana de Login
        self.title("Administracion")
        self.geometry("800x800")
        self.resizable(False, False)

        # 3. Creación de los Componentes (Widgets)
        self.crear_interfaz_login()

    def crear_interfaz_login(self):
        # --- TÍTULO PRINCIPAL ---
        self.lbl_bienvenido = ctk.CTkLabel(
            self, 
            text="ADMINISTRACION", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.lbl_bienvenido.pack(pady=(40, 20))

        # --- CONTENEDOR CENTRAL (FRAME) ---
        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.pack(pady=10, padx=30, fill="both", expand=True)

        self.btn_agregar = ctk.CTkButton(
            self.frame_login,  
            text=" Agregar nuevo auto al inventario", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.procesar_login
        )
        self.btn_agregar.pack(pady=(40, 20))

        self.btn_ver = ctk.CTkButton(
            self.frame_login,  
            text=" Ver listado de rentas realizadas", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.procesar_login
        )
        self.btn_ver.pack(pady=(40, 20))

        self.btn_eliminar = ctk.CTkButton(
            self.frame_login,  
            text=" Eliminar un tikect del control", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.procesar_login
        )
        self.btn_eliminar.pack(pady=(40, 20))

        self.btn_informe = ctk.CTkButton(
            self.frame_login,  
            text=" Informe de  Rentasl", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.procesar_login
        )
        self.btn_informe.pack(pady=(40, 20))

        self.btn_salir = ctk.CTkButton(
            self.frame_login,  
            text=" Salir del sistema", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self.cerrar_sesion
        )
        self.btn_salir.pack(pady=(40, 20))

    def cerrar_sesion(self):
        self.destroy()  # Destruye el Dashboard
        
        # IMPORTANTE: Para evitar errores de importación circular, 
        # puedes importar el Login aquí dentro de la función (import local)
        from main import LoginApp 
        
        # Crea una nueva instancia del Login
        ventana_login = LoginApp()
        ventana_login.mainloop()



#--------------------------------------------------------------------------
        # # --- SELECCIÓN DE ROL / PUESTO ---
        # self.lbl_rol = ctk.CTkLabel(
        #     self.frame_login,  
        #     text="Seleccione una opcion:",
        #     font=ctk.CTkFont(size=14, weight="bold")
        # )
        # self.lbl_rol.pack(pady=(25, 5), padx=30, anchor="w")

        # self.roles_disponibles = ["Administrador","Financieros", "Financieros", "Supervisor"]
        # self.cmb_rol = ctk.CTkComboBox(
        #     self.frame_login,  # <-- DEBE DECIR self.frame_login
        #     values=self.roles_disponibles,
        #     width=320,
        #     state="readonly"
        # )
        # self.cmb_rol.set("Administrador")
        # self.cmb_rol.pack(pady=5, padx=30)

        # # --- CAMPO: USUARIO ---
        # self.lbl_usuario = ctk.CTkLabel(
        #     self.frame_login,  
        #     text="Nombre de Usuario o ID:",
        #     font=ctk.CTkFont(size=14, weight="bold")
        # )
        # self.lbl_usuario.pack(pady=(20, 5), padx=30, anchor="w")

        # self.txt_usuario = ctk.CTkEntry(
        #     self.frame_login, 
        #     width=320, 
        #     placeholder_text="Ej. juan.perez"
        # )
        # self.txt_usuario.pack(pady=5, padx=30)

        # # --- CAMPO: CONTRASEÑA ---
        # self.lbl_password = ctk.CTkLabel(
        #     self.frame_login,  
        #     text="Contraseña:",
        #     font=ctk.CTkFont(size=14, weight="bold")
        # )
        # self.lbl_password.pack(pady=(20, 5), padx=30, anchor="w")

        # self.txt_password = ctk.CTkEntry(
        #     self.frame_login,  
        #     width=320, 
        #     placeholder_text="••••••••", 
        #     show="•"
        # )
        # self.txt_password.pack(pady=5, padx=30)

        # # --- BOTÓN DE ENTRADA ---
        # self.btn_ingresar = ctk.CTkButton(
        #     self.frame_login,  
        #     text="Ingresar al Sistema", 
        #     width=200,
        #     height=40,
        #     font=ctk.CTkFont(size=15, weight="bold"),
        #     command=self.procesar_login
        # )
        # self.btn_ingresar.pack(pady=(40, 20))


    # 4. Lógica del Botón
    # def procesar_login(self):
    #     rol_seleccionado = self.cmb_rol.get()
    #     usuario = self.txt_usuario.get()
    #     password = self.txt_password.get()

    #     # [Validación Temporal en Consola]
    #     print(f"\n[INTENTO DE LOGIN]")
    #     print(f"Rol: {rol_seleccionado} | Usuario: {usuario} | Clave: {password}")

    #     # Aquí es donde en la siguiente clase llamaremos a tus otros scripts para validar
    #     # Ejemplo provisional de bienvenida:
    #     if usuario != "" and password != "":
    #         print(f"¡Acceso Concedido como {rol_seleccionado}!")
    #         # Limpiamos los campos
    #         self.txt_usuario.delete(0, 'end')
    #         self.txt_password.delete(0, 'end')
    #     else:
    #         print("Error: Campos vacíos")
    #     if rol_seleccionado ==  "Mostrador":
    #         menu_administrador()                         # cambiar por def



if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()