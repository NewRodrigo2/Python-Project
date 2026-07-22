import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class LoginApp(ctk.CTk):
    def __init__(self, rol_usuario=None):
        super().__init__()
        self.rol = rol_usuario

        self.title("Login - Mi Carrito en Renta")
        self.geometry("1100x800")
        self.resizable(False, False)
        self.crear_interfaz_login()  # 3. Creación de los Componentes (Widgets)

        self.aplicar_permisos()

    def crear_interfaz_login(self):
        self.lbl_bienvenido = ctk.CTkLabel(
        self,
        text="TITULO GENERAL DEL SISTEMA, NOMBRE DE LA EMPRESA ", 
        font=ctk.CTkFont(size=30, weight="bold")
        )
        self.lbl_bienvenido.pack(pady=(40, 20))
        
        rol_texto = f" - Rol Activo {self.rol}" if self.rol else ""
        self.lbl_menu = ctk.CTkLabel(self,
        text=f"MENU GENERAL DEL SISTEMA {rol_texto}", 
        font=ctk.CTkFont(size=25, weight="bold")
        )
        self.lbl_menu.pack(pady=(25, 5), padx=30, anchor="w")
        
        # ---------------------------------------- CONTENEDOR CENTRAL (FRAME) ---
        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.pack(pady=10, padx=30, fill="both", expand=True)
        # ----------------------------------------------------------------------

        self.btn_rentar = ctk.CTkButton(
            self.frame_login,  
            text=" Renta de autos", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.procesar_login
        )
        self.btn_rentar.pack(pady=(40, 20))

        self.btn_ver = ctk.CTkButton(
            self.frame_login,  
            text=" Administracion", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.procesar_login
        )
        self.btn_ver.pack(pady=(40, 20))

        self.btn_eliminar = ctk.CTkButton(
            self.frame_login,  
            text=" Taller / mantenimiento", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.procesar_login
        )
        self.btn_eliminar.pack(pady=(40, 20))

        self.btn_informe = ctk.CTkButton(
            self.frame_login,  
            text=" Utilerias ", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.procesar_login
        )
        self.btn_informe.pack(pady=(40, 20))

        self.btn_salir = ctk.CTkButton(
            self.frame_login,  
            text=" Salir del sistema", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self.cerrar_sesion
        )
        self.btn_salir.pack(pady=(40, 20))

    def aplicar_permisos(self):
        if not self.rol:
            return
        botones_menu = [self.btn_rentar, self.btn_ver, self.btn_eliminar, self.btn_informe]
        for btn in botones_menu:
            btn.configure(state="disabled")
        rol_lower = self.rol.lower()

        if rol_lower == "mostrador":
            self.btn_rentar.configure(state="normal")
        elif rol_lower == "administrador":
            for btn in botones_menu:
                btn.configure(state="normal")
        elif rol_lower == "mecanico" or rol_lower == "mantenimiento":
            self.btn_eliminar.configure(state="normal")
        elif rol_lower == "financieros" or rol_lower == "supervisor":
            self.btn_informe.configure(state="normal")


    

    def cerrar_sesion(self):
            self.destroy()  # Destruye el Dashboard
       

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()


