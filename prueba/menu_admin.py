import json
import os
from pathlib import Path
import customtkinter as ctk
import renta as rta
import herramientas as h
import admin as admin

# ------------------------------------------------------------------------------------------
ruta_actual = os.getcwd() 
unidad = os.path.splitdrive(ruta_actual)[0] 
if unidad == "C:":
    CARPETA_DATOS = Path(unidad + "\\") / "Users" / "danie" / "Documents" / "Python Project" / "prueba" / "datos"
else:
    CARPETA_DATOS = Path(unidad + "\\") / "Python" / "Python Project" / "prueba" / "datos"

# Rutas de archivos corregidas
ARCHIVO_DATOS = CARPETA_DATOS / "inventario.json"
ARCHIVO_CONTROL = CARPETA_DATOS / "control.json"
ARCHIVO_TEX = CARPETA_DATOS / "autos_ordenados.txt"
PERSONAL = CARPETA_DATOS / "personal.json"  
# ------------------------------------------------------------------------------------------

class DashboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Configuración de la Ventana del Dashboard de Administración
        self.title("Administración")
        self.geometry("800x800")
        self.resizable(False, False)
        self.crear_interfaz_login()

    def crear_interfaz_login(self):
        # --- TÍTULO PRINCIPAL ---
        self.lbl_bienvenido = ctk.CTkLabel(
            self, 
            text="ADMINISTRACIÓN", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.lbl_bienvenido.pack(pady=(40, 20))
        
# ................--- CONTENEDOR CENTRAL (FRAME) ---.................
        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.pack(pady=10, padx=30, fill="both", expand=True)
# ................--- CONTENEDOR CENTRAL (FRAME) ---.................

        # Botones del menú
        self.btn_rh = ctk.CTkButton(
            self.frame_login,  
            text="Recursos Humanos", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self.rec_hum
        )
        self.btn_rh.pack(pady=(40, 20))

        self.btn_agregar = ctk.CTkButton(
            self.frame_login,  
            text="Agregar nuevo auto al inventario", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.agregar_auto
        )
        self.btn_agregar.pack(pady=(40, 20))

        self.btn_ver = ctk.CTkButton(
            self.frame_login,  
            text="Ver listado de rentas realizadas", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.ver_rentas
        )
        self.btn_ver.pack(pady=(40, 20))

        self.btn_eliminar = ctk.CTkButton(
            self.frame_login,  
            text="Eliminar un ticket del control", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.eliminar_ticket
        )
        self.btn_eliminar.pack(pady=(40, 20))

        self.btn_informe = ctk.CTkButton(
            self.frame_login,  
            text="Informe de Rentas", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.generar_informe
        )
        self.btn_informe.pack(pady=(40, 20))

        self.btn_salir = ctk.CTkButton(
            self.frame_login,  
            text="Salir del sistema", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self.cerrar_sesion
        )
        self.btn_salir.pack(pady=(40, 20))

    def rec_hum(self):
        # 1. Ocultamos el frame principal del login
        self.frame_login.pack_forget()
        
        # 2. Si el segundo frame no ha sido creado, lo creamos
        if not hasattr(self, "frame_segundo"):
            self.frame_segundo = ctk.CTkFrame(self)

            # Botón para volver al primer frame
            self.btn_agrega_rh = ctk.CTkButton(
                self.frame_segundo,  
                text="Agrerar Nuevo PersonL", 
                # command=self.mostrar_menu_principal
            )
            self.btn_agrega_rh.pack(pady=(40, 20))

            self.btn_nomina = ctk.CTkButton(
                self.frame_segundo,  
                text="Realizar Nomina", 
                # command=self.mostrar_menu_principal
            )
            self.btn_nomina.pack(pady=(40, 20))            

            self.btn_volver = ctk.CTkButton(
                self.frame_segundo,  
                text="Volver", 
                command=self.mostrar_menu_principal
            )
            self.btn_volver.pack(pady=(40, 20))

        # 3. Mostramos el segundo frame en pantalla
        self.frame_segundo.pack(pady=10, padx=30, fill="both", expand=True)

    def mostrar_menu_principal(self):
        self.frame_segundo.pack_forget() # Ocultamos el segundo
        self.frame_login.pack(pady=10, padx=30, fill="both", expand=True) # Volvemos a mostrar el primero

    def cerrar_sesion(self):
        self.destroy()                     # Destruye el Dashboard
        
        # Importación local para evitar errores circulares
        from main import LoginApp 
        
        # Crea una nueva instancia del Login
        ventana_login = LoginApp()
        ventana_login.mainloop()

if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()