# Memoria dinámica optimizada


## AuthManager (línea 26)
- __init__ (línea 27) → inicializa atributos principales
  - Atributo: self.archivo_personal (línea 28)
- validar_usuario (línea 30) → acción definida
  - Atributo: with open(self.archivo_personal, "r", encoding (línea 33)
- Usa open (línea 33) → lectura/escritura de archivos
- Usa json.load (línea 34) → carga datos

## RoleManager (línea 61)
- __init__ (línea 62) → inicializa atributos principales
  - Atributo: self.archivo_personal (línea 63)
  - Atributo: self.roles (línea 66)
  - Atributo: self.permisos (línea 69)
- obtener_roles (línea 77) → acción definida
- aplicar_permisos (línea 81) → acción definida

## HRManager (línea 101)
- __init__ (línea 102) → inicializa atributos principales
  - Atributo: self.archivo_personal (línea 103)

## InventoryManager (línea 109)
- __init__ (línea 110) → inicializa atributos principales
  - Atributo: self.archivo_datos (línea 111)
  - Atributo: self.carpeta_datos (línea 112)
  - Atributo: self.ARCHIVO_CONTROL (línea 113)
  - Atributo: self.INVENTARIO_DEFECTO (línea 115)
  - Atributo: self.AUTO_CONTROL (línea 121)
- cargar_inventario (línea 135) → acción definida
  - Atributo: with open(self.archivo_datos, "r", encoding (línea 142)
- Usa open (línea 142) → lectura/escritura de archivos
  - Atributo: self.inventario (línea 143)
- Usa json.load (línea 143) → carga datos
  - Atributo: self.inventario (línea 145)
  - Atributo: self.inventario (línea 147)
- guardar_inventario (línea 150) → acción definida
  - Atributo: with open(self.archivo_datos, "w", encoding (línea 151)
  - Atributo: json.dump(self.inventario, archivo, indent (línea 152)
- Usa json.dump (línea 152) → guarda datos
- verificar_control (línea 154) → acción definida
  - Atributo: with open(self.ARCHIVO_CONTROL, "r", encoding (línea 158)
- guarda_control (línea 167) → acción definida
  - Atributo: datos (línea 169)
- obtener_autos_disponibles (línea 174) → acción definida
- obtener_autos_rentados (línea 179) → acción definida
- procesar_renta (línea 184) → acción definida
- calcular_presupuesto_regreso (línea 206) → acción definida
  - Atributo: (a for a in self.inventario if int(a["id"]) (línea 222)
- procesar_regreso (línea 234) → acción definida
  - Atributo: presupuesto, mensaje (línea 236)
  - Atributo: with open(self.ARCHIVO_CONTROL, "r", encoding (línea 265)
- calcular_precio (línea 288) → acción definida
  - Atributo: auto (línea 292)

## RentalManager (línea 302)
- __init__ (línea 304) → inicializa atributos principales
  - Atributo: self.inventario (línea 305)
- calcular_precio_renta (línea 307) → acción definida
  - Atributo: total (línea 313)
- calcular_presupuesto_regreso (línea 320) → acción definida
- confirmar_regreso_auto (línea 332) → acción definida
- confirmar_renta_auto (línea 344) → acción definida

## MaintenanceManager (línea 357)
- __init__ (línea 358) → inicializa atributos principales
  - Atributo: self.archivo_mantenimiento (línea 359)