Este proyecto solo es para el autoaprendizaje de la programacion, 
crese todos los dias y tiene mejoras con ayuda de la IA y con la documentacion oficial de cada lenguaje.
no esta diseñado para solucionar un problemas es específico. 
se aceptan comentarios. 

## Asistente local con Ollama

El proyecto incluye una interfaz local que consulta el modelo `qwen3:4b-instruct` mediante Ollama.

Para abrirla con doble clic, ejecuta `iniciar_asistente.bat` desde el Explorador de archivos. El lanzador abre PowerShell en la carpeta del proyecto y ejecuta el asistente.

1. Asegúrate de que Ollama esté instalado y abierto.
2. Desde esta carpeta, ejecuta `python asistente_local.py`.
3. Escribe una pregunta y pulsa **Preguntar**. La combinación `Ctrl+Enter` también la envía.
4. Pulsa **Actualizar mapa** para regenerar el inventario del código.
5. Pulsa **Guardar y copiar** para añadir la pregunta y respuesta actuales a `.asistente/RESPUESTAS.md` y copiar la respuesta al portapapeles para pegarla en ChatGPT.

En el selector **Ruta**, elige **Aplicación prueba** para limitar la búsqueda a `prueba/main.py`, `prueba/menu_gral.py` y `prueba/logic.py`. El mapa resume los tres; la aplicación envía el código del archivo que menciones o de hasta dos archivos relacionados con la pregunta. **Automática** puede elegir hasta tres archivos de cualquier parte del proyecto. Ambas rutas usan un contexto de 8,192 tokens.

La aplicación actualiza `.asistente/MAPA_PROYECTO.md` antes de cada pregunta y envía al modelo el mapa, las notas y hasta tres archivos que parecen relacionados con la consulta. Muestra la hora local de cada pregunta y respuesta. Las reglas persistentes están en `.asistente/INSTRUCCIONES.md`; el progreso, pendientes y errores se documentan en los otros archivos Markdown de esa carpeta.

La versión inicial solo analiza archivos `.py` y consulta Ollama localmente. La búsqueda en internet y el registro de notas desde botones de la interfaz quedan como siguientes mejoras.
