# Memoria del proyecto para asistentes de IA

Última revisión: 2026-10-04.

## Propósito

Proyecto personal de autoaprendizaje de programación. Cambia con frecuencia y se desarrolla con apoyo de IA y documentación oficial.

## Estructura conocida

- `prueba/`: aplicación de consola para renta de vehículos y funciones relacionadas con personal, inventario, roles y administración. El punto de entrada aparente es `prueba/main.py`; confirmar siempre leyendo el archivo actual.
- `prueba/logic.py`: clases de lógica de negocio, entre ellas `AuthManager`, `RoleManager`, `HRManager`, `InventoryManager`, `RentalManager`, `MaintenanceManager` y `UtilitiesManager` (según el mapa generado el 2026-10-04).
- `android_happy_face/`: pequeño proyecto Android/Kivy que dibuja y anima una cara; revisar `BUILD_INSTRUCTIONS.txt` antes de modificar o ejecutar su proceso de construcción.
- `mapas/`: analizadores AST anteriores y mapas históricos. Son referencias, no la fuente actual del código.
- `auto_pr_script.py`: automatización relacionada con creación y manejo de Pull Requests; inspeccionar antes de ejecutarla porque puede interactuar con GitHub.
- `pba_codigo.py`: ejercicios de Python.
- `asistente_local.py`: interfaz de escritorio en Tkinter que conecta el proyecto con el servicio local de Ollama.
- `iniciar_asistente.bat`: abre PowerShell en la carpeta del proyecto e inicia la interfaz local.
- El botón **Guardar y copiar** añade la pregunta y respuesta actuales a `.asistente/RESPUESTAS.md` y copia solo la respuesta al portapapeles.
- `requirements.txt`: dependencias Python declaradas del proyecto.

## Memoria y mapa dinámico

- `MAPA_PROYECTO.md` se regenera desde los `.py` actuales con análisis AST al pulsar **Actualizar mapa** y antes de cada consulta en el asistente local.
- El mapa identifica rutas, clases, funciones, métodos, líneas y docstrings simples. No demuestra el comportamiento en ejecución ni detecta todas las relaciones entre objetos.
- `INSTRUCCIONES.md` contiene las preferencias de respuesta para la IA local.
- `PROGRESO.md`, `PENDIENTES.md` y `ERRORES.md` registran el estado de trabajo; actualizar estas notas cuando cambie el estado confirmado.
- Los archivos `mapas/PROJECT_MAP_*.txt` son instantáneas históricas. En particular, `PROJECT_MAP_FUNC_20260927_200356.txt` cubre la carpeta `prueba/`, no todo el proyecto ni el estado actual.

## Reglas para futuras sesiones

1. Leer esta memoria y las notas recientes antes de responder sobre el proyecto.
2. Para hechos actuales, comprobar `MAPA_PROYECTO.md` y leer los `.py` relevantes; no confiar en mapas antiguos si difieren del código.
3. En la ruta **Automática**, el asistente selecciona hasta tres archivos por coincidencia de palabras clave, limita cada uno a 5,000 caracteres y usa 8,192 tokens para preguntas normales. La ruta **Aplicación prueba** limita la búsqueda a `prueba/main.py`, `prueba/menu_gral.py` y `prueba/logic.py`. Las preguntas de inventario (listar clases, funciones o métodos) usan solo el mapa actualizado, sin código fuente ni notas, y configuran 4,096 tokens; si se nombra un `.py`, solo se adjunta la sección de ese archivo del mapa.
4. Ollama y los modelos instalados responden localmente. La búsqueda web no está implementada en `asistente_local.py` todavía.
5. Preferencia del usuario: explicar primero el error y la propuesta de solución sin generar código; crear código solo cuando lo solicite, y ejemplos extra solo si los pide. Responder en español y con brevedad.
6. `asistente_local.py` usa `qwen3:4b-instruct`, solicita respuestas de hasta dos párrafos breves, muestra la hora local de pregunta y respuesta, permite guardar/copiar la última respuesta y ofrece las rutas **Automática** y **Aplicación prueba**. Las preguntas de inventario limitan la salida a 110 tokens y el contexto a 4,096; las demás consultas usan 8,192 tokens.

## Límites de esta memoria

Este documento es un resumen de navegación, no una copia del código ni memoria automática del modelo. Puede quedar desactualizado; validar los detalles consultando el proyecto actual.
