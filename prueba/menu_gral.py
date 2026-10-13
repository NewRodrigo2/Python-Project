''' 
datos necesarios para Copilot:este es mi script menu_gral.py, es el mas actualizado, se realizo un git pull al inicio de la joranada, 
rama activa class_pyton, todos los script , clases , metodos que se importan estan actualizados
ruta de archivos en documentar.txt
Objetivo de la revision: 
Pregunta para Copilot: ninguna

'''

import customtkinter as ctk
from logic import RoleManager, InventoryManager
import menu_admin as m_admin

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class LoginApp(ctk.CTk):
    """Ventana principal del menú general."""
    def __init__(self, rol_usuario, ventana_login, inventory):
        super().__init__()
        self.title("Menu General - Mi Carrito en Renta")
        self.geometry("1000x900")
        self.resizable(False, False)

# Controladores
        self.inventory = inventory
        self.logic = LogicController(rol_usuario, ventana_login, self, self.inventory)
        self.frames = FrameManager(self, self.logic, self.inventory)
        self.inventario = InventoryManager()

# Inicializar interfaz
        self.frames.crear_menu_principal()
        self.logic.aplicar_permisos(self.frames)

class FrameManager:
    """Encargado de crear y manejar los distintos frames."""
    def __init__(self, root, logic, inventory):
        self.root = root
        self.logic = logic
        self.encabezado_frame = None
        self.frame_login = None
        self.frame_renta = None
        self.inventory = inventory

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
            text=f"  MENU GENERAL  {rol_texto}",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.lbl_menu.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

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

#--- Configuración de columnas para que se expandan
        for i in range(5):  # número de columnas
            self.encabezado_frame.grid_columnconfigure(i, weight=1)

#--- Configuración de filas/columnas en la ventana principal
        self.root.grid_rowconfigure(1, weight=1)        # frame principal sí se expande
        self.root.grid_columnconfigure(0, weight=1)

    def interfaz_renta(self):
        self.limpiar_encabezado()
        
        lbl_bienvenido = ctk.CTkLabel(self.encabezado_frame,
            text="GESTION DE RENTAS",
            font=ctk.CTkFont(size=15, weight="bold"))
        lbl_bienvenido.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.frame_renta = ctk.CTkFrame(self.root)
        self.frame_renta.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.btn_entrega = ctk.CTkButton(self.frame_renta, 
            text="ENTREGA DE AUTOS",
            command=self.mostrar_auto)
        self.btn_entrega.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.btn_devolucion = ctk.CTkButton(self.frame_renta, 
            text="REGRESA DE AUTOS",
            command=self.regresa_auto)
        self.btn_devolucion.grid(row=0, column=1, padx=10, pady=10, sticky="ew")        

        self.btn_salir_renta = ctk.CTkButton(self.frame_renta, 
            text="RETURN", 
            command=self.cerrar_frame_renta)
        self.btn_salir_renta.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

    def _limpiar_contenido_renta(self):
        """Limpia los widgets de la vista y conserva los botones de navegación."""
        botones_navegacion = {
            self.btn_entrega,
            self.btn_devolucion,
            self.btn_salir_renta,
        }
        for widget in self.frame_renta.winfo_children():
            if widget not in botones_navegacion:
                widget.destroy()

    def regresa_auto(self):
        self._limpiar_contenido_renta()
        self._presupuesto_regreso_entrada = None
        autos = self.logic.inventario.obtener_autos_rentados()
        tot_autos = len(autos)

        if autos:
            fila = 2
            for auto in autos:
                texto = f"{auto['id']} - {auto['marca']} | {auto['modelo']} | ${auto['precio_dia']} por día"
                lbl_auto = ctk.CTkLabel(self.frame_renta, text=texto, anchor="w")
                lbl_auto.grid(row=fila, column=0, padx=10, pady=5, sticky="w")
                fila += 1
        else:
            lbl_vacio = ctk.CTkLabel(self.frame_renta, text="No hay autos rentados ❌")
            lbl_vacio.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        lbl_total = ctk.CTkLabel(self.frame_renta, text=f"Total de autos rentados: {tot_autos}")
        lbl_id = ctk.CTkLabel(self.frame_renta, text=f"ID DE AUTO A REGRESAR")
        self.ent_id = ctk.CTkEntry(self.frame_renta, width=50)  
        lbl_1 = ctk.CTkLabel(self.frame_renta, text=f"DIAS REALES RENTADOS")
        self.dias_rent = ctk.CTkEntry(self.frame_renta, width=70)
        lbl_2 = ctk.CTkLabel(self.frame_renta, text=f"KILOMETROS RECORRIDOS")
        self.km_rec = ctk.CTkEntry(self.frame_renta, width=70)
        self.lbl_presupuesto_regreso = ctk.CTkLabel(
            self.frame_renta,
            text="PRESUPUESTO ESTIMADO: pendiente de calcular")


        lbl_total.grid(row=0, column=3, padx=10, pady=10, sticky="ew")
        lbl_id.grid(row=1, column=2, padx=10, pady=10, sticky="ew")
        self.ent_id.grid(row=1, column=3, padx=10, pady=10, sticky="e")  
        lbl_1.grid(row=2,column=2, padx=10, pady=10, sticky="ew")
        self.dias_rent.grid(row=2,column=3, padx=10, pady=10, sticky="e")
        lbl_2.grid(row=3,column=2, padx=10, pady=10, sticky="ew")
        self.km_rec.grid(row=3,column=3, padx=10, pady=10, sticky="e")        

