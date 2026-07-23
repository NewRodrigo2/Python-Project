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
    def __init__(self, ventana_menu_gral=None): # <--- Cambiado aquí
        super().__init__()
        self.ventana_menu_gral = ventana_menu_gral # Guardamos la referencia
        self.title("Administración")
        self.geometry("800x800")
        self.resizable(False, False)
        self.crear_interfaz_login()

    def crear_interfaz_login(self):
        # --- TÍTULO PRINCIPAL ---
        self.lbl_bienvenido = ctk.CTkLabel(
            self, text="ADMINISTRACIÓN", font=ctk.CTkFont(size=24, weight="bold")
        )
        self.lbl_bienvenido.pack(pady=(40, 20))

        # ................--- CONTENEDOR CENTRAL (FRAME) ---.................
        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.pack(pady=10, padx=30, fill="both", expand=True)

        # Botones del menú
        self.btn_rh = ctk.CTkButton(
            self.frame_login, text="Recursos Humanos", width=300, height=40, font=ctk.CTkFont(size=15, weight="bold"),
            command=self.rec_hum
        )
        self.btn_rh.pack(pady=(40, 20))

        self.btn_agregar = ctk.CTkButton(
            self.frame_login, text="Agregar nuevo auto al inventario", width=300, height=40, font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.agregar_auto
        )
        self.btn_agregar.pack(pady=(40, 20))

        self.btn_ver = ctk.CTkButton(
            self.frame_login, text="Ver listado de rentas realizadas", width=300, height=40, font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.ver_rentas
        )
        self.btn_ver.pack(pady=(40, 20))

        self.btn_eliminar = ctk.CTkButton(
            self.frame_login, text="Eliminar un ticket del control", width=300, height=40, font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.eliminar_ticket
        )
        self.btn_eliminar.pack(pady=(40, 20))

        self.btn_informe = ctk.CTkButton(
            self.frame_login, text="Informe de Rentas", width=300, height=40, font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.generar_informe
        )
        self.btn_informe.pack(pady=(40, 20))

        self.btn_salir = ctk.CTkButton(
            self.frame_login, text="Salir del sistema", width=300, height=40, font=ctk.CTkFont(size=15, weight="bold"),
            command=self.cerrar_sesion
        )
        self.btn_salir.pack(pady=(40, 20))

    def rec_hum(self):
        # 1. Ocultamos el frame principal de administración
        self.frame_login.pack_forget()

        # 2. Si el segundo frame no ha sido creado, lo construimos de forma segura
        if not hasattr(self, "frame_segundo"):
            self.frame_segundo = ctk.CTkFrame(self)

            # --- SOLUCIÓN: Usamos una tupla ("Familia", Tamaño, "Estilo") en lugar de ctk.CTkFont ---
            fuente_botones = ("Arial", 15, "bold") 

            self.btn_agrega_rh = ctk.CTkButton(
                self.frame_segundo, 
                text="Agregar Nuevo Personal", 
                width=300, 
                height=40, 
                font=fuente_botones # <--- Cambiado aquí
            )
            self.btn_agrega_rh.pack(pady=(40, 20))

            self.btn_nomina = ctk.CTkButton(
                self.frame_segundo, 
                text="Realizar Nomina", 
                width=300, 
                height=40, 
                font=fuente_botones # <--- Cambiado aquí
            )
            self.btn_nomina.pack(pady=(40, 20))

            self.btn_volver = ctk.CTkButton(
                self.frame_segundo, 
                text="Volver", 
                width=300, 
                height=40, 
                font=fuente_botones, # <--- Cambiado aquí
                command=self.mostrar_menu_principal
            )
            self.btn_volver.pack(pady=(40, 20))

        # 3. Mostramos el segundo frame en pantalla
        self.frame_segundo.pack(pady=10, padx=30, fill="both", expand=True)

    def mostrar_menu_principal(self):
        if hasattr(self, "frame_segundo"):
            self.frame_segundo.pack_forget()  # Ocultamos submenú de RH
        self.frame_login.pack(pady=10, padx=30, fill="both", expand=True)  # Mostramos menú admin

    def cerrar_sesion(self):
        if self.ventana_menu_gral:
            self.destroy() # Destruye administración
            self.ventana_menu_gral.deiconify() # Regresa al menú general sin errores
        else:
            self.destroy()

if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()
