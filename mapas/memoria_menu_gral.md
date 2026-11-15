# Memoria dinámica optimizada


## LoginApp (línea 11)
- __init__ (línea 13) → inicializa atributos principales
  - Atributo: self.inventory (línea 20)
  - Atributo: self.rental_manager (línea 21)
  - Atributo: self.grid_columnconfigure(0, weight (línea 24)
  - Atributo: self.grid_rowconfigure(0, weight (línea 25)
  - Atributo: self.logic (línea 26)
  - Atributo: self.frames (línea 27)
  - Atributo: self.logic.frames (línea 33)

## FrameManager (línea 39)
- __init__ (línea 40) → inicializa atributos principales
  - Atributo: self.root (línea 41)
  - Atributo: self.logic (línea 42)
  - Atributo: self.inventory (línea 43)
  - Atributo: self.rental_manager (línea 44)
  - Atributo: self.root.grid_columnconfigure(0, weight (línea 47)
  - Atributo: self.root.grid_rowconfigure(0, weight (línea 48)
  - Atributo: self.encabezado_frame (línea 51)
  - Atributo: self.frame_login (línea 52)
  - Atributo: self.frame_renta (línea 53)
  - Atributo: self.panel_admin (línea 56)
  - Atributo: self.admin (línea 57)
  - Atributo: self.renta (línea 60)
- crear_menu_principal (línea 62) → acción definida
  - Atributo: self.encabezado_frame (línea 68)
  - Atributo: self.encabezado_frame.grid(row (línea 69)
  - Atributo: self.renta (línea 72)
  - Atributo: lbl_bienvenido (línea 77)
  - Atributo: rol_texto (línea 82)
  - Atributo: self.lbl_menu (línea 83)
  - Atributo: self.lbl_menu.grid(row (línea 86)
  - Atributo: self.btn_rentar (línea 89)
  - Atributo: command (línea 90)
  - Command: command=self.renta.interfaz_renta) (línea 90)
  - Atributo: self.btn_rentar.grid(row (línea 91)
  - Atributo: self.btn_ver (línea 93)
  - Atributo: command (línea 94)
  - Command: command=self.logic.abrir_admin) (línea 94)
  - Atributo: self.btn_ver.grid(row (línea 95)
  - Atributo: self.btn_eliminar (línea 97)
  - Atributo: self.btn_eliminar.grid(row (línea 98)
  - Atributo: self.btn_informe (línea 100)
  - Atributo: self.btn_informe.grid(row (línea 101)
  - Atributo: self.btn_salir (línea 103)
  - Atributo: command (línea 104)
  - Command: command=self.logic.cerrar_sesion) (línea 104)
  - Atributo: self.btn_salir.grid(row (línea 105)
- mostrar_admin (línea 107) → acción definida
  - Atributo: self.panel_admin (línea 113)
  - Atributo: self.panel_admin.grid_columnconfigure(0, weight (línea 115)
  - Atributo: self.admin (línea 116)
  - Atributo: root (línea 117)
  - Atributo: logic (línea 118)
- regresar_menu_principal (línea 128) → acción definida

## LogicController (línea 134)
- __init__ (línea 136) → inicializa atributos principales
  - Atributo: self.role_manager (línea 137)
  - Atributo: self.rol (línea 138)
  - Atributo: self.ventana_login (línea 139)
  - Atributo: self.ventana_principal (línea 140)
- aplicar_permisos (línea 144) → acción definida
  - Atributo: permisos (línea 154)
- abrir_admin (línea 159) → acción definida
- regresar_desde_admin (línea 162) → acción definida
- cerrar_sesion (línea 167) → acción definida
  - Atributo: ventana (línea 168)
  - Atributo: ventana_login (línea 169)
  - Atributo: self._cerrando_sesion (línea 175)
- finalizar_cierre (línea 177) → acción definida
  - Atributo: self._cerrando_sesion (línea 196)