#--- Botón para calcular precio
        btn_calcular1 = ctk.CTkButton(
            self.frame_renta, 
            text="Calcular presupuesto", 
            command=lambda: self.calcular_presupuesto_regreso( self.km_rec.get(),self.dias_rent.get(),self.ent_id.get()))
        btn_calcular1.grid(row=5, column=3, padx=10, pady=10, sticky="e")      
        self.lbl_presupuesto_regreso.grid(row=4,column=2, padx=10, pady=10, sticky="ew")

        # La devolución solo se confirma después de calcular una vista previa válida.
        self.btn_confirmar_regreso = ctk.CTkButton(
            self.frame_renta,
            text="Confirmar devolución",
            command=self.confirmar_regreso,
            state="disabled",
        )
        self.btn_confirmar_regreso.grid(
            row=6, column=2, columnspan=2, padx=10, pady=10, sticky="ew"
        )

    def calcular_presupuesto_regreso(self, km_str, dias_str, id_str):
        """Solicita el cálculo al controlador y solo actualiza la etiqueta."""
        presupuesto, mensaje = self.logic.calcular_presupuesto_regreso(
            km_str, dias_str, id_str
        )
        if presupuesto is None:
            self._presupuesto_regreso_entrada = None
            self.lbl_presupuesto_regreso.configure(text=mensaje)
            self.btn_confirmar_regreso.configure(state="disabled")
            return

        # Guardamos los valores cotizados para impedir confirmar un presupuesto desactualizado.
        self._presupuesto_regreso_entrada = (id_str, dias_str, km_str)
        self.lbl_presupuesto_regreso.configure(
            text=f"PRESUPUESTO ESTIMADO: ${presupuesto:.2f}"
        )
        self.btn_confirmar_regreso.configure(state="normal")

    def confirmar_regreso(self):
        """Confirma la devolución con los valores actuales de los campos."""
        valores_actuales = (
            self.ent_id.get(), self.dias_rent.get(), self.km_rec.get()
        )
        if valores_actuales != self._presupuesto_regreso_entrada:
            self.lbl_presupuesto_regreso.configure(
                text="Los campos cambiaron; vuelve a calcular el presupuesto antes de confirmar."
            )
            self.btn_confirmar_regreso.configure(state="disabled")
            return

        exito, mensaje = self.logic.confirmar_regreso_auto(
            *valores_actuales
        )
        if not exito:
            self.lbl_presupuesto_regreso.configure(text=mensaje)
            self.btn_confirmar_regreso.configure(state="disabled")
            return

        # Refrescamos la lista y limpiamos los campos después de guardar la devolución.
        self.regresa_auto()
        self.lbl_presupuesto_regreso.configure(text=mensaje)
        self.btn_confirmar_regreso.configure(state="disabled")

    def mostrar_auto(self):
