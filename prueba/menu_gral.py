''' 
datos necesarios para Copilot:este es mi script menu_gral.py, es el mas actualizado, se realizo un git pull al inicio de la joranada, 
rama activa class_pyton, todos los script , clases , metodos que se importan estan actualizados
ruta de archivos en documentar.txt

Objetivo de la revision: mensaje de error en linea 112

Pregunta para Copilot: por que este error?

'''

import customtkinter as ctk
from logic import RoleManager, InventoryManager
import menu_admin as m_admin

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class LoginApp(ctk.CTk):
    """Ventana principal del menú general."""
    def __init__(self, rol_usuario, ventana_login=None):
        super().__init__()
        self.title("Menu General - Mi Carrito en Renta")
        self.geometry("1000x900")
        self.resizable(False, False)

# Controladores
        self.logic = LogicController(rol_usuario, ventana_login, self)
        self.frames = FrameManager(self, self.logic)

# Inicializar interfaz
        self.frames.crear_menu_principal()
        self.logic.aplicar_permisos(self.frames)

class FrameManager:
    """Encargado de crear y manejar los distintos frames."""
    def __init__(self, root, logic):
        self.root = root
        self.logic = logic
        self.encabezado_frame = None
        self.frame_login = None
        self.frame_renta = None

    def limpiar_encabezado(self):
        if self.encabezado_frame:
            for widget in self.encabezado_frame.winfo_children():
                widget.destroy()

    def crear_menu_principal(self):
        self.limpiar_encabezado()
        self.encabezado_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.encabezado_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        lbl_bienvenido = ctk.CTkLabel(self.encabezado_frame,
            text="MI CARRITO EN RENTA",
            font=ctk.CTkFont(size=15, weight="bold"))
        lbl_bienvenido.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        rol_texto = f" - Rol Activo {self.logic.rol}" if self.logic.rol else " - Sin Rol"
        self.lbl_menu = ctk.CTkLabel(self.encabezado_frame,
            text=f"MENU GENERAL DEL SISTEMA {rol_texto}",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.lbl_menu.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        # Botones principales
        self.btn_rentar = ctk.CTkButton(self.encabezado_frame, text="Renta de autos",
            command=self.interfaz_renta
        )
        self.btn_rentar.grid(row=2, column=0, padx=10, pady=20, sticky="ew")

        self.btn_ver = ctk.CTkButton(self.encabezado_frame, text="Administración",
            command=self.logic.abrir_admin
        )
        self.btn_ver.grid(row=2, column=1, padx=10, pady=20, sticky="ew")

        self.btn_eliminar = ctk.CTkButton(self.encabezado_frame, text="Taller / mantenimiento")
        self.btn_eliminar.grid(row=2, column=2, padx=10, pady=20, sticky="ew")

        self.btn_informe = ctk.CTkButton(self.encabezado_frame, text="Utilerías")
        self.btn_informe.grid(row=2, column=3, padx=10, pady=20, sticky="ew")

        self.btn_salir = ctk.CTkButton(self.encabezado_frame, text="Salir del sistema",
            command=self.logic.cerrar_sesion
        )
        self.btn_salir.grid(row=2, column=4, padx=10, pady=20, sticky="ew")

# Configuración de columnas para que se expandan
        for i in range(5):  # número de columnas
            self.encabezado_frame.grid_columnconfigure(i, weight=1)

#--- Configuración de filas/columnas en la ventana principal
        # self.root.grid_rowconfigure(0, weight=0)  # encabezado no se expande
        self.root.grid_rowconfigure(1, weight=1)  # frame principal sí se expande
        self.root.grid_columnconfigure(0, weight=1)

    def interfaz_renta(self):
        self.limpiar_encabezado()
        pba = f"prueba"
        lbl_bienvenido = ctk.CTkLabel(self.encabezado_frame,
            text="GESTION DE RENTAS / desde interfaz_renta ",
            font=ctk.CTkFont(size=15, weight="bold"))
        lbl_bienvenido.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.frame_renta = ctk.CTkFrame(self.root)
        self.frame_renta.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        lbl_info = ctk.CTkLabel(self.frame_renta, text=f"GESTIÓN DE RENTAS/self.frame_renta {pba} ")
        lbl_info.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        btn_renta = ctk.CTkButton(self.frame_renta, 
            text="RENTA DE AUTOS",
            command=self.mostrar_auto)
        btn_renta.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        btn_regresar = ctk.CTkButton(self.frame_renta, 
            text="Regresar", 
            command=self.cerrar_frame_renta)
        btn_regresar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    def mostrar_auto(self):
#--- falta crear lo botones para que muestre los autos        
        self.frame_login = ctk.CTkFrame(self.root)
        self.frame_login.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        lbl_info = ctk.CTkLabel(self.frame_login, text="EN ESTE FRAME COLOCAR LOS AUTOS PARA RENTA Y LOS WIDGET")
        lbl_info.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        lbl_ver = ctk.CTkLabel(self.frame_login, text="aqui debe salir la lista de autos")
        lbl_ver.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    def cerrar_frame_renta(self):
        if self.frame_renta:
            self.frame_renta.destroy()
            self.crear_menu_principal()        

class LogicController:
    """Encargado de la lógica de permisos y navegación."""
    def __init__(self, rol_usuario, ventana_login, ventana_principal):
        self.role_manager = RoleManager()
        self.inventario = InventoryManager()
        self.rol = rol_usuario
        self.ventana_login = ventana_login
        self.ventana_principal = ventana_principal

    def aplicar_permisos(self, frames: FrameManager):
        botones = {
            "renta": frames.btn_rentar,
            "admin": frames.btn_ver,
            "taller": frames.btn_eliminar,
            "utilerias": frames.btn_informe
        }
        for btn in botones.values():
            btn.configure(state="disabled")

        permisos = self.role_manager.aplicar_permisos(self.rol)
        for permiso in permisos:
            if permiso in botones:
                botones[permiso].configure(state="normal")

    def abrir_admin(self):
        def ejecutar():
            self.ventana_principal.withdraw()
            nueva_admin = m_admin.DashboardApp(ventana_menu_gral=self.ventana_principal)
            nueva_admin.protocol("WM_DELETE_WINDOW", lambda: self.regresar_desde_admin(nueva_admin))
            nueva_admin.mainloop()
        self.ventana_principal.after(100, ejecutar)

    def regresar_desde_admin(self, ventana_admin):
        ventana_admin.destroy()
        self.ventana_principal.deiconify()
        self.aplicar_permisos(self.ventana_principal.frames)

    def renta_auto(self):
        autos = self.inventario.obtener_autos_disponibles()
        if autos:
            for auto in autos:
                texto=f"{auto['id']} - {auto['marca']} {auto['modelo']} {auto['precio_dia']}"
        else:
            print("No hay autos disponibles ❌")

    def cerrar_sesion(self):
        if self.ventana_login:
            self.ventana_principal.destroy()
            self.ventana_login.deiconify()
        else:
            self.ventana_principal.destroy()
         
if __name__ == "__main__":
    # Prueba local simulando rol de mostrador
    app = LoginApp(rol_usuario="mostrador")
    app.mainloop()