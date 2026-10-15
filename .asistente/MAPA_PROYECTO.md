# Mapa del proyecto Python

Generado: 2026-10-15

> Inventario de navegación actualizado con los archivos fuente disponibles. Las ubicaciones se deben confirmar en el código antes de usarlas, pues cambian con las ediciones. Los mapas dentro de `mapas/` son referencias históricas.

## Estructura

- `prueba/`: aplicación de renta de vehículos en Python. Su entrada es `main.py`; contiene 11 archivos Python de aplicación.
- `mapas/`: analizadores AST y salidas históricas; no representan necesariamente el estado actual.
- `.asistente/`: memoria, mapa y notas de estado del proyecto.
- `requirements.txt`: dependencias declaradas.
- `iniciar_asistente.bat`: lanzador auxiliar; inspeccionar antes de ejecutar.
- `.vscode/`, `venv/`: configuración local y entorno virtual.
- `proyecto/`: directorio de trabajo adicional; confirmar sus contenidos antes de documentar funciones.

## Aplicación `prueba/`

### Flujo principal

`main.py` crea `VentanaLogin` e instancia los gestores de `logic.py`. El login valida las credenciales con `AuthManager`; al tener éxito, abre `LoginApp` de `menu_gral.py` y le pasa el rol y la instancia de `InventoryManager`. `FrameManager` presenta la interfaz; `LogicController` aplica permisos, valida entradas y coordina la lógica de rentas y devoluciones.

### Archivos fuente

- `main.py`: punto de entrada, autenticación e instanciación de gestores.
- `logic.py`: rutas de datos basadas en `Path(__file__).parent / "datos"`; clases `AuthManager`, `RoleManager`, `HRManager`, `InventoryManager`, `RentalManager`, `MaintenanceManager` y `UtilitiesManager`. Incluye operaciones de inventario, renta, devolución y cálculo de presupuesto.
- `menu_gral.py`: interfaz principal (`LoginApp`), menú (`FrameManager`) y coordinador `LogicController`. Importa `renta_autos.renta` para delegar la vista de rentas. Un bloque de métodos antiguos de renta dentro de `FrameManager` está entre comillas triples y no se ejecuta como código.
- `renta_autos.py`: implementación activa de la interfaz de renta y devolución. Muestra presupuesto, habilita confirmación tras una cotización válida y vuelve a comprobar que los campos no hayan cambiado antes de confirmar.
- `menu_admin.py`: interfaz administrativa y captura de personal; delega el alta a `rh.agregar_personal_gui`. Revisar antes de usar: el constructor actual de `DashboardApp` no recibe argumentos, aunque `LogicController.abrir_admin` le pasa `ventana_menu_gral`.
- `admin.py`: funciones administrativas principalmente de consola para altas e informes; usa rutas heredadas y depende de módulos `renta` y `herramientas`. No forma parte del flujo principal de `main.py`; `renta.py` no aparece entre los archivos actuales de `prueba/`.
- `rh.py`: persistencia de personal y alta para interfaz. Conserva rutas dependientes del directorio de trabajo y rutas absolutas heredadas.
- `utilerias.py` y `herramientas.py`: funciones de consola, formato y persistencia heredadas; sus rutas deben comprobarse antes de utilizarlas.
- `menu_renta.py` y `menu_rh.py`: archivos vacíos o casi vacíos en la última inspección; confirmar antes de usarlos.

### Datos de `prueba/datos/`

- `personal.json`: credenciales y datos de personal; el login consulta `nombre`, `id_emp`, `pasword` y `area`.
- `inventario.json`: vehículos, tarifas, disponibilidad, días, kilometraje e importes.
- `control.json`: historial de rentas y devoluciones.
- `mtto.json`: archivo presente pero vacío; el gestor de mantenimiento sigue incompleto.
- `autos_ordenados.txt`: archivo auxiliar de datos/reporte.

`logic.py` resuelve las rutas respecto al directorio del módulo. Algunos módulos antiguos usan `os.getcwd()` o rutas absolutas de otro equipo; comprobar las rutas efectivas antes de modificar persistencia.

### Contratos y estado funcional

- `AuthManager.validar_usuario(usuario, password, rol)` consulta el JSON de personal.
- `RoleManager.obtener_roles()` y `aplicar_permisos(rol)` alimentan selección de rol y permisos.
- `InventoryManager` carga/guarda inventario, lista vehículos disponibles/rentados, procesa rentas, calcula una devolución sin guardar y confirma la devolución actualizando inventario e historial. La renta almacena días pactados; la devolución distingue y guarda días pactados, reales y cobrados.
- `RentalManager.registrar_renta` y `registrar_entrega` existen; confirmar su integración con `InventoryManager` antes de ampliar su uso.
- `HRManager.agregar_personal` y `calcular_nomina` siguen sin implementar (`pass`). La interfaz administrativa llama a `rh.agregar_personal_gui`; el acoplamiento de ventana administrativa tiene una discrepancia de argumentos que debe corregirse antes de dar por funcional esa navegación.
- `MaintenanceManager` y `UtilitiesManager` son estructuras incompletas. Aunque existe `datos/mtto.json` vacío, la nota de `logic.py` pide dejar pendiente la ruta hasta definir el archivo correspondiente.

## Notas de trabajo vigentes

- La memoria pide responder en español y con brevedad; primero explicar el error y luego proponer solución. No generar código salvo solicitud explícita.
- `PROGRESO.md` registra separación entre vista previa y confirmación de devolución, persistencia de días pactados/reales/cobrados y verificación aislada satisfactoria; falta confirmar la interacción completa desde la GUI.
- `PENDIENTES.md` aún pide el botón de confirmación y verificar días al rentar, aunque el código actual ya contiene esos cambios; actualizar esa nota tras confirmar la GUI.
- `ERRORES.md` conserva un error anterior en los argumentos de `calcular_precio`; la interfaz activa en `renta_autos.py` pasa dos valores y su método los recibe. El método homónimo de `FrameManager` está en un bloque comentado de `menu_gral.py`, así que el registro no describe un error vigente confirmado.
- `HRManager` y mantenimiento requieren definición/implementación; las rutas heredadas deben revisarse con cuidado.

## Referencias históricas

Los mapas en `mapas/` son resultados de analizadores anteriores. Las fechas y rutas capturadas allí no se deben tomar como estado actual; leer los módulos fuente de `prueba/` para confirmar cualquier detalle.
