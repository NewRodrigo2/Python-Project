
import customtkinter as ctk
class renta:
    def __init__(self, root, logic, encabezado_frame):
        self.root = root
        self.logic = logic
        self.encabezado_frame = encabezado_frame
        self.frame_renta = None
        self._presupuesto_regreso_entrada = None
 
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
            state="disabled")                   # borre la , despues de "disabled",
        self.btn_confirmar_regreso.grid(
            row=6, column=2, columnspan=2, padx=10, pady=10, sticky="ew")

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

    def limpiar_encabezado(self):
        if self.encabezado_frame:
            for widget in self.encabezado_frame.winfo_children():
                widget.destroy()

    def cerrar_frame_renta(self):
        if self.frame_renta:
            self.frame_renta.destroy()
            self.frame_renta = None

        self.root.frames.crear_menu_principal()
        self.root.logic.aplicar_permisos(self.root.frames)

if __name__ == "__main__":
    import customtkinter as ctk
    from logic import Logic  # ejemplo de tu controlador

    root = ctk.CTk()
    logic = Logic()
    encabezado = ctk.CTkFrame(root)
    encabezado.pack()

    renta_app = renta(root, logic, encabezado)
    renta_app.interfaz_renta()

    root.mainloop()
           
