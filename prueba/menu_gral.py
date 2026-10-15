
import customtkinter as ctk
from logic import RoleManager, InventoryManager
from renta_autos import renta
from admin import admin as AdminPanel


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class LoginApp(ctk.CTk):
    """Ventana principal del menú general."""
    def __init__(self, rol_usuario, ventana_login, inventory):
        super().__init__()
        self.title("Menu General - Mi Carrito en Renta")
        self.geometry("1000x900")
        self.resizable(False, False)
        self.panel_admin = None

#--- Controladores
        self.inventory = inventory
        self.logic = LogicController(rol_usuario, ventana_login, self, self.inventory)
        self.frames = FrameManager(self, self.logic, self.inventory)
        self.inventario = InventoryManager()

#--- Inicializar interfaz
        self.frames.crear_menu_principal()
        self.logic.aplicar_permisos(self.frames)

class FrameManager:
    def __init__(self, root, logic, inventory):
        self.root = root
        self.logic = logic
        self.inventory = inventory

        # Frames inicializados en None
        self.encabezado_frame = None
        self.frame_login = None
        self.frame_renta = None

        # ⚠️ Nota: self.renta NO se instancia aquí, porque aún no existe encabezado_frame.
        self.renta = None

    def crear_menu_principal(self):

    # Eliminar el encabezado anterior, si existe.
        if self.encabezado_frame is not None:
            self.encabezado_frame.destroy()

        self.encabezado_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.encabezado_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        # Ahora sí, instanciar la clase renta con encabezado válido
        self.renta = renta(self.root, self.logic, self.encabezado_frame)
        self.renta.limpiar_encabezado() 

        lbl_bienvenido = ctk.CTkLabel(self.encabezado_frame,
            text="MI CARRITO EN RENTA",
            font=ctk.CTkFont(size=15, weight="bold"))
        lbl_bienvenido.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        rol_texto = f" - Rol Activo {self.logic.rol}" if self.logic.rol else " - Sin Rol"
        self.lbl_menu = ctk.CTkLabel(self.encabezado_frame,
            text=f"  MENU GENERAL  {rol_texto}",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.lbl_menu.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Botones principales
        self.btn_rentar = ctk.CTkButton(self.encabezado_frame, text="Renta de autos",
            command=self.renta.interfaz_renta)
        self.btn_rentar.grid(row=2, column=0, padx=10, pady=20, sticky="ew")

        self.btn_ver = ctk.CTkButton(self.encabezado_frame, text="Administración",
            command=self.logic.abrir_admin)
        self.btn_ver.grid(row=2, column=1, padx=10, pady=20, sticky="ew")

        self.btn_eliminar = ctk.CTkButton(self.encabezado_frame, text="Taller / mantenimiento")
        self.btn_eliminar.grid(row=2, column=2, padx=10, pady=20, sticky="ew")

        self.btn_informe = ctk.CTkButton(self.encabezado_frame, text="Utilerías")
        self.btn_informe.grid(row=2, column=3, padx=10, pady=20, sticky="ew")

        self.btn_salir = ctk.CTkButton(self.encabezado_frame, text="Salir del sistema",
            command=self.logic.cerrar_sesion)
        self.btn_salir.grid(row=2, column=4, padx=10, pady=20, sticky="ew")

    def mostrar_admin(self):
        # Ocultar el menú general
        self.encabezado_frame.grid_remove()

        # Crear el panel administrativo una sola vez
        if self.panel_admin is None:
            self.panel_admin = ctk.CTkFrame(self.root)
            self.admin = AdminPanel(
                root=self.panel_admin,
                logic=self.logic,
                encabezado_frame=self.encabezado_frame
            )

        self.panel_admin.grid(
            row=0, column=0,
            padx=20, pady=10,
            sticky="nsew"
        )

        self.admin.menu_admin()

    def mostrar_admin(self):
        # Ocultar el menú general
        self.encabezado_frame.grid_remove()

        # Crear el panel administrativo una sola vez
        if self.panel_admin is None:
            self.panel_admin = ctk.CTkFrame(self.root)
            self.admin = AdminPanel(
                root=self.panel_admin,
                logic=self.logic,
                encabezado_frame=self.encabezado_frame
            )

        self.panel_admin.grid(
            row=0, column=0,
            padx=20, pady=10,
            sticky="nsew"
        )

        self.admin.menu_admin()

    def regresar_menu_principal(self):
        if self.panel_admin is not None:
            self.panel_admin.grid_remove()

        self.encabezado_frame.grid()                

class LogicController:
    """Encargado de la lógica de permisos y navegación."""
    def __init__(self, rol_usuario, ventana_login, ventana_principal, inventory):
        self.role_manager = RoleManager()
        self.inventario = inventory
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


    def calcular_precio_renta(self, id_auto_str, dias_str):
        try:
            id_auto = int(id_auto_str)
            dias = int(dias_str)
            if dias <= 0:
                return None, "Los días de renta deben ser mayores que cero."
            total = self.inventario.calcular_precio(id_auto, dias)
            if total is None:
                return None, "El ID no corresponde a un auto disponible."
            return total, "OK"
        except (TypeError, ValueError):
            return None, "⚠️ Ingresa un número válido de días y un ID correcto."

    def calcular_presupuesto_regreso(self, km_str, dias_str, id_str):
        try:
            id_auto = int(id_str)
            dias_reales = int(dias_str)
            km_nuevos = float(km_str)
        except (TypeError, ValueError):
            return None, "⚠️ Ingresa valores numéricos válidos en los campos."

        # El controlador valida la entrada; InventoryManager aplica las reglas del inventario.
        return self.inventario.calcular_presupuesto_regreso(
            id_auto, dias_reales, km_nuevos
        )

    def confirmar_regreso_auto(self, id_auto_str, dias_str, km_str):
        """Valida los campos y delega el guardado de la devolución al inventario."""
        try:
            id_auto = int(id_auto_str)
            dias_reales = int(dias_str)
            km_nuevos = float(km_str)
        except (TypeError, ValueError):
            return False, "Ingresa un ID, días y kilómetros válidos."

        return self.inventario.procesar_regreso(
            id_auto, dias_reales, km_nuevos
        )

    def confirmar_renta_auto(self, id_auto_str, dias_str):
        """Valida los campos y devuelve el resultado real de procesar la renta."""
        try:
            id_auto = int(id_auto_str)
            dias = int(dias_str)
        except (TypeError, ValueError):
            return False, "Ingresa un ID y días válidos."

        return self.inventario.procesar_renta(id_auto, dias)

if __name__ == "__main__":
    # Prueba local simulando rol de mostrador
    app = LoginApp(rol_usuario="mostrador")
    app.mainloop()

