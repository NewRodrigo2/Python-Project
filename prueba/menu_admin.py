''' este script se llama menu_admin.py 
'''
import json
import os
from pathlib import Path
import customtkinter as ctk
from logic import RoleManager
# Importamos nuestro módulo de Recursos Humanos
import rh as hr 

# ------------------------------------------------------------------------------------------
ruta_actual = os.getcwd() 
unidad = os.path.splitdrive(ruta_actual)[0] 
if unidad == "C:":
    CARPETA_DATOS = Path(unidad + "\\") / "Users" / "danie" / "Documents" / "Python Project" / "prueba" / "datos"
else:
    CARPETA_DATOS = Path(unidad + "\\") / "Python" / "Python Project" / "prueba" / "datos"

# Rutas de archivos
ARCHIVO_DATOS = CARPETA_DATOS / "inventario.json"
ARCHIVO_CONTROL = CARPETA_DATOS / "control.json"
ARCHIVO_TEX = CARPETA_DATOS / "autos_ordenados.txt"
PERSONAL = CARPETA_DATOS / "personal.json"  
# ------------------------------------------------------------------------------------------

class DashboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.role_manager = RoleManager()
        self.ventana_menu_gral = ventana_menu_gral
        roles_disponibles = self.role_manager.obtener_roles()
        # aquí usas roles_disponibles para permisos o menús


        self.title("Administración")
        self.geometry("800x800")
        self.resizable(False, False)
        self.crear_interfaz_login()

    def crear_interfaz_login(self):
        self.lbl_bienvenido = ctk.CTkLabel(
            self, text="ADMINISTRACIÓN", font=ctk.CTkFont(size=24, weight="bold")
        )
        self.lbl_bienvenido.pack(pady=(35, 20))

        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.pack(pady=10, padx=30, fill="both", expand=True)

        self.btn_rh = ctk.CTkButton(
            self.frame_login, text="Recursos Humanos", width=300, height=40, font=ctk.CTkFont(size=15, weight="bold"),
            command=self.rec_hum
        )
        self.btn_rh.pack(pady=(35, 20))

        self.btn_agregar = ctk.CTkButton(
            self.frame_login, text="Agregar nuevo auto al inventario", width=300, height=40, font=ctk.CTkFont(size=15, weight="bold")
        )
        self.btn_agregar.pack(pady=(35, 20))

        self.btn_ver = ctk.CTkButton(
            self.frame_login, text="Ver listado de rentas realizadas", width=300, height=40, font=ctk.CTkFont(size=15, weight="bold")
        )
        self.btn_ver.pack(pady=(35, 20))

        self.btn_eliminar = ctk.CTkButton(
            self.frame_login, text="Eliminar un ticket del control", width=300, height=40, font=ctk.CTkFont(size=15, weight="bold")
        )
        self.btn_eliminar.pack(pady=(35, 20))

        self.btn_informe = ctk.CTkButton(
            self.frame_login, text="Informe de Rentas", width=300, height=40, font=ctk.CTkFont(size=15, weight="bold")
        )
        self.btn_informe.pack(pady=(35, 20))

        self.btn_salir = ctk.CTkButton(
            self.frame_login, text="Salir del sistema", width=300, height=40, font=ctk.CTkFont(size=15, weight="bold"),
            command=self.cerrar_sesion
        )
        self.btn_salir.pack(pady=(35, 20))

    def rec_hum(self):
        self.frame_login.pack_forget()

        if not hasattr(self, "frame_segundo"):
            self.frame_segundo = ctk.CTkFrame(self)
            fuente_botones = ("Arial", 15, "bold") 

            self.btn_agrega_rh = ctk.CTkButton(
                self.frame_segundo, 
                text="Agregar Nuevo Personal", 
                width=300, 
                height=40, 
                font=fuente_botones, 
                command=self.rh_frame
            )
            self.btn_agrega_rh.pack(pady=(35, 20))

            self.btn_nomina = ctk.CTkButton(
                self.frame_segundo, 
                text="Realizar Nomina", 
                width=300, 
                height=40, 
                font=fuente_botones
            )
            self.btn_nomina.pack(pady=(35, 20))

            self.btn_volver = ctk.CTkButton(
                self.frame_segundo, 
                text="Volver", 
                width=300, 
                height=40, 
                font=fuente_botones, 
                command=self.mostrar_menu_principal
            )
            self.btn_volver.pack(pady=(35, 20))

        self.frame_segundo.pack(pady=10, padx=30, fill="both", expand=True)

    def rh_frame(self):
        self.frame_segundo.pack_forget()

        if not hasattr(self, "frame_tercer"):
            self.frame_tercer = ctk.CTkFrame(self)
            fuente_botones = ("Arial", 15, "bold") 

            self.lbl_captura = ctk.CTkLabel(
                self.frame_tercer, 
                text="CAPTURA DE NUEVO PERSONAL", 
                font=fuente_botones
            )
            self.lbl_captura.pack(pady=(35, 20))

            self.txt_nombre = ctk.CTkEntry(    
                self.frame_tercer,
                width=320, placeholder_text="Nombre del trabajador"
            )
            self.txt_nombre.pack(pady=5, padx=30)

            self.roles_disponibles = ["Mostrador", "Financieros", "Mecánico", "Administrador", "Supervisor"]
        
            self.cmb_rol = ctk.CTkComboBox(
                self.frame_tercer, values=self.roles_disponibles, width=320, state="readonly"
            )
            self.cmb_rol.set("Mostrador")
            self.cmb_rol.pack(pady=5, padx=30)

            self.txt_area = ctk.CTkEntry(
                self.frame_tercer,
                width=320, placeholder_text="Area de trabajo"
            )
            self.txt_area.pack(pady=5, padx=30)

            self.txt_hr_cont = ctk.CTkEntry(
                self.frame_tercer,
                width=320, placeholder_text="Horas contratadas"
            )
            self.txt_hr_cont.pack(pady=5, padx=30)

            self.txt_sueldo = ctk.CTkEntry(
                self.frame_tercer,
                width=320, placeholder_text="Sueldo Base"
            )
            self.txt_sueldo.pack(pady=5, padx=30)

            self.txt_psw = ctk.CTkEntry(
                self.frame_tercer,
                width=320, placeholder_text="Password", show="*"
            )
            self.txt_psw.pack(pady=5, padx=30)            

            self.btn_grabar = ctk.CTkButton(
                self.frame_tercer,
                text="GRABAR DATOS",
                font=fuente_botones,
                command=self.graba_dato
            )
            self.btn_grabar.pack(pady=(10, 10))

            # Label de estado/mensaje para notificar si se guardó correctamente
            self.lbl_estado = ctk.CTkLabel(
                self.frame_tercer, text="", font=("Arial", 12)
            )
            self.lbl_estado.pack(pady=5)

            self.btn_salir = ctk.CTkButton(
                self.frame_tercer,
                text="VOLVER",
                font=fuente_botones,
                command=self.mostrar_frame_segundo
            )
            self.btn_salir.pack(pady=(10, 20))

        self.frame_tercer.pack(pady=10, padx=30, fill="both", expand=True)

    def graba_dato(self):
        # 1. Obtener valores de la interfaz
        nombre = self.txt_nombre.get().strip()
        rol = self.cmb_rol.get()
        area = self.txt_area.get().strip()
        horas = self.txt_hr_cont.get().strip()
        sueldo = self.txt_sueldo.get().strip()
        password = self.txt_psw.get().strip()

        # Validar campos vacíos básicos
        if not nombre or not area or not horas or not sueldo or not password:
            self.lbl_estado.configure(text="⚠ Todos los campos son obligatorios.", text_color="red")
            return

        # 2. Llamar a la función de lógica de negocio en hr.py
        exito, mensaje = hr.agregar_personal_gui(
            nombre=nombre,
            rol=rol,
            area=area,
            hrs_cont=horas,
            sueldo=sueldo,
            password=password
        )

        # 3. Mostrar resultado al usuario
        if exito:
            self.lbl_estado.configure(text=f"✓ {mensaje}", text_color="green")
            self.limpiar_formulario()
        else:
            self.lbl_estado.configure(text=f"✕ {mensaje}", text_color="red")

    def limpiar_formulario(self):
        """Limpia los campos tras una grabación exitosa."""
        self.txt_nombre.delete(0, 'end')
        self.cmb_rol.set("Mostrador")
        self.txt_area.delete(0, 'end')
        self.txt_hr_cont.delete(0, 'end')
        self.txt_sueldo.delete(0, 'end')
        self.txt_psw.delete(0, 'end')

    def mostrar_menu_principal(self):
        if hasattr(self, "frame_segundo"):
            self.frame_segundo.pack_forget()
        self.frame_login.pack(pady=10, padx=30, fill="both", expand=True)

    def mostrar_frame_segundo(self):
        if hasattr(self, "frame_tercer"):
            self.frame_tercer.pack_forget()
            if hasattr(self, "lbl_estado"):
                self.lbl_estado.configure(text="") # Limpia mensaje previo
        self.frame_segundo.pack(pady=10, padx=30, fill="both", expand=True)

    def cerrar_sesion(self):
        if self.ventana_menu_gral:
            self.destroy()
            self.ventana_menu_gral.deiconify()
        else:
            self.destroy()

if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()