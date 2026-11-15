# Memoria dinámica optimizada


## AuthManager
- __init__ → inicializa atributos principales
- Atributo: self.archivo_personal
- validar_usuario → acción definida
- Atributo: with open(self.archivo_personal, "r", encoding
- Usa open → lectura/escritura de archivos
- Usa json.load → carga datos

## RoleManager
- __init__ → inicializa atributos principales
- Atributo: self.archivo_personal
- Atributo: self.roles
- Atributo: self.permisos
- obtener_roles → acción definida
- aplicar_permisos → acción definida

## HRManager
- __init__ → inicializa atributos principales
- Atributo: self.archivo_personal

## InventoryManager
- __init__ → inicializa atributos principales
- Atributo: self.archivo_datos
- Atributo: self.carpeta_datos
- Atributo: self.ARCHIVO_CONTROL
- Atributo: self.INVENTARIO_DEFECTO
- Atributo: self.AUTO_CONTROL
- cargar_inventario → acción definida
- Atributo: with open(self.archivo_datos, "r", encoding
- Usa open → lectura/escritura de archivos
- Atributo: self.inventario
- Usa json.load → carga datos
- guardar_inventario → acción definida
- Atributo: with open(self.archivo_datos, "w", encoding
- Atributo: json.dump(self.inventario, archivo, indent
- Usa json.dump → guarda datos
- verificar_control → acción definida
- Atributo: with open(self.ARCHIVO_CONTROL, "r", encoding
- guarda_control → acción definida
- Atributo: datos
- obtener_autos_disponibles → acción definida
- obtener_autos_rentados → acción definida
- procesar_renta → acción definida
- calcular_presupuesto_regreso → acción definida
- Atributo: (a for a in self.inventario if int(a["id"])
- procesar_regreso → acción definida
- Atributo: presupuesto, mensaje
- calcular_precio → acción definida
- Atributo: auto

## RentalManager
- __init__ → inicializa atributos principales
- Atributo: self.inventario
- calcular_precio_renta → acción definida
- Atributo: total
- calcular_presupuesto_regreso → acción definida
- confirmar_regreso_auto → acción definida
- confirmar_renta_auto → acción definida

## MaintenanceManager
- __init__ → inicializa atributos principales
- Atributo: self.archivo_mantenimiento