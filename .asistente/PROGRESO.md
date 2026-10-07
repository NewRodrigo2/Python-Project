# Progreso

## 2026-10-04

- Instalado Ollama y descargado el modelo local `qwen3:4b`.
- Creada la primera versión del asistente local conectado al proyecto.
- Corregida la consulta para desactivar el razonamiento interno de Qwen3, que podía consumir el límite de salida antes de producir una respuesta visible.
- Actualizado `asistente_local.py` para usar `qwen3:4b-instruct`, pedir respuestas de hasta dos párrafos breves por defecto y mostrar la hora local de cada pregunta y respuesta.
- Mejorado el diagnóstico de Ollama: la conexión usa `127.0.0.1` y la interfaz distingue errores HTTP de fallos de conexión.
- Ajustado el contexto enviado a Ollama: hasta tres archivos relevantes, fragmentos acotados y `num_ctx` configurado en 8,192 para evitar el límite previo de 4,096 tokens.
- Añadido el botón **Guardar y copiar**: registra pregunta y respuesta con hora en `RESPUESTAS.md` y copia la respuesta al portapapeles.
- Añadido el selector de ruta **Aplicación prueba** para limitar la búsqueda a `prueba/main.py`, `prueba/menu_gral.py` y `prueba/logic.py`.
- Optimizada la ruta **Aplicación prueba** para enviar solo el código relacionado con la pregunta y volver a 8,192 tokens de contexto tras un timeout con los tres archivos completos.
- Creado `iniciar_asistente.bat` para abrir PowerShell en la carpeta del proyecto e iniciar el asistente con doble clic.
- Optimizada la consulta de inventario en la ruta **Aplicación prueba**: las preguntas sobre clases, funciones o métodos usan solo el mapa actualizado, omiten código fuente y notas, y reducen el contexto y la salida.
- Aplicado el mismo modo compacto de inventario a **Automática** y corregida la clasificación: solo las preguntas de enumeración usan 4,096 tokens; las demás conservan 8,192.
