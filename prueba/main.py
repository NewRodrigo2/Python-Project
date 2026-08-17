''' se agrego boton salir y def salir_definitivo(self): '''
import json 
import customtkinter as ctk
import renta as rta
import os
from pathlib import Path
import herramientas  as h
import admin as admin
from menu_admin import DashboardApp as ma
from menu_gral import LoginApp as mg  # O el menú general correspondiente

# ...................... Estableciendo la ruta de los archivos .json  ..........
ruta_actual = os.getcwd() 
unidad = os.path.splitdrive(ruta_actual)[0] 
if unidad == "C:":
    CARPETA_DATOS = Path(unidad + "\\") / "Users" / "danie" / "Documents" / "Python Project" / "prueba" / "datos"
else:
    CARPETA_DATOS = Path(unidad + "\\") / "Python" / "Python Project" / "prueba" / "datos"

ARCHIVO_DATOS = CARPETA_DATOS / "inventario.json"
ARCHIVO_CONTROL = CARPETA_DATOS / "control.json"
ARCHIVO_TEX = CARPETA_DATOS / "autos_ordenados.txt"
PERSONAL = CARPETA_DATOS / "personal.json"  
# ...........................................................................

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class VentanaLogin(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - Mi Carrito en Renta")
        self.geometry("450x650")
        self.resizable(False, False)
        self.crear_interfaz_login()

    def crear_interfaz_login(self):
        self.lbl_bienvenido = ctk.CTkLabel(
            self, text="INICIAR SESIÓN", font=ctk.CTkFont(size=24, weight="bold")
        )
        self.lbl_bienvenido.pack(pady=(40, 20))
#................................................................................
        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.pack(pady=10, padx=30, fill="both", expand=True)
#................................................................................

        self.lbl_rol = ctk.CTkLabel(
            self.frame_login, text="Seleccione su Tipo de Personal:", font=ctk.CTkFont(size=14, weight="bold")
        )
        self.lbl_rol.pack(pady=(25, 5), padx=30, anchor="w")
        
        # Roles de la interfaz gráfica
        self.roles_disponibles = ["Mostrador", "Financieros", "Mecánico", "Administrador", "Supervisor"]

        self.cmb_rol = ctk.CTkComboBox(
        self.frame_login, values=self.roles_disponibles, width=320, state="readonly"
        )

        self.cmb_rol.set("Mostrador")
        self.cmb_rol.pack(pady=5, padx=30)

        self.lbl_usuario = ctk.CTkLabel(
            self.frame_login, text="Nombre de Usuario o ID:", font=ctk.CTkFont(size=14, weight="bold"))

        self.lbl_usuario.pack(pady=(20, 5), padx=30, anchor="w")

        self.txt_usuario = ctk.CTkEntry(
            self.frame_login, width=320, placeholder_text="Ej. Jose o ID")
        self.txt_usuario.pack(pady=5, padx=30)

        self.lbl_password = ctk.CTkLabel(
            self.frame_login, text="Contraseña:", font=ctk.CTkFont(size=14, weight="bold"))
        
        self.lbl_password.pack(pady=(20, 5), padx=30, anchor="w")

        self.txt_password = ctk.CTkEntry(
        self.frame_login, width=320, placeholder_text="••••••••", show="•")

        self.txt_password.pack(pady=5, padx=30)

        self.btn_ingresar = ctk.CTkButton(
            self.frame_login, text="Ingresar al Sistema", width=200, height=40, 
            font=ctk.CTkFont(size=15, weight="bold"), command=self.procesar_login
        )
        self.btn_ingresar.pack(pady=(40, 20))
#................................................
        self.btn_salir = ctk.CTkButton(
            self.frame_login, text="Cerrar el Sistema", width=200, height=40, 
            font=ctk.CTkFont(size=15, weight="bold"), 
            command=self.salir_definitivo
        )
        self.btn_salir.pack(pady=(20, 20))
#.....
        self.etiqueta_mensaje = ctk.CTkLabel(
            self, text="Esperando acción...", font=("Arial", 14), text_color="gray"
        )
        self.etiqueta_mensaje.pack(pady=20)

    def procesar_login(self):
        rol_seleccionado = self.cmb_rol.get()
        # Aseguramos que el input de usuario sea procesado en minúsculas para la validación
        usuario = self.txt_usuario.get().strip().lower()
        password = self.txt_password.get().strip()

        if usuario == "" or password == "":
            self.etiqueta_mensaje.configure(
                text="Error: Complete los campos vacíos.", text_color="orange"
            )
            return

        # Diccionario para mapear los roles de la interfaz con las áreas del JSON en minúsculas
        mapeo_roles = {
            "Mostrador": "mostrador",
            "Financieros": "financieros",
            "Mecánico": "mantenimiento", 
            "Administrador": "administrador",
            "Supervisor": "supervisor"
        }
        
        area_esperada = mapeo_roles.get(rol_seleccionado)

        try:
            with open(PERSONAL, "r", encoding="utf-8") as archivo:
                usuarios_db = json.load(archivo)

            usuario_valido = False
            
            for user in usuarios_db:
                # Comprobación estandarizada aplicando .lower() a los datos leídos del JSON
                db_nombre = str(user.get("nombre", "")).strip().lower()
                db_id = str(user.get("id_emp", "")).strip().lower()
                db_password = str(user.get("pasword", "")).strip()
                db_area = str(user.get("area", "")).strip().lower()

                match_usuario = (db_nombre == usuario or db_id == usuario)
                match_password = (db_password == password)
                match_area = (db_area == area_esperada)

                if  match_password and match_area:
                    usuario_valido = True
                    break                 # Rompe el ciclo for si encuentra coincidencia

            if usuario_valido:
                self.etiqueta_mensaje.configure(
                    text="¡Login exitoso! Abriendo sistema...", text_color="green"
                )
                self.txt_usuario.delete(0, 'end')
                self.txt_password.delete(0, 'end')
                
                # 1. Destruimos inmediatamente la ventana de login
                self.withdraw()
                nueva_ventana = mg(rol_usuario=rol_seleccionado, ventana_login=self)
                nueva_ventana.mainloop()

            else:
                self.etiqueta_mensaje.configure(
                    text="Error: Usuario, contraseña o rol incorrectos.", text_color="red")

        except FileNotFoundError:
            self.etiqueta_mensaje.configure(
                 text="Error crítico: El archivo no existe en la ruta", text_color="red")            
        except json.JSONDecodeError:
            self.etiqueta_mensaje.configure(
                 text="Error crítico: El archivo 'personal.json' tiene un formato inválido.", text_color="red"
            )

    def salir_definitivo(self):
        ''' Termina el mainloop y destruye la ventana tras la animación del click.'''
        # Esperamos 100ms para evitar el error de animación en segundo plano
        self.after(100, self.destroy)

                        

if __name__ == "__main__":
    app = VentanaLogin()
    app.mainloop()