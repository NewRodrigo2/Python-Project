import customtkinter as ctk

class admin:
    def __init__(self, root, logic):
        self.root = root
        self.logic = logic

        # CAMBIO: el encabezado administrativo es propio del panel y no modifica
        # los controles ni el encabezado del menú general.
        self.encabezado_frame = ctk.CTkFrame(self.root, fg_color="transparent")

        # CAMBIO: el panel reparte el ancho entre las cuatro columnas del encabezado.
        for columna in range(4):
            self.root.grid_columnconfigure(columna, weight=1)
            self.encabezado_frame.grid_columnconfigure(columna, weight=1)

        # CAMBIO: la sección de contenido puede crecer verticalmente.       
        for fila in range(10):  
            self.root.grid_rowconfigure(fila, weight=1)
  
        self.encabezado_frame.grid(row=0, column=0, columnspan=4, padx=20, pady=10, sticky="ew")
        self.frame_botones = ctk.CTkFrame(self.root)

        # CAMBIO: reparte el ancho del área de botones entre sus cuatro columnas.
        for columna in range(4):
            self.frame_botones.grid_columnconfigure(columna, weight=1)

        self.frame_rh = ctk.CTkFrame(self.root)
        for col in range(6): # filas 0 a 5
            self.frame_rh.grid_columnconfigure(col, weight=1)

        self.frame_autos = ctk.CTkFrame(self.root)
        for col in range(4):
            self.frame_autos.grid_columnconfigure(col, weight=1)

        self.frame_financieros = ctk.CTkFrame(self.root)
        for col in range(4):
            self.frame_financieros.grid_columnconfigure(col, weight=1)

        self.frame_admon = ctk.CTkFrame(self.root)
        for col in range(4):
            self.frame_admon.grid_columnconfigure(col, weight=1)

    def menu_admin(self):    
        # CAMBIO: limpiar únicamente el encabezado administrativo propio.
        for widget in self.encabezado_frame.winfo_children():
            widget.destroy()
        # CAMBIO: evita duplicar botones si menu_admin() se vuelve a ejecutar.
        for widget in self.frame_botones.winfo_children():
            widget.destroy()

        # encabezados
        lbl_rh = ctk.CTkLabel(self.encabezado_frame, 
            text="RECURSOS HUMANOS",font=ctk.CTkFont(size=12, weight="bold"))
        lbl_autos = ctk.CTkLabel(self.encabezado_frame, 
             text="AUTOS",font=ctk.CTkFont(size=12, weight="bold"))
        lbl_financieros = ctk.CTkLabel(self.encabezado_frame, 
             text="FINANCIEROS",font=ctk.CTkFont(size=12, weight="bold"))
        lbl_admon = ctk.CTkLabel(self.encabezado_frame, 
             text="ADMINISTRACION",font=ctk.CTkFont(size=12, weight="bold"))
                         
        lbl_rh.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        lbl_autos.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        lbl_financieros.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        lbl_admon.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        self.frame_botones.grid(row=1, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")

        # primera linea de botones
        self.btn_alta_rh = ctk.CTkButton(self.frame_botones,
            text="ALTAS DE PERSONAL", command=self.alta_rh,font=ctk.CTkFont(size=10))
        self.btn_rep_autos = ctk.CTkButton(self.frame_botones,
            text="REPORTE DE AUTOS", command=self.rep_autos,font=ctk.CTkFont(size=10))
        self.btn_gastos = ctk.CTkButton(self.frame_botones,
            text="GASTOS", command=self.gastos,font=ctk.CTkFont(size=10))
        self.btn_rep_autos_ejecutivo = ctk.CTkButton(self.frame_botones,
            text="REPORTE EJECUTIVO", command=self.rep_auto_eje,font=ctk.CTkFont(size=10))

        # segunda linea de botones
        self.btn_baja_rh = ctk.CTkButton(self.frame_botones,
            text="BAJA DE PERSONAL", command=self.baja_rh,font=ctk.CTkFont(size=10))
        self.btn_alta_autos = ctk.CTkButton(self.frame_botones,
            text="ALTA DE AUTOS", command=self.alta_autos,font=ctk.CTkFont(size=10))
        self.btn_balance = ctk.CTkButton(self.frame_botones, 
            text="BALANCE", command=self.balance,font=ctk.CTkFont(size=10))
        self.btn_rep_gastos_ejecutivo = ctk.CTkButton(self.frame_botones, 
            text="REPORTE DE GASTOS", command=self.rep_gastos_eje,font=ctk.CTkFont(size=10))

        # tercer linea de botones
        self.btn_nomina = ctk.CTkButton(self.frame_botones,
            text="NOMINA", command=self.nomina,font=ctk.CTkFont(size=10))
        self.btn_bajas_autos = ctk.CTkButton(self.frame_botones,
            text=" BAJAS DE AUTOS", command=self.baja_auto)
        btn_salir = ctk.CTkButton(self.frame_botones,
            text="SALIR", command=self.salir,font=ctk.CTkFont(size=15))        

        self.btn_alta_rh.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.btn_rep_autos.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.btn_gastos.grid(row=1, column=2, padx=10, pady=10, sticky="ew")
        self.btn_rep_autos_ejecutivo.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

        self.btn_baja_rh.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.btn_alta_autos.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        self.btn_balance.grid(row=2, column=2, padx=10, pady=10, sticky="ew")
        self.btn_rep_gastos_ejecutivo.grid(row=2, column=3, padx=10, pady=10, sticky="ew")

        self.btn_nomina.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        self.btn_bajas_autos.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        btn_salir.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

    def alta_rh(self):
        self.mostrar_frame_rh()

        lbl_id = ctk.CTkLabel(self.frame_rh, 
            text="Id empleado",font=ctk.CTkFont(size=12, weight="bold"))       
        lbl_nom = ctk.CTkLabel(self.frame_rh, 
            text="Nombre",font=ctk.CTkFont(size=12, weight="bold"))
        lbl_area = ctk.CTkLabel(self.frame_rh, 
            text="Area",font=ctk.CTkFont(size=12, weight="bold"))        
        lbl_hr_cont = ctk.CTkLabel(self.frame_rh, 
            text="Hr Contratadas",font=ctk.CTkFont(size=12, weight="bold"))
        lbl_hr_trab = ctk.CTkLabel(self.frame_rh, 
            text="Hr Trabajadas",font=ctk.CTkFont(size=12, weight="bold"))
        lbl_sueldo = ctk.CTkLabel(self.frame_rh, 
            text="Sueldo",font=ctk.CTkFont(size=12, weight="bold"))
        lbl_usen = ctk.CTkLabel(self.frame_rh, 
            text="Ausencias",font=ctk.CTkFont(size=12, weight="bold"))        
        lbl_pw = ctk.CTkLabel(self.frame_rh, 
            text="Password",font=ctk.CTkFont(size=12, weight="bold"))
        
        lbl_id.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        lbl_nom.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        lbl_area.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        lbl_hr_cont.grid(row=1, column=3, padx=5, pady=5, sticky="ew")
        lbl_hr_trab.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        lbl_sueldo.grid(row=2, column=3, padx=5, pady=5, sticky="ew")
        lbl_usen.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        lbl_pw.grid(row=3, column=3, padx=5, pady=5, sticky="ew")

        self.Entry_id = ctk.CTkEntry(self.frame_rh, 
            font=ctk.CTkFont(size=12, weight="bold"))       
        self.Entry_nom = ctk.CTkEntry(self.frame_rh, 
            font=ctk.CTkFont(size=12, weight="bold"))
        self.Entry_area = ctk.CTkEntry(self.frame_rh, 
            font=ctk.CTkFont(size=12, weight="bold"))        
        self.Entry_hr_cont = ctk.CTkEntry(self.frame_rh, 
            font=ctk.CTkFont(size=12, weight="bold"))
        self.Entry_hr_trab = ctk.CTkEntry(self.frame_rh, 
            font=ctk.CTkFont(size=12, weight="bold"))
        self.Entry_sueldo = ctk.CTkEntry(self.frame_rh, 
            font=ctk.CTkFont(size=12, weight="bold"))
        self.Entry_usen = ctk.CTkEntry(self.frame_rh, 
            font=ctk.CTkFont(size=12, weight="bold"))        
        self.Entry_pw = ctk.CTkEntry(self.frame_rh, 
            font=ctk.CTkFont(size=12, weight="bold"))  

        self.Entry_id.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.Entry_nom.grid(row=0, column=4, columnspan=3, padx=5, pady=5, sticky="ew")
        self.Entry_area.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.Entry_hr_cont.grid(row=1, column=4, padx=5, pady=5, sticky="ew")
        self.Entry_hr_trab.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.Entry_sueldo.grid(row=2, column=4, padx=5, pady=5, sticky="ew")
        self.Entry_usen.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        self.Entry_pw.grid(row=3, column=4, padx=5, pady=5, sticky="ew")
                            
        
        btn_guardar = ctk.CTkButton(
            self.frame_rh,
            text="GUARDAR",
            font=ctk.CTkFont(size=15)
            # command=self.salir  # Sin command, el botón no realiza ninguna acción.
        )

        btn_salir = ctk.CTkButton(
            self.frame_rh,
            text="SALIR",
            font=ctk.CTkFont(size=15)
            # command=self.salir  # Sin command, el botón no realiza ninguna acción.
        )

        btn_guardar.grid(row=5, column=3, padx=10, pady=10, sticky="ew")
        btn_salir.grid(row=5, column=6, padx=10, pady=10, sticky="ew")
        
    def baja_rh(self):
        self.mostrar_frame_rh()
        # colocar todos los entry para borrar del personal.json
        
    def nomina(self):
        self.mostrar_frame_rh()

        lbl_mes_nomina = ctk.CTkLabel(self.frame_rh, 
            text="Genera Nomina del mes",font=ctk.CTkFont(size=12, weight="bold"))
        lbl_mes_nomina.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        self.Entry_mes_nomina = ctk.CTkEntry(self.frame_rh, 
            font=ctk.CTkFont(size=12, weight="bold"))
        self.Entry_mes_nomina.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        btn_generar = ctk.CTkButton(
                self.frame_rh,
                text="GENERAR",
                font=ctk.CTkFont(size=15)
                # command=self.salir  # Sin command, el botón no realiza ninguna acción.
            )

        btn_salir = ctk.CTkButton(
            self.frame_rh,
            text="SALIR",
            font=ctk.CTkFont(size=15)
            # command=self.salir  # Sin command, el botón no realiza ninguna acción.
        )

        btn_generar.grid(row=5, column=3, padx=10, pady=10, sticky="ew")
        btn_salir.grid(row=5, column=6, padx=10, pady=10, sticky="ew")        

        
    def rep_autos(self):
        self.mostrar_frame_autos()
        # colocar todos los entry para solicitar de que mes se quiere el reporte y 
        # generar archivo informe.txt
        
    def alta_autos(self):
        self.mostrar_frame_autos()
        # colocar todos los entry para agregar un auto nuevo a inventario.json
        
    def baja_auto(self):
        self.mostrar_frame_autos()
        # colocar el entry id para dar de baja el auto 
        # mostrar los datos del auto
        
    def gastos(self):
        self.mostrar_frame_financieros()
        # colocar todos los entry para capturar facturas y agregar al gastos.json
        
    def balance(self):
        self.mostrar_frame_financieros()
        # colocar todos el entry para solicitar de que mes se quiere el reporte y 
        # generar archivo balance.txt
        # ejecutar metodo con las operaciones matematicas necesarias
        
    def rep_auto_eje(self):
        self.mostrar_frame_admon()
        # colocar todos el entry para solicitar de que mes se quiere el reporte y 
        # generar archivo balance.txt
        # ejecutar metodo con las operaciones matematicas necesarias
        
    def rep_gastos_eje(self):
        self.mostrar_frame_admon()
        # colocar todos el entry para solicitar de que mes se quiere el reporte y 
        # generar archivo balance.txt
        # ejecutar metodo con las operaciones matematicas necesarias
            
   
    def ocultar_secciones(self):
        secciones = [
            self.frame_rh,
            self.frame_autos,
            self.frame_financieros,
            self.frame_admon
        ]

        for frame in secciones:
            if frame.winfo_manager() == "grid":
                frame.grid_remove()

    def mostrar_frame_rh(self):
        self.ocultar_secciones()
        self.frame_rh.grid(row=3, column=0, columnspan=4,
                        padx=20, pady=10, sticky="nsew")

    def mostrar_frame_autos(self):
        self.ocultar_secciones()
        self.frame_autos.grid(row=3, column=0, columnspan=4,
                            padx=20, pady=10, sticky="nsew")

    def mostrar_frame_financieros(self):
        self.ocultar_secciones()
        self.frame_financieros.grid(row=3, column=0, columnspan=4,
                                    padx=20, pady=10, sticky="nsew")

    def mostrar_frame_admon(self):
        self.ocultar_secciones()
        self.frame_admon.grid(row=3, column=0, columnspan=4,
                            padx=20, pady=10, sticky="nsew")

    def salir(self):
        # CAMBIO: restaura el menú general conservado en FrameManager.
        self.logic.frames.regresar_menu_principal()
