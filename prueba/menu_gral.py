import customtkinter as ctk 
import menu_admin as m_admin 

ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue") 

class LoginApp(ctk.CTk): 
    # Añadimos ventana_login=None para guardar la referencia y no perder el hilo
    def __init__(self, rol_usuario=None, ventana_login=None): 
        super().__init__() 
        self.rol = rol_usuario 
        self.ventana_login = ventana_login # Guardamos el login aquí
        
        self.title("Menu General - Mi Carrito en Renta") 
        self.geometry("1100x800") 
        self.resizable(False, False) 
        
        # Primero creamos la interfaz para que existan los botones
        self.crear_interfaz_login() 
        # Forzamos la actualización de la interfaz gráfica antes de bloquear botones
        self.update_idletasks()
        self.aplicar_permisos() 

    def crear_interfaz_login(self): 
        self.lbl_bienvenido = ctk.CTkLabel( 
            self, text="TITULO GENERAL DEL SISTEMA, NOMBRE DE LA EMPRESA ", font=ctk.CTkFont(size=30, weight="bold") 
        ) 
        self.lbl_bienvenido.pack(pady=(40, 20)) 
        
        rol_texto = f" - Rol Activo {self.rol}" if self.rol else " - Sin Rol" 
        self.lbl_menu = ctk.CTkLabel(
            self, text=f"MENU GENERAL DEL SISTEMA {rol_texto}", font=ctk.CTkFont(size=25, weight="bold") 
        ) 
        self.lbl_menu.pack(pady=(25, 5), padx=30, anchor="w") 

        self.frame_login = ctk.CTkFrame(self) 
        self.frame_login.pack(pady=10, padx=30, fill="both", expand=True) 
        
        self.btn_rentar = ctk.CTkButton( 
            self.frame_login, text=" Renta de autos", width=300, height=40, font=("Arial", 15, "bold")
        ) 
        self.btn_rentar.pack(pady=(20, 10)) 
        
        self.btn_ver = ctk.CTkButton( 
            self.frame_login, text=" Administracion", width=300, height=40, font=("Arial", 15, "bold"), 
            command=self.abrir_admin 
        ) 
        self.btn_ver.pack(pady=(20, 10)) 
        
        self.btn_eliminar = ctk.CTkButton( 
            self.frame_login, text=" Taller / mantenimiento", width=300, height=40, font=("Arial", 15, "bold")
        ) 
        self.btn_eliminar.pack(pady=(20, 10)) 
        
        self.btn_informe = ctk.CTkButton( 
            self.frame_login, text=" Utilerias ", width=300, height=40, font=("Arial", 15, "bold")
        ) 
        self.btn_informe.pack(pady=(20, 10)) 
        
        self.btn_salir = ctk.CTkButton( 
            self.frame_login, text=" Salir del sistema", width=300, height=40, font=("Arial", 15, "bold"), 
            command=self.cerrar_sesion 
        ) 
        self.btn_salir.pack(pady=(20, 10)) 

    def aplicar_permisos(self): 
        botones_menu = [self.btn_rentar, self.btn_ver, self.btn_eliminar, self.btn_informe] 
        
        # 1. PASO OBLIGATORIO: Deshabilitar TODO sin condiciones
        for btn in botones_menu: 
            btn.configure(state="disabled") 

        # Si por alguna razón el rol llegó vacío, detenemos aquí (todo se queda deshabilitado)
        if not self.rol: 
            print("Advertencia: No se recibió ningún rol en el Menú General.")
            return 

        # 2. Limpieza estricta de acentos
        rol_procesado = self.rol.lower().replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").strip() 
        print(f"Aplicando permisos para el rol procesado: '{rol_procesado}'") # Para verificar en terminal

        # 3. Activación quirúrgica
        if rol_procesado == "mostrador": 
            self.btn_rentar.configure(state="normal") 
        elif rol_procesado == "administrador": 
            for btn in botones_menu: 
                btn.configure(state="normal") 
        elif rol_procesado == "mecanico" or rol_procesado == "mantenimiento": 
            self.btn_eliminar.configure(state="normal") 
        elif rol_procesado == "financieros" or rol_procesado == "supervisor": 
            self.btn_informe.configure(state="normal") 

    def abrir_admin(self): 
        # Ocultamos esta ventana en lugar de destruirla para congelar sus animaciones de forma segura
        self.withdraw() 
        # Pasamos 'self' para que la administración sepa cómo regresar al menú general
        nuva_admin = m_admin.DashboardApp(ventana_menu_gral=self) 
        nuva_admin.mainloop() 

    def cerrar_sesion(self): 
        # Si venimos desde el login, destruimos esta ventana y volvemos a mostrar el login original
        if self.ventana_login:
            self.destroy()
            self.ventana_login.deiconify()
        else:
            self.destroy()

if __name__ == "__main__": 
    app = LoginApp() 
    app.mainloop()
