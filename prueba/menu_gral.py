''' menu_gral.py
datos necesarios para Copilot: este es mi script main.py, es el mas actualizado, se realizo un git pull al inicio de la joranada, 
rama activa class_pyton, todos los script , clases , metodos que se importan estan actualizados
'''
import customtkinter as ctk
from logic import RoleManager,InventoryManager
import menu_admin as m_admin # Descomenta en tu entorno


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class LoginApp(ctk.CTk):
    def __init__(self, rol_usuario, ventana_login):
        super().__init__()
        self.role_manager = RoleManager()
        self.ventana_login = ventana_login
        self.rol = rol_usuario
        self.inventario = InventoryManager()
        self.crear_interfaz_login()       

# aquí usas roles_disponibles para construir menús dinámicos
        roles_disponibles = self.role_manager.obtener_roles()

        self.title("Menu General - Mi Carrito en Renta")
        self.geometry("1100x800")
        self.resizable(False, False)
        
# Contenedor principal para los títulos mutables
        self.encabezado_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.encabezado_frame.grid(row=0, column=0, padx=20, sticky="nsew")
        
# Inicializar los frames como None
        self.frame_login = None
        self.frame_renta = None
        
# Cargar interfaz inicial
        self.crear_interfaz_login()
        self.update_idletasks()      
        self.aplicar_permisos()

    def limpiar_encabezado(self):
        """Elimina los widgets del encabezado para redibujarlos."""
        for widget in self.encabezado_frame.winfo_children():
            widget.destroy()

    def crear_interfaz_login(self):
        # self.limpiar_encabezado()
        
#--- FRAME ENCABEZADO ---
        self.encabezado_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.encabezado_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

#--- Títulos en el contenedor de encabezado
        lbl_bienvenido = ctk.CTkLabel(
            self.encabezado_frame, 
            text="MI CARRITO EN RENTA", 
            font=ctk.CTkFont(size=25, weight="bold"))
        lbl_bienvenido.grid(row=0, column=0, padx=10, pady=20, sticky="ew")
        
        rol_texto = f" - Rol Activo {self.rol}" if self.rol else " - Sin Rol"
        self.lbl_menu = ctk.CTkLabel(
            self.encabezado_frame, 
            text=f"MENU GENERAL DEL SISTEMA {rol_texto}", 
            font=ctk.CTkFont(size=22, weight="bold"))
        self.lbl_menu.grid(row=1, column=0, padx=10, pady=20, sticky="ew")

#--- FRAME PRINCIPAL (BOTONES) ---
        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.grid(row=1, column=0, padx=30, pady=10, sticky="nsew")

#--- BOTONES EN UNA SOLA FILA ---
        self.btn_rentar = ctk.CTkButton(
            self.frame_login, text=" Renta de autos", width=300, height=40, 
            font=("Arial", 15, "bold"), command=self.interfaz_renta)
        self.btn_rentar.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

        self.btn_ver = ctk.CTkButton(
            self.frame_login, text=" Administracion", width=300, height=40, 
            font=("Arial", 15, "bold"), command=self.abrir_admin)
        self.btn_ver.grid(row=0, column=1, padx=10, pady=20, sticky="ew")

        self.btn_eliminar = ctk.CTkButton(
            self.frame_login, text=" Taller / mantenimiento", width=300, height=40, 
            font=("Arial", 15, "bold"))
        self.btn_eliminar.grid(row=0, column=2, padx=10, pady=20, sticky="ew")

        self.btn_informe = ctk.CTkButton(
            self.frame_login, text=" Utilerias ", width=300, height=40, 
            font=("Arial", 15, "bold"))
        self.btn_informe.grid(row=0, column=3, padx=10, pady=20, sticky="ew")

        self.btn_salir = ctk.CTkButton(
            self.frame_login, text=" Salir del sistema", width=300, height=40, 
            font=("Arial", 15, "bold"), command=self.cerrar_sesion)
        self.btn_salir.grid(row=0, column=4, padx=10, pady=20, sticky="ew")

#--- Configuración de columnas para que se expandan ---
        for i in range(5):  # número de columnas
            self.frame_login.grid_columnconfigure(i, weight=1)

#--- Configuración de filas/columnas en la ventana principal ---
        self.grid_rowconfigure(0, weight=0)  # encabezado no se expande
        self.grid_rowconfigure(1, weight=1)  # frame_login sí se expande
        self.grid_columnconfigure(0, weight=1)
        
    def aplicar_permisos(self):
        # Deshabilitamos todos los botones primero
        botones_menu = {
            "renta": self.btn_rentar,
            "admin": self.btn_ver,
            "taller": self.btn_eliminar,
            "utilerias": self.btn_informe
        }
        for btn in botones_menu.values():
            btn.configure(state="disabled")

        if not self.rol:
            print("Advertencia: No se recibió ningún rol en el Menú General.")
            return

#--- Usamos RoleManager para obtener permisos, llamamos a logic/class/metodo pasamos parametro 
        permisos = self.role_manager.aplicar_permisos(self.rol)  

        # Activamos solo los botones permitidos
        for permiso in permisos:
            if permiso in botones_menu:
                botones_menu[permiso].configure(state="normal")