#--- Limpiar contenido previo en frame_renta
        self._limpiar_contenido_renta()

#--- Obtener autos disponibles desde InventoryManager
        autos = self.logic.inventario.obtener_autos_disponibles()
        tot_autos = len(autos)

        lbl_total = ctk.CTkLabel(self.frame_renta, text=f"Total de autos disponibles: {tot_autos}")
        lbl_total.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

        lbl_id = ctk.CTkLabel(self.frame_renta, text=f"ID DE AUTO A RENTAR")
        lbl_id.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        self.ent_id = ctk.CTkEntry(self.frame_renta, width=50)  
        self.ent_id.grid(row=1, column=3, padx=10, pady=10, sticky="e")  

        lbl_1 = ctk.CTkLabel(self.frame_renta, text=f"DIAS ESTIMADOS POR RENTAR")
        lbl_1.grid(row=2,column=2, padx=10, pady=10, sticky="ew")

        self.ent_1 = ctk.CTkEntry(self.frame_renta, width=70)
        self.ent_1.grid(row=2,column=3, padx=10, pady=10, sticky="e")

#--- Botón para calcular precio
        btn_calcular = ctk.CTkButton(
            self.frame_renta, 
            text="Calcular precio", 
            command=lambda: self.calcular_precio(self.ent_id.get(), self.ent_1.get()))
        btn_calcular.grid(row=4, column=3, padx=10, pady=10, sticky="e")      

        lbl_2 = ctk.CTkLabel(self.frame_renta, text=f"PRESUPUESTO ESTIMADO")
        lbl_2.grid(row=3,column=2, padx=10, pady=10, sticky="ew")

        if autos:
            fila = 2
            for auto in autos:
                texto = f"{auto['id']} - {auto['marca']} | {auto['modelo']} | ${auto['precio_dia']} por día"
                lbl_auto = ctk.CTkLabel(self.frame_renta, text=texto, anchor="w")
                lbl_auto.grid(row=fila, column=0, padx=10, pady=5, sticky="w")
                fila += 1
        else:
            lbl_vacio = ctk.CTkLabel(self.frame_renta, text="No hay autos disponibles ❌")
            lbl_vacio.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
            
#--- mostrar presupuesto  / falta boton acepta renta
    def calcular_precio(self,id_auto_str, dias_str):
            total, mensaje = self.logic.calcular_precio_renta(id_auto_str, dias_str)
            
            if total is not None:
                lbl_total = ctk.CTkLabel(self.frame_renta, text=f"💰 Precio total: ${total}")
                lbl_total.grid(row=6, column=2, columnspan=2, padx=10, pady=10, sticky="ew")

                btn_confirmar = ctk.CTkButton(
                    self.frame_renta, 
                    text="Confirmar renta",
                    command=lambda: self.confirmar_renta(self.ent_id.get(), self.ent_1.get())
                )
                btn_confirmar.grid(row=7, column=2, columnspan=2, padx=10, pady=10, sticky="ew")
            else:
                lbl_error = ctk.CTkLabel(self.frame_renta, text=mensaje)
                lbl_error.grid(row=5, column=2, columnspan=2, padx=10, pady=10, sticky="ew")

    def confirmar_renta(self, id_auto, dias):
        """Confirma la renta y muestra el resultado que devuelve el controlador."""
        exito, mensaje = self.logic.confirmar_renta_auto(id_auto, dias)
        if exito:
            lbl_ok = ctk.CTkLabel(self.frame_renta, text=mensaje)
            lbl_ok.grid(row=8, column=2, columnspan=2, padx=10, pady=10, sticky="ew")
        else:
            lbl_error = ctk.CTkLabel(self.frame_renta, text=mensaje)
            lbl_error.grid(row=5, column=2, columnspan=2, padx=10, pady=10, sticky="ew")

    def cerrar_frame_renta(self):
        if self.frame_renta:
            self.frame_renta.destroy()
            self.crear_menu_principal()    

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

    def cerrar_sesion(self):
        if self.ventana_login:
            self.ventana_principal.destroy()
            self.ventana_login.deiconify()
        else:
            self.ventana_principal.destroy()

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

