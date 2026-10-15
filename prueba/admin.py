
class admin:
    def __init__(self, root, logic, encabezado_frame):
        self.root = root
        self.logic = logic
        self.encabezado_frame = encabezado_frame

        self.frame_botones = ctk.CTkFrame(self.root)

        self.frame_rh = ctk.CTkFrame(self.root)
        self.frame_autos = ctk.CTkFrame(self.root)
        self.frame_financieros = ctk.CTkFrame(self.root)
        self.frame_admon = ctk.CTkFrame(self.root)
        

    def menu_admin(self):    

        self.limpiar_encabezado()


        # encabezados
        lbl_rh = ctk.CTkLabel(self.encabezado_frame, 
            text="RECURSOS HUMANOS",font=ctk.CTkFont(size=15, weight="bold"))
        lbl_autos = ctk.CTkLabel(self.encabezado_frame, 
             text="AUTOS",font=ctk.CTkFont(size=15, weight="bold"))
        lbl_financieros = ctk.CTkLabel(self.encabezado_frame, 
             text="FINANCIEROS",font=ctk.CTkFont(size=15, weight="bold"))
        lbl_admon = ctk.CTkLabel(self.encabezado_frame, 
             text="ADMINISTRACION",font=ctk.CTkFont(size=15, weight="bold"))
        btn_salir = ctk.CTkButton(self.encabezado_frame,
            text="SALIR", command=self.salir)                         

        lbl_rh.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        lbl_autos.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        lbl_financieros.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        lbl_admon.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        btn_salir.grid(row=0, column=4, padx=5, pady=5, sticky="ew")

        self.frame_botones.grid(row=1, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")

        # primera linea de botones
        self.btn_alta_rh = ctk.CTkButton(self.frame_botones,
            text="ALTAS DE PERSONAL", command=self.alta_rh)
        self.btn_rep_autos = ctk.CTkButton(self.frame_botones,
            text="REPORTE DE AUTOS", command=self.rep_autos)
        self.btn_gastos = ctk.CTkButton(self.frame_botones,
            text="GASTOS", command=self.gastos)
        self.btn_rep_autos_ejecutivo = ctk.CTkButton(self.frame_botones,
            text="REPORTE EJECUTIVO", command=self.rep_auto_eje)

        # segunda linea de botones
        self.btn_baja_rh = ctk.CTkButton(self.frame_botones,
            text="BAJA DE PERSONAL", command=self.baja_rh)
        self.btn_alta_autos = ctk.CTkButton(self.frame_botones,
            text="ALTA DE AUTOS", command=self.alta_autos)
        self.btn_balance = ctk.CTkButton(self.frame_botones, 
            text="BALANCE", command=self.balance)
        self.btn_rep_gastos_ejecutivo = ctk.CTkButton(self.frame_botones, 
            text="REPORTE DE GASTOS", command=self.rep_gastos_eje)

        # tercer linea de botones
        self.btn_nomina = ctk.CTkButton(self.frame_botones,
            text="NOMINA", command=self.nomina)
        self.btn_bajas_autos = ctk.CTkButton(self.frame_botones,
            text=" BAJAS DE AUTOS", command=self.baja_auto)

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

    def alta_rh(self):
        self.mostrar_frame_rh()
        # colocar todos los entry para agregar al personal.json
        
    def baja_rh(self):
        self.mostrar_frame_rh()
        # colocar todos los entry para borrar del personal.json
        
    def nomina(self):
        self.mostrar_frame_rh()
        # colocar todos los entry para actualizar al personal.json
        # llamar metodo para generar el informe nomina.txt
        
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
        self.frame_rh.grid(row=4, column=0, columnspan=4,
                        padx=20, pady=10, sticky="nsew")


    def mostrar_frame_autos(self):
        self.ocultar_secciones()
        self.frame_autos.grid(row=4, column=0, columnspan=4,
                            padx=20, pady=10, sticky="nsew")


    def mostrar_frame_financieros(self):
        self.ocultar_secciones()
        self.frame_financieros.grid(row=4, column=0, columnspan=4,
                                    padx=20, pady=10, sticky="nsew")


    def mostrar_frame_admon(self):
        self.ocultar_secciones()
        self.frame_admon.grid(row=4, column=0, columnspan=4,
                            padx=20, pady=10, sticky="nsew")

    def salir(self):
        None     
