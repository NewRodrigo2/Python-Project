import customtkinter as ctk
import renta as rta

# 1. Configuración estética de CustomTkinter
ctk.set_appearance_mode("Dark")  # Forzamos un modo oscuro muy elegante
ctk.set_default_color_theme("blue") 

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 2. Configuración de la Ventana de Login
        self.title("Acceso al Sistema - Mi Carrito en Renta")
        self.geometry("450x550")
        self.resizable(False, False)

        # 3. Creación de los Componentes (Widgets)
        self.crear_interfaz_login()

    def crear_interfaz_login(self):
        # --- TÍTULO PRINCIPAL ---
        self.lbl_bienvenido = ctk.CTkLabel(
            self, 
            text="INICIAR SESIÓN", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.lbl_bienvenido.pack(pady=(40, 20))

        # --- CONTENEDOR CENTRAL (FRAME) ---
        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.pack(pady=10, padx=30, fill="both", expand=True)

        # --- SELECCIÓN DE ROL / PUESTO ---
        self.lbl_rol = ctk.CTkLabel(
            self.frame_login,  # <-- DEBE DECIR self.frame_login
            text="Seleccione su Tipo de Personal:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.lbl_rol.pack(pady=(25, 5), padx=30, anchor="w")

        self.roles_disponibles = ["Mostrador", "Financieros", "Mecánico", "Administrador", "Supervisor"]
        self.cmb_rol = ctk.CTkComboBox(
            self.frame_login,  # <-- DEBE DECIR self.frame_login
            values=self.roles_disponibles,
            width=320,
            state="readonly"
        )
        self.cmb_rol.set("Mostrador")
        self.cmb_rol.pack(pady=5, padx=30)

        # --- CAMPO: USUARIO ---
        self.lbl_usuario = ctk.CTkLabel(
            self.frame_login,  # <-- DEBE DECIR self.frame_login
            text="Nombre de Usuario o ID:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.lbl_usuario.pack(pady=(20, 5), padx=30, anchor="w")

        self.txt_usuario = ctk.CTkEntry(
            self.frame_login,  # <-- DEBE DECIR self.frame_login
            width=320, 
            placeholder_text="Ej. juan.perez"
        )
        self.txt_usuario.pack(pady=5, padx=30)

        # --- CAMPO: CONTRASEÑA ---
        self.lbl_password = ctk.CTkLabel(
            self.frame_login,  # <-- DEBE DECIR self.frame_login
            text="Contraseña:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.lbl_password.pack(pady=(20, 5), padx=30, anchor="w")

        self.txt_password = ctk.CTkEntry(
            self.frame_login,  # <-- DEBE DECIR self.frame_login
            width=320, 
            placeholder_text="••••••••", 
            show="•"
        )
        self.txt_password.pack(pady=5, padx=30)

        # --- BOTÓN DE ENTRADA ---
        self.btn_ingresar = ctk.CTkButton(
            self.frame_login,  # <-- DEBE DECIR self.frame_login
            text="Ingresar al Sistema", 
            width=200,
            height=40,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self.procesar_login
        )
        self.btn_ingresar.pack(pady=(40, 20))


    # 4. Lógica del Botón
    def procesar_login(self):
        rol_seleccionado = self.cmb_rol.get()
        usuario = self.txt_usuario.get()
        password = self.txt_password.get()

        # [Validación Temporal en Consola]
        print(f"\n[INTENTO DE LOGIN]")
        print(f"Rol: {rol_seleccionado} | Usuario: {usuario} | Clave: {password}")

        # Aquí es donde en la siguiente clase llamaremos a tus otros scripts para validar
        # Ejemplo provisional de bienvenida:
        if usuario != "" and password != "":
            print(f"¡Acceso Concedido como {rol_seleccionado}!")
            # Limpiamos los campos
            self.txt_usuario.delete(0, 'end')
            self.txt_password.delete(0, 'end')
        else:
            print("Error: Campos vacíos")
        if rol_seleccionado ==  "Mostrador":
            rta.menu_principal()

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
