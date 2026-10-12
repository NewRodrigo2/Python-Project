# Mapa del proyecto Python

Generado: 2026-10-11 20:24:03

Archivos Python encontrados: 15

> Inventario estático generado desde los archivos actuales. Las líneas indican ubicaciones en el momento de generación; el mapa no confirma el comportamiento en ejecución.

## `mapas/analiza.py`

- Línea 5: **clase** `MethodAnalyzer`
  - Línea 6: **método de MethodAnalyzer** `__init__`
  - Línea 11: **método de MethodAnalyzer** `visit_Call`
  - Línea 19: **método de MethodAnalyzer** `visit_Attribute`
  - Línea 25: **método de MethodAnalyzer** `visit_Return`
- Línea 31: **clase** `ClassAnalyzer`
  - Línea 32: **método de ClassAnalyzer** `__init__`
  - Línea 37: **método de ClassAnalyzer** `visit_FunctionDef`
- Línea 56: **función** `analizar_archivo`
- Línea 75: **función** `analizar_proyecto`

## `mapas/analizaF.py`

- Línea 5: **clase** `MethodAnalyzer`
  - Línea 6: **método de MethodAnalyzer** `__init__`
  - Línea 11: **método de MethodAnalyzer** `visit_Call`
  - Línea 19: **método de MethodAnalyzer** `visit_Attribute`
  - Línea 25: **método de MethodAnalyzer** `visit_Return`
- Línea 31: **clase** `ClassAnalyzer`
  - Línea 32: **método de ClassAnalyzer** `__init__`
  - Línea 37: **método de ClassAnalyzer** `visit_FunctionDef`
- Línea 56: **función** `analizar_archivo`
- Línea 75: **función** `analizar_proyecto`

## `mapas/asistente.py`

- Línea 21: **función** `generar_memoria_optimizada` — Procesa un archivo Python y genera un README.md optimizado:
- Línea 90: **función** `generar_texto` — Genera texto optimizado para el archivo indicado y lo guarda en memoria_optimizada.txt
- Línea 102: **función** `copiar_archivo` — Copia el archivo generado y además mantiene su contenido en el portapapeles.

## `mapas/optimiza.py`

- Línea 5: **función** `generar_memoria_optimizada` — Procesa un archivo Python y genera un README.md optimizado:

## `prueba/admin.py`

- Línea 44: **función** `eliminar_renta_admin`
- Línea 84: **función** `informe_rentas`
- Línea 130: **función** `mostrar_informe`
- Línea 167: **función** `agrega_auto`
- Línea 209: **función** `menu_administrador` — Submenú protegido para agregar vehículos nuevos.

## `prueba/herramientas.py`

- Línea 34: **función** `dibu_enca`
- Línea 41: **función** `limpiar_pantalla`
- Línea 47: **función** `row_space`
- Línea 51: **función** `guardar_inventario` — Guarda el estado actual del inventario en el archivo JSON.
- Línea 61: **función** `guarda_control`

## `prueba/logic.py`

- Línea 32: **clase** `AuthManager`
  - Línea 33: **método de AuthManager** `__init__`
  - Línea 36: **método de AuthManager** `validar_usuario`
- Línea 67: **clase** `RoleManager`
  - Línea 68: **método de RoleManager** `__init__`
  - Línea 83: **método de RoleManager** `obtener_roles` — Devuelve la lista de roles disponibles para la interfaz.
  - Línea 87: **método de RoleManager** `aplicar_permisos` — Devuelve qué acciones están habilitadas según el rol.
- Línea 107: **clase** `HRManager`
  - Línea 108: **método de HRManager** `__init__`
  - Línea 112: **método de HRManager** `agregar_personal` — Agrega nuevo personal al archivo JSON.
  - Línea 116: **método de HRManager** `calcular_nomina` — Calcula la nómina del personal registrado.
- Línea 124: **clase** `InventoryManager`
  - Línea 125: **método de InventoryManager** `__init__`
  - Línea 150: **método de InventoryManager** `cargar_inventario` — Lee el inventario.json o carga los valores por defecto si no existe.
  - Línea 165: **método de InventoryManager** `guardar_inventario`
  - Línea 169: **método de InventoryManager** `verificar_control` — Verifica que control.json no esté vacío; si lo está, agrega la lista por defecto.
  - Línea 182: **método de InventoryManager** `guarda_control`
  - Línea 189: **método de InventoryManager** `obtener_autos_disponibles`
  - Línea 194: **método de InventoryManager** `obtener_autos_rentados`
  - Línea 199: **método de InventoryManager** `procesar_renta`
  - Línea 221: **método de InventoryManager** `calcular_presupuesto_regreso` — Calcula el cobro de una devolución sin modificar ni guardar el inventario.
  - Línea 249: **método de InventoryManager** `procesar_regreso` — Confirma una devolución, actualiza inventario y agrega su registro de control.
  - Línea 303: **método de InventoryManager** `calcular_precio`
- Línea 317: **clase** `RentalManager`
  - Línea 318: **método de RentalManager** `__init__`
  - Línea 321: **método de RentalManager** `registrar_renta` — Registra una nueva renta.
  - Línea 325: **método de RentalManager** `registrar_entrega` — Registra la entrega de un auto rentado.
- Línea 333: **clase** `MaintenanceManager`
  - Línea 334: **método de MaintenanceManager** `__init__`
  - Línea 337: **método de MaintenanceManager** `registrar_mantenimiento` — Registra un mantenimiento realizado.
- Línea 345: **clase** `UtilitiesManager`
  - Línea 346: **método de UtilitiesManager** `__init__`
  - Línea 349: **método de UtilitiesManager** `generar_reporte_general` — Genera un reporte general del sistema.

## `prueba/main.py`

- Línea 39: **clase** `VentanaLogin`
  - Línea 40: **método de VentanaLogin** `__init__`
  - Línea 56: **método de VentanaLogin** `crear_interfaz_login`
  - Línea 125: **método de VentanaLogin** `procesar_login`
  - Línea 146: **método de VentanaLogin** `salir_definitivo` — Termina el mainloop y destruye la ventana tras la animación del click.

## `prueba/menu_admin.py`

- Línea 26: **clase** `DashboardApp`
  - Línea 27: **método de DashboardApp** `__init__`
  - Línea 40: **método de DashboardApp** `crear_interfaz_login`
  - Línea 81: **método de DashboardApp** `rec_hum`
  - Línea 119: **método de DashboardApp** `rh_frame`
  - Línea 195: **método de DashboardApp** `graba_dato`
  - Línea 226: **método de DashboardApp** `limpiar_formulario` — Limpia los campos tras una grabación exitosa.
  - Línea 235: **método de DashboardApp** `mostrar_menu_principal`
  - Línea 240: **método de DashboardApp** `mostrar_frame_segundo`
  - Línea 247: **método de DashboardApp** `cerrar_sesion`

## `prueba/menu_gral.py`

- Línea 17: **clase** `LoginApp` — Ventana principal del menú general.
  - Línea 19: **método de LoginApp** `__init__`
- Línea 35: **clase** `FrameManager` — Encargado de crear y manejar los distintos frames.
  - Línea 37: **método de FrameManager** `__init__`
  - Línea 45: **método de FrameManager** `limpiar_encabezado`
  - Línea 50: **método de FrameManager** `crear_menu_principal`
  - Línea 97: **método de FrameManager** `interfaz_renta`
  - Línea 123: **método de FrameManager** `_limpiar_contenido_renta` — Limpia los widgets de la vista y conserva los botones de navegación.
  - Línea 134: **método de FrameManager** `regresa_auto`
  - Línea 191: **método de FrameManager** `calcular_presupuesto_regreso` — Solicita el cálculo al controlador y solo actualiza la etiqueta.
  - Línea 209: **método de FrameManager** `confirmar_regreso` — Confirma la devolución con los valores actuales de los campos.
  - Línea 234: **método de FrameManager** `mostrar_auto`
  - Línea 279: **método de FrameManager** `calcular_precio`
  - Línea 297: **método de FrameManager** `confirmar_renta` — Confirma la renta y muestra el resultado que devuelve el controlador.
  - Línea 308: **método de FrameManager** `mostrar_auto1`
  - Línea 314: **método de FrameManager** `cerrar_frame_renta`
- Línea 319: **clase** `LogicController` — Encargado de la lógica de permisos y navegación.
  - Línea 321: **método de LogicController** `__init__`
  - Línea 328: **método de LogicController** `aplicar_permisos`
  - Línea 343: **método de LogicController** `abrir_admin`
  - Línea 351: **método de LogicController** `regresar_desde_admin`
  - Línea 356: **método de LogicController** `cerrar_sesion`
  - Línea 363: **método de LogicController** `calcular_precio_renta`
  - Línea 376: **método de LogicController** `calcular_presupuesto_regreso`
  - Línea 389: **método de LogicController** `confirmar_regreso_auto` — Valida los campos y delega el guardado de la devolución al inventario.
  - Línea 402: **método de LogicController** `confirmar_renta_auto` — Valida los campos y devuelve el resultado real de procesar la renta.

## `prueba/menu_renta.py`

- No se detectaron clases ni funciones de nivel superior.

## `prueba/menu_rh.py`

- No se detectaron clases ni funciones de nivel superior.

## `prueba/renta.py`

- Línea 70: **función** `cargar_inventario` — Lee los archivos JSON de inventario y control. Si no existen, los crea.
- Línea 112: **función** `mostrar_inventario`
- Línea 122: **función** `mostrar_inv_disp`
- Línea 137: **función** `mostrar_inv_no_disp`
- Línea 158: **función** `rentar_auto`
- Línea 192: **función** `regresar_auto`
- Línea 288: **función** `menu_principal`

## `prueba/rh.py`

- Línea 20: **función** `guardar_inventario_personal` — Guarda la lista de empleados en el archivo JSON.
- Línea 31: **función** `abre_inventario_personal` — Carga los empleados del archivo JSON si existe.
- Línea 44: **función** `agregar_personal_gui` — Función optimizada para la Interfaz Gráfica (Tkinter).

## `prueba/utilerias.py`

- Línea 62: **función** `guardar_inventario_personal` — Guarda el estado actual del inventario en el archivo JSON.
- Línea 71: **función** `abre_inventario_personal`
- Línea 83: **función** `agregar_personal`
- Línea 135: **función** `menu_util`