# ...........................  correir: debe abrir menu_admin.py
    def abrir_admin(self):
        """Oculta el menú general y abre la administración de forma segura."""
        def ejecutar_apertura():
            # Ocultamos esta ventana de forma segura después del click
            self.withdraw() 
            
            # Pasamos 'self' para que la administración sepa cómo regresar al menú general
            # NOTA: Asegúrate de que DashboardApp en 'menu_admin.py' herede de ctk.CTkToplevel o ctk.CTk
            nueva_admin = m_admin.DashboardApp(ventana_menu_gral=self)
            
            # CONFIGURACIÓN DE SEGURIDAD PARA LA "X" DE LA VENTANA
            # Si cierran el Dashboard desde la X, llamamos a una función que restaure el menú general
            nueva_admin.protocol("WM_DELETE_WINDOW", lambda: self.regresar_desde_admin(nueva_admin))
            
            nueva_admin.mainloop()

        # Esperamos 100 milisegundos para que termine la animación del click del botón
        self.after(100, ejecutar_apertura)

    def regresar_desde_admin(self, ventana_admin):
        """Destruye de forma segura la ventana de admin y restaura el menú general."""
        def restaurar():
            ventana_admin.destroy()  # Destruye la ventana de administración
            self.deiconify()         # Hace aparecer de nuevo el menú general
            self.aplicar_permisos()  # Re-aplica los permisos por seguridad
            
        self.after(100, restaurar)


    def interfaz_renta(self):
        # 1. Ocultar el frame anterior para dar espacio al nuevo
        if self.frame_login:
           self.frame_login.pack_forget()
        
        self.limpiar_encabezado()   
        
        # 3. LÍNEA 98 CORREGIDA: Creación y empaquetado correcto del segundo frame
        self.frame_renta = ctk.CTkFrame(self)
        self.frame_renta.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        
#--- AGREGAR CONTENIDO AL SEGUNDO FRAME ---
# 2. Configurar nuevos títulos del encabezado

        lbl_info_renta = ctk.CTkLabel(
            self.encabezado_frame, text="GESTION DE RENTAS", font=("Arial", 34)
        )
        lbl_info_renta.pack(pady=20)
        
        lbl_titulo_renta = ctk.CTkButton(
            self.frame_renta, text="RENTA DE AUTOS", width=300, height=40, 
            font=ctk.CTkFont(size=18, weight="bold"),
            command=self.renta_auto

        )
        lbl_titulo_renta.pack(pady=(20, 10))
        
        lbl_entrega = ctk.CTkButton(
            self.frame_renta, text="ENTREGA DE AUTOS",width=300, height=40, font=ctk.CTkFont(size=18, weight="bold")
        )
        lbl_entrega.pack(pady=(20, 10))

        # Botón para regresar al menú anterior
        btn_regresar = ctk.CTkButton(
            self.frame_renta, text="REGRESA A MENU PRINCIPAL", width=300, height=40,font=ctk.CTkFont(size=18, weight="bold"),
            command=self.regresar_menu_principal
        )
        btn_regresar.pack(pady=(20,10))

    def renta_auto(self):
# Limpiar frame anterior si existe
        if hasattr(self, "frame_renta") and self.frame_renta is not None:
            self.frame_renta.destroy()

# Crear nuevo frame
        frame_renta = ctk.CTkFrame(self)
        frame_renta.pack(fill="both", expand=True)

# Encabezado
        lbl_titulo = ctk.CTkLabel(frame_renta, 
            text="Autos disponibles para renta", 
            font=("Arial", 20))
        lbl_titulo.pack(pady=10)

# Obtener listado desde InventoryManager
        autos_disponibles = self.inventario.obtener_autos_disponibles()

# Mostrar listado en labels
        if autos_disponibles:
            for auto in autos_disponibles:
                texto = f"{auto['id']} - {auto['marca']} {auto['modelo']} {auto['precio_dia']}"
                lbl_auto = ctk.CTkLabel(frame_renta, text=texto)
                lbl_auto.pack(anchor="w", padx=20)
        else:
            lbl_vacio = ctk.CTkLabel(frame_renta, text="No hay autos disponibles ❌")
            lbl_vacio.pack(pady=20)

# widegt
        self.limpiar_encabezado()

        self.l1 = ctk.CTkLabel(frame_renta, 
            text="Cual auto desea rentar")
        self.l1.pack(pady=20)

        self.e1 = ctk.CTkEntry(frame_renta, width=320, placeholder_text="Ingrese ID de auto")
        self.e1.pack(pady=20)

        self.e2 = ctk.CTkEntry(frame_renta, width=320, placeholder_text="Km esperados")
        self.e2.pack(pady=5, padx=30)

        self.b1 = ctk.CTkButton(frame_renta, text="rentar")
        self.b1.pack(pady=20)

        self.btn_b2 = ctk.CTkButton(frame_renta, text="Regresar",
            command=self.regresar_menu_principal)
        self.btn_b2.pack(pady=20)

    def regresar_menu_principal(self):
        """Destruye el frame de renta y vuelve a dibujar el menú principal."""
        if self.frame_renta:
            self.frame_renta.destroy()
        self.crear_interfaz_login()
        self.aplicar_permisos()

    def cerrar_sesion(self):
        if self.ventana_login:
            self.destroy()
            self.ventana_login.deiconify()
        else:
            self.destroy()

if __name__ == "__main__":
    # Prueba local simulando rol de mostrador
    app = LoginApp(rol_usuario="mostrador")
    app.mainloop()
