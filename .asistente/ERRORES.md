# Errores conocidos

## Respuesta vacía de Qwen3

- **Causa identificada:** la variante `qwen3:4b` mostraba razonamiento interno incluso al pedir que lo desactivara.
- **Corrección aplicada:** `asistente_local.py` ahora usa la variante `qwen3:4b-instruct` y muestra un aviso si Ollama devuelve una respuesta vacía.
- **Estado:** pendiente de confirmar el resultado en la interfaz.

## Error de conexión reportado el 2026-10-05

- `ollama list` confirma que el servicio y `qwen3:4b-instruct` están disponibles desde PowerShell.
- El asistente ocultaba los errores HTTP bajo un mensaje genérico de conexión.
- **Corrección aplicada:** usar `127.0.0.1` directamente y mostrar el código y cuerpo de los errores HTTP, o el motivo de conexión.
- **Estado:** pendiente de volver a consultar desde la interfaz y revisar el detalle si falla.

## Contexto excedido el 2026-10-05

- **Causa confirmada:** la solicitud tenía 6,776 tokens, mientras que Ollama reservaba 4,096.
- **Corrección aplicada:** configurar `num_ctx` en 8,192 y reducir el mapa, las notas y el código recuperado por consulta.
- **Estado:** pendiente de confirmar una respuesta desde la interfaz.

## Timeout al consultar la ruta Aplicación prueba el 2026-10-06

- **Causa confirmada:** la ruta enviaba los tres scripts completos en una sola solicitud, haciendo lenta la evaluación del contexto en el procesador.
- **Corrección aplicada:** la ruta mantiene los tres archivos en su alcance, pero envía el código seleccionado por la pregunta; si se nombra un archivo, incluye ese archivo completo. El contexto vuelve a 8,192 tokens.
- **Corrección adicional:** las preguntas de inventario (clases, funciones o métodos) usan únicamente el mapa actualizado, sin código fuente ni notas, con contexto de 4,096 tokens y salida limitada.
- **Reporte posterior:** en la ruta **Automática** llegó una solicitud de 6,888 tokens con límite de 4,096. La selección del límite dependía de una expresión distinta a la detección de inventario, y podía activar 4,096 por mencionar clases o métodos sin que el contenido se compactara de igual manera.
- **Corrección aplicada:** unificada la detección de inventario entre la construcción del contexto y las opciones del modelo; en **Automática**, una pregunta que nombra un archivo usa solo su sección del mapa.
- **Estado:** pendiente de probar la consulta de clases en `logic.py`.
