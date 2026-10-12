# Progreso

## 2026-10-11

- Separada la vista previa de devolución de su confirmación: calcular no modifica archivos; confirmar vuelve a validar y guarda inventario y control.
- Añadido el registro explícito de días pactados, reales y cobrados; el campo `dias` refleja los días reales después de la devolución.
- Centralizado el cálculo de devolución en `InventoryManager` y delegado el parseo y la coordinación en `LogicController`; `FrameManager` conserva solo la interacción visual.
- Corregido el resultado de confirmación de renta para distinguir éxito y error, y eliminado el cálculo duplicado de devolución en la interfaz.
- **Verificación aislada satisfactoria:** el flujo de renta, la vista previa sin cambios en archivos, la confirmación, el inventario actualizado, el registro en `control.json` y el rechazo de una devolución duplicada funcionaron con archivos temporales.
- El análisis AST actualizó `MAPA_PROYECTO.md` con 15 archivos Python.
- Pendiente confirmar la interacción completa desde la interfaz gráfica.
