
import customtkinter as ctk
from logic import RoleManager, InventoryManager, RentalManager
from renta_autos import renta
from admin import admin as AdminPanel


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class LoginApp(ctk.CTk):
    """Ventana principal del menú general."""
    def __init__(self, rol_usuario, ventana_login, inventory, rental_manager):
        super().__init__()
        self.title("Menu General - Mi Carrito en Renta")
        self.geometry("900x700")
        self.resizable(False, False)

        #--- Controladores
        self.inventory = inventory
        self.rental_manager = rental_manager

        # CAMBIO: permite que el área principal crezca con el tamaño de la ventana.
        self.grid_columnconfigure(0, weight=2)
        self.grid_rowconfigure(0, weight=2)
        self.logic = LogicController(rol_usuario, ventana_login, self)
        self.frames = FrameManager(
            self, self.logic, self.inventory, self.rental_manager
        )

        # CAMBIO: conecta el controlador con el gestor de frames; abrir_admin()
        # usa esta referencia para mostrar el panel administrativo.
        self.logic.frames = self.frames

        #--- Inicializar interfaz
        self.frames.crear_menu_principal()
        self.logic.aplicar_permisos(self.frames)

class FrameManager:
    def __init__(self, root, logic, inventory, rental_manager):
        self.root = root
        self.logic = logic
        self.inventory = inventory
        self.rental_manager = rental_manager

        # CAMBIO: permite que el área principal crezca con el tamaño de la ventana.
        self.root.grid_columnconfigure(0, weight=2)
        self.root.grid_rowconfigure(0, weight=2)

        # Frames inicializados en None
        self.encabezado_frame = None
        self.frame_login = None
        self.frame_renta = None

        # CAMBIO: FrameManager conserva y reutiliza el panel de Administración.
        self.panel_admin = None
        self.admin = None

        # ⚠️ Nota: self.renta NO se instancia aquí, porque aún no existe encabezado_frame.
        self.renta = None

    def crear_menu_principal(self):

    # Eliminar el encabezado anterior, si existe.
        if self.encabezado_frame is not None:
            self.encabezado_frame.destroy()

        self.encabezado_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.encabezado_frame.grid(row=0, column=0, padx=5, pady=5, sticky="new")

        # Ahora sí, instanciar la clase renta con encabezado válido
        self.renta = renta(
            self.root, self.rental_manager, self.inventory, self.encabezado_frame)
        self.renta.limpiar_encabezado() 


        lbl_bienvenido = ctk.CTkLabel(self.encabezado_frame,
            text="MI CARRITO EN RENTA",
            font=ctk.CTkFont(size=15, weight="bold"))
        lbl_bienvenido.grid(row=0, column=0, padx=5, columnspan=5, pady=5, sticky="ew")

        rol_texto = f" - Rol Activo {self.logic.rol}" if self.logic.rol else " - Sin Rol"
        self.lbl_menu = ctk.CTkLabel(self.encabezado_frame,
            text=f"  MENU GENERAL  {rol_texto}",
            font=ctk.CTkFont(size=14, weight="bold"))
        self.lbl_menu.grid(row=1, column=0, padx=5, columnspan=5, pady=5, sticky="ew")

        # Botones principales
        self.btn_rentar = ctk.CTkButton(self.encabezado_frame, text="Renta de autos",
            command=self.renta.interfaz_renta)
        self.btn_rentar.grid(row=2, column=0,  padx=5, pady=5, sticky="ew")

        self.btn_ver = ctk.CTkButton(self.encabezado_frame, text="Administración",
            command=self.logic.abrir_admin)
        self.btn_ver.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.btn_eliminar = ctk.CTkButton(self.encabezado_frame, text="Taller/Mantenimiento")
        self.btn_eliminar.grid(row=2, column=2, padx=5, pady=5, sticky="ew")

        self.btn_informe = ctk.CTkButton(self.encabezado_frame, text="Utilerías")
        self.btn_informe.grid(row=2, column=3, padx=5, pady=5, sticky="ew")

        self.btn_salir = ctk.CTkButton(self.encabezado_frame, text="Salir del sistema",
            command=self.logic.cerrar_sesion)
        self.btn_salir.grid(row=2, column=4, padx=5, pady=5, sticky="ew")

    def mostrar_admin(self):
        # CAMBIO: ocultar el menú general conserva todos sus controles para volver.
        self.encabezado_frame.grid_remove()

        # CAMBIO: el contenedor, AdminPanel y sus controles se crean una sola vez.
        if self.panel_admin is None:
            self.panel_admin = ctk.CTkFrame(self.root)
            # CAMBIO: el panel administrativo expande su contenido al ocupar la ventana.
            self.panel_admin.grid_columnconfigure(0, weight=1)
            self.admin = AdminPanel(
                root=self.panel_admin,
                logic=self.logic
            )
            self.admin.menu_admin()

        self.panel_admin.grid(
            row=0, column=0,
            padx=20, pady=5,
            sticky="nsew"
        )

    def regresar_menu_principal(self):
        if self.panel_admin is not None:
            self.panel_admin.grid_remove()

        self.encabezado_frame.grid()                

class LogicController:
    """Encargado de la lógica de permisos y navegación."""
    def __init__(self, rol_usuario, ventana_login, ventana_principal):
        self.role_manager = RoleManager()
        self.rol = rol_usuario
        self.ventana_login = ventana_login
        self.ventana_principal = ventana_principal
        # La referencia a FrameManager se asigna desde LoginApp después de crear
        # ambos objetos; aquí todavía no existe self.frames ni self.logic.

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
        self.frames.mostrar_admin()

    def regresar_desde_admin(self, ventana_admin):
        ventana_admin.destroy()
        self.ventana_principal.deiconify()
        self.aplicar_permisos(self.ventana_principal.frames)

    def cerrar_sesion(self):
        ventana = self.ventana_principal
        ventana_login = self.ventana_login

        # Evitar que el cierre se solicite varias veces.
        if getattr(self, "_cerrando_sesion", False):
            return

        self._cerrando_sesion = True

        def finalizar_cierre():
            try:
                if ventana_login is not None:
                    try:
                        if ventana_login.winfo_exists():
                            ventana_login.deiconify()
                    except Exception as e:
                        print(f"Error al mostrar el login: {e}")

                ventana.destroy()

            except Exception as e:
                print(f"Error al cerrar la sesión: {e}")

        try:
            # Ejecutar el cierre en el siguiente ciclo de eventos.
            ventana.after_idle(finalizar_cierre)
        except Exception as e:
            print(f"No se pudo programar el cierre: {e}")
            self._cerrando_sesion = False

if __name__ == "__main__":
    # Prueba local simulando rol de mostrador
    # CAMBIO: se proporcionan los tres argumentos requeridos por LoginApp.
    # No hay una ventana de login previa en esta prueba directa, por eso se pasa None.
    inventory = InventoryManager()
    app = LoginApp(
        rol_usuario="mostrador",
        ventana_login=None,
        inventory=inventory,
        rental_manager=RentalManager(inventory)
    )
    app.mainloop()

