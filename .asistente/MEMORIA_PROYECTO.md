# Memoria del proyecto para asistentes de IA

Última revisión: 2026-10-15.

## Propósito

Proyecto personal de autoaprendizaje de programación. Cambia con frecuencia y se desarrolla con apoyo de IA y documentación oficial.

## Estructura conocida

- `prueba/`: aplicación de consola para renta de vehículos y funciones relacionadas con personal, inventario, roles y administración. El punto de entrada aparente es `prueba/main.py`; confirmar siempre leyendo el archivo actual.
- `prueba/logic.py`: clases de lógica de negocio; consultar el mapa y el archivo actual para confirmar nombres y responsabilidades.
- `android_happy_face/`: pequeño proyecto Android/Kivy que dibuja y anima una cara; revisar `BUILD_INSTRUCTIONS.txt` antes de modificar o ejecutar su proceso de construcción.
- `mapas/`: analizadores AST anteriores y mapas históricos. Son referencias, no la fuente actual del código.
- `auto_pr_script.py`: automatización relacionada con creación y manejo de Pull Requests; inspeccionar antes de ejecutarla porque puede interactuar con GitHub.
- `pba_codigo.py`: ejercicios de Python.
- `requirements.txt`: dependencias Python declaradas del proyecto.

## Memoria y mapa

- `MAPA_PROYECTO.md` resume archivos Python, clases, funciones, métodos y docstrings detectados mediante análisis AST. No demuestra el comportamiento en ejecución ni detecta todas las relaciones entre objetos.
- El mapa se regeneró el 2026-10-13 y está modificado en el árbol de trabajo; revisar ese cambio antes de reemplazarlo. Puede quedar desactualizado después de cambios en los archivos Python; para preguntas sobre el estado actual, verificar el código fuente pertinente y actualizar el mapa cuando corresponda.
- `PROGRESO.md`, `PENDIENTES.md` y `ERRORES.md` registran el estado de trabajo; actualizar estas notas cuando cambie el estado confirmado.
- Los archivos `mapas/PROJECT_MAP_*.txt` son instantáneas históricas. En particular, `PROJECT_MAP_FUNC_20260927_200356.txt` cubre la carpeta `prueba/`, no todo el proyecto ni el estado actual.

## Reglas para futuras sesiones

1. Leer esta memoria y las notas recientes antes de responder sobre el proyecto.
2. Para hechos actuales, comprobar `MAPA_PROYECTO.md` y leer los `.py` relevantes; no confiar en mapas antiguos si difieren del código.
3. Preferencia del usuario: explicar primero el error y la propuesta de solución sin generar código; crear código solo cuando lo solicite, y ejemplos extra solo si los pide. Responder en español y con brevedad.

## Límites de esta memoria

Este documento es un resumen de navegación, no una copia del código ni memoria automática del modelo. Puede quedar desactualizado; validar los detalles consultando el proyecto actual.

## Ruta raíz y acceso de archivos

- La raíz del proyecto es C:\Users\Rodrigo\Documents\GitHub\Python-Project; la carpeta prueba/ es solo uno de sus subdirectorios.
- En cada sesión, el acceso de la IA depende de las carpetas y permisos que el entorno de Codex tenga habilitados. No asumir que una sesión en otra computadora u oficina tiene el mismo acceso de escritura.
- Antes de concluir que una nota del proyecto no existe, comprobar la raíz Python-Project y sus subdirectorios relevantes.

## Estado confirmado de `prueba/` (2026-10-15)

- En `menu_gral.py` ya están conectados el cálculo previo y la confirmación de devolución. `LogicController` delega la confirmación a `InventoryManager.procesar_regreso`.
- `InventoryManager.procesar_renta` guarda los días pactados; `procesar_regreso` actualiza disponibilidad, días reales/pactados/cobrados, kilometraje, venta e historial en `control.json`.
- La verificación aislada está documentada en `PROGRESO.md`; aún falta confirmar el flujo completo desde la GUI.
- `PENDIENTES.md` aún enumera como pendientes el botón de confirmación y la persistencia de días, pero ambos aparecen implementados en el código actual. Actualizar esa nota cuando se realice la verificación GUI.
- `ERRORES.md` conserva un error previo sobre los argumentos de `calcular_precio`; ya no coincide con `menu_gral.py` actual, donde la lambda y el método aceptan los dos valores de entrada. Considerarlo histórico hasta que se reproduzca.
- `HRManager`, `RentalManager`, `MaintenanceManager` y `UtilitiesManager` mantienen métodos sin implementar (`pass`). La ruta de mantenimiento permanece pendiente hasta definir su archivo.

