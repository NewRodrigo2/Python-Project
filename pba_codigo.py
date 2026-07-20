import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - Mi Carrito en Renta")
        self.geometry("800x800")
        self.resizable(False, False)
        self.crear_interfaz_login()  # 3. Creación de los Componentes (Widgets)

    def crear_interfaz_login(self):

        self.lbl_bienvenido = ctk.CTkLabel(self,
        text="TITULO GENERAL DEL SISTEMA, NOMBRE DE LA EMPRESA ", 
        font=ctk.CTkFont(size=30, weight="bold")
        )
        self.lbl_bienvenido.pack(pady=(40, 20))
        
        self.lbl_rol = ctk.CTkLabel(self,
        text="MENU GENERAL DEL SISTEMA", font=ctk.CTkFont(size=30, weight="bold")
        )
        self.lbl_rol.pack(pady=(25, 5), padx=30, anchor="w")
        
        # ---------------------------------------- CONTENEDOR CENTRAL (FRAME) ---
        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.pack(pady=10, padx=30, fill="both", expand=True)
        # ----------------------------------------------------------------------

        self.btn_agregar = ctk.CTkButton(
            self.frame_login,  
            text=" Renta de autos", 
            width=300,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            # command=self.procesar_login
        )
        self.btn_agregar.pack(pady=(40, 20))

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
    def cerrar_sesion(self):
            self.destroy()  # Destruye el Dashboard

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()


