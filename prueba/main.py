import customtkinter as ctk

# Configuración del tema visual
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue") 

class AppControlPersonal(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la Ventana Principal
        self.title("Sistema de Control de Personal")
        self.geometry("600x400")
        self.resizable(False, False) 

        # Componentes de la Interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        # Título
        self.lbl_titulo = ctk.CTkLabel(
            self, 
            text="Control de Personal", 
            font=ctk.CTkFont(size=22, weight="bold")
        )
        self.lbl_titulo.pack(pady=20)

        # Contenedor (Frame)
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=10, padx=30, fill="both", expand=True)

        # Campo: Nombre
        self.lbl_nombre = ctk.CTkLabel(self.frame, text="Nombre del Empleado:")
        self.lbl_nombre.grid(row=0, column=0, padx=20, pady=15, sticky="w")

        self.txt_nombre = ctk.CTkEntry(self.frame, width=200, placeholder_text="Ej. Juan Pérez")
        self.txt_nombre.grid(row=0, column=1, padx=20, pady=15)

        # Campo: Puesto
        self.lbl_puesto = ctk.CTkLabel(self.frame, text="Puesto / Cargo:")
        self.lbl_puesto.grid(row=1, column=0, padx=20, pady=15, sticky="w")

        self.txt_puesto = ctk.CTkEntry(self.frame, width=200, placeholder_text="Ej. Administrador")
        self.txt_puesto.grid(row=1, column=1, padx=20, pady=15)

        # Botón Guardar
        self.btn_registrar = ctk.CTkButton(
            self.frame, 
            text="Registrar Empleado", 
            command=self.registrar_empleado
        )
        self.btn_registrar.grid(row=2, column=0, columnspan=2, pady=25)

    def registrar_empleado(self):
        nombre = self.txt_nombre.get()
        puesto = self.txt_puesto.get()
        
        # Muestra el resultado en tu terminal para validar que funciona
        print(f"[NUEVO REGISTRO] Empleado: {nombre} | Puesto: {puesto}")
        
        # Limpia las cajas de texto
        self.txt_nombre.delete(0, 'end')
        self.txt_puesto.delete(0, 'end')

if __name__ == "__main__":
    app = AppControlPersonal()
    app.mainloop()
