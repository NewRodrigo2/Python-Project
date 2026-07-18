import json 
import customtkinter as ctk
import renta as rta
import os
from pathlib import Path
import herramientas  as h

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

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - Mi Carrito en Renta")
        self.geometry("450x550")
        self.resizable(False, False)
        self.crear_interfaz_login()

    def crear_interfaz_login(self):
        self.lbl_bienvenido = ctk.CTkLabel(
            self, text="INICIAR SESIÓN", font=ctk.CTkFont(size=24, weight="bold")
        )
        self.lbl_bienvenido.pack(pady=(40, 20))

        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.pack(pady=10, padx=30, fill="both", expand=True)

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
            self.frame_login, text="Nombre de Usuario o ID:", font=ctk.CTkFont(size=14, weight="bold")
        )
        self.lbl_usuario.pack(pady=(20, 5), padx=30, anchor="w")
        self.txt_usuario = ctk.CTkEntry(
            self.frame_login, width=320, placeholder_text="Ej. Jose o ID"
        )
        self.txt_usuario.pack(pady=5, padx=30)

        self.lbl_password = ctk.CTkLabel(
            self.frame_login, text="Contraseña:", font=ctk.CTkFont(size=14, weight="bold")
        )
        self.lbl_password.pack(pady=(20, 5), padx=30, anchor="w")
        self.txt_password = ctk.CTkEntry(
            self.frame_login, width=320, placeholder_text="••••••••", show="•"
        )
        self.txt_password.pack(pady=5, padx=30)

        self.btn_ingresar = ctk.CTkButton(
            self.frame_login, text="Ingresar al Sistema", width=200, height=40, 
            font=ctk.CTkFont(size=15, weight="bold"), command=self.procesar_login
        )
        self.btn_ingresar.pack(pady=(40, 20))

    def procesar_login(self):
        rol_seleccionado = self.cmb_rol.get()
        usuario = self.txt_usuario.get().strip()
        password = self.txt_password.get().strip()

        if usuario == "" or password == "":
            print("Error: Campos vacíos")
            return

        # Diccionario para mapear los roles de la interfaz con las áreas del JSON
        mapeo_roles = {
            "Mostrador": "mostrador",
            "Financieros": "financieros",
            "Mecánico": "mantenimiento", # "Mecánico" equivale a "mantenimiento" en tu JSON
            "Administrador": "administrador",
            "Supervisor": "supervisor"
        }
        
        area_esperada = mapeo_roles.get(rol_seleccionado)

        try:
            with open(PERSONAL, "r", encoding="utf-8") as archivo:
                usuarios_db = json.load(archivo)

            usuario_valido = False
            
            for user in usuarios_db:
                # Comprobación de datos usando las llaves exactas de tu archivo JSON
                match_usuario = (user.get("nombre") == usuario or user.get("id_emp") == usuario)
                match_password = (user.get("pasword") == password)
                match_area = (user.get("area") == area_esperada)

                print(f"DEBUG: verificando los datos del personal")
                print(user.get("id_emp"))
                print(user.get("nombre"))
                print(user.get("area"))
                print(user.get("pasword"))
                h.row_space()

                if match_usuario and match_password and match_area:
                    usuario_valido = True
                    break

            if usuario_valido:
                print(f"¡Acceso Concedido como {rol_seleccionado}!")
                self.txt_usuario.delete(0, 'end')
                self.txt_password.delete(0, 'end')
                self.destroy()
                
                if rol_seleccionado == "Mostrador":
                    rta.menu_principal()
                else:
                    print(f"Abriendo menú para {rol_seleccionado} (Requiere implementar en rta)...")
            else:
                print("Error: Usuario, contraseña o rol incorrectos.")

        except FileNotFoundError:
            print(f"Error crítico: El archivo no existe en la ruta {PERSONAL}")
        except json.JSONDecodeError:
            print("Error crítico: El archivo 'personal.json' tiene un formato inválido.")

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
