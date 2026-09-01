''' este script se llama main.py y es el login de mi proyecto
se agrego boton salir y def salir_definitivo(self): '''
import json 
import customtkinter as ctk
import renta as rta
import os
from pathlib import Path
import herramientas  as h
import admin as admin
from menu_admin import DashboardApp as ma
from menu_gral import LoginApp as mg       # O el menú general correspondiente
from logic import AuthManager, RoleManager


# ...................... Estableciendo la ruta de los archivos .json  ..........
# Carpeta donde está main.py

ruta_actual = Path(__file__).parent
CARPETA_DATOS = ruta_actual / "datos"

ARCHIVO_DATOS = CARPETA_DATOS / "inventario.json"
ARCHIVO_CONTROL = CARPETA_DATOS / "control.json"
ARCHIVO_TEX = CARPETA_DATOS / "autos_ordenados.txt"
PERSONAL = CARPETA_DATOS / "personal.json"

# Debug prints para confirmar rutas
ruta_actual = Path(__file__).parent
CARPETA_DATOS = ruta_actual / "datos"

ARCHIVO_DATOS = CARPETA_DATOS / "inventario.json"
ARCHIVO_CONTROL = CARPETA_DATOS / "control.json"
ARCHIVO_TEX = CARPETA_DATOS / "autos_ordenados.txt"
PERSONAL = CARPETA_DATOS / "personal.json"

# Debug prints para confirmar rutas
# Color morado para debug
PURPLE = "\033[95m"
V_B = "\033[92m"
RESET = "\033[0m"

# Debug prints con color
print(f"{PURPLE}[DEBUG] main.py {ruta_actual}{RESET}")
print(f"{PURPLE}[DEBUG] Ruta actual: {V_B}{ruta_actual}{RESET}")
print(f"{PURPLE}[DEBUG] Carpeta de datos:{V_B} {CARPETA_DATOS}{RESET}")
print(f"{PURPLE}[DEBUG] Archivo inventario.json:{V_B} {ARCHIVO_DATOS}{RESET}")
print(f"{PURPLE}[DEBUG] Archivo control.json:{V_B} {ARCHIVO_CONTROL}{RESET}")
print(f"{PURPLE}[DEBUG] Archivo autos_ordenados.txt:{V_B} {ARCHIVO_TEX}{RESET}")
print(f"{PURPLE}[DEBUG] Archivo personal.json:{V_B} {PERSONAL}{RESET}")
 
# ...........................................................................

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# auth = AuthManager(PERSONAL)   # instancia global

from logic import AuthManager, RoleManager

class VentanaLogin(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - Mi Carrito en Renta")
        self.geometry("450x650")
        self.resizable(False, False)

        self.auth = AuthManager(PERSONAL)
        self.role_manager = RoleManager()   # instancia de RoleManager

        self.crear_interfaz_login()

    def crear_interfaz_login(self):
        # Etiqueta de bienvenida
        self.lbl_bienvenido = ctk.CTkLabel(
            self, text="INICIAR SESIÓN", font=ctk.CTkFont(size=24, weight="bold")
        )
        self.lbl_bienvenido.pack(pady=(40, 20))

        # Frame principal del login
        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.pack(pady=10, padx=30, fill="both", expand=True)

        # Etiqueta de rol
        self.lbl_rol = ctk.CTkLabel(
            self.frame_login, text="Seleccione su Tipo de Personal:", font=ctk.CTkFont(size=14, weight="bold")
        )
        self.lbl_rol.pack(pady=(25, 5), padx=30, anchor="w")

# Roles desde RoleManager
# ComboBox de roles

        roles_disponibles = self.role_manager.obtener_roles()
        self.cmb_rol = ctk.CTkComboBox(
            self.frame_login, values=roles_disponibles, width=320, state="readonly"
        )
        self.cmb_rol.set(roles_disponibles[0])  # primer rol como default
        self.cmb_rol.pack(pady=5, padx=30)

# Etiqueta usuario
        self.lbl_usuario = ctk.CTkLabel(
            self.frame_login, text="Nombre de Usuario o ID:", font=ctk.CTkFont(size=14, weight="bold")
        )
        self.lbl_usuario.pack(pady=(20, 5), padx=30, anchor="w")

# Campo usuario
        self.txt_usuario = ctk.CTkEntry(
            self.frame_login, width=320, placeholder_text="Ej. Jose o ID"
        )
        self.txt_usuario.pack(pady=5, padx=30)

# Etiqueta contraseña
        self.lbl_password = ctk.CTkLabel(
            self.frame_login, text="Contraseña:", font=ctk.CTkFont(size=14, weight="bold")
        )
        self.lbl_password.pack(pady=(20, 5), padx=30, anchor="w")

# Campo contraseña
        self.txt_password = ctk.CTkEntry(
            self.frame_login, width=320, placeholder_text="••••••••", show="•"
        )
        self.txt_password.pack(pady=5, padx=30)

        # Botón ingresar
        self.btn_ingresar = ctk.CTkButton(
            self.frame_login, text="Ingresar al Sistema", width=200, height=40,
            font=ctk.CTkFont(size=15, weight="bold"), command=self.procesar_login
        )
        self.btn_ingresar.pack(pady=(40, 20))

        # Botón salir
        self.btn_salir = ctk.CTkButton(
            self.frame_login, text="Cerrar el Sistema", width=200, height=40,
            font=ctk.CTkFont(size=15, weight="bold"), command=self.salir_definitivo
        )
        self.btn_salir.pack(pady=(20, 20))

        # Etiqueta de mensajes
        self.etiqueta_mensaje = ctk.CTkLabel(
            self, text="Esperando acción...", font=("Arial", 14), text_color="gray"
        )
        self.etiqueta_mensaje.pack(pady=20)


    def procesar_login(self):
        usuario = self.txt_usuario.get().strip().lower()
        password = self.txt_password.get().strip()
        rol_seleccionado = self.cmb_rol.get()

        # Usamos el método de AuthManager
        usuario_valido = self.auth.validar_usuario(usuario, password, rol_seleccionado)

        if usuario_valido:
            self.etiqueta_mensaje.configure(text="¡Login exitoso! Abriendo sistema...", text_color="green")
            self.withdraw()
            nueva_ventana = mg(rol_usuario=rol_seleccionado, ventana_login=self)
            nueva_ventana.mainloop()
        else:
            self.etiqueta_mensaje.configure(text="Error: Usuario, contraseña o rol incorrectos.", text_color="red")

    def salir_definitivo(self):
        ''' Termina el mainloop y destruye la ventana tras la animación del click.'''
        # Esperamos 100ms para evitar el error de animación en segundo plano
        self.after(100, self.destroy)

                        

if __name__ == "__main__":
    app = VentanaLogin()
    app.mainloop()