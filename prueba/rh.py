'''
Módulo de Recursos Humanos (Lógica de Datos)
'''
import os
import json
from pathlib import Path

# Configuración de rutas
ruta_actual = os.getcwd() 
unidad = os.path.splitdrive(ruta_actual)[0] 
if unidad == "C:":
    CARPETA_DATOS = Path(unidad + "\\") / "Users" / "danie" / "Documents" / "Python Project" / "prueba" / "datos"
else:
    CARPETA_DATOS = Path(unidad + "\\") / "Python" / "Python Project" / "prueba" / "datos"

ARCHIVO_DATOS = CARPETA_DATOS / "personal.json"

new_personal = []

def guardar_inventario_personal(archi):
    """Guarda la lista de empleados en el archivo JSON."""
    try:
        # Aseguramos que la carpeta exista antes de guardar
        CARPETA_DATOS.mkdir(parents=True, exist_ok=True)
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump(archi, archivo, indent=4, ensure_ascii=False)
        return True, "Datos guardados correctamente."
    except Exception as e:
        return False, f"Error al guardar el archivo: {e}"

def abre_inventario_personal():
    """Carga los empleados del archivo JSON si existe."""
    global new_personal
    if ARCHIVO_DATOS.exists():
        try:
            with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
                new_personal = json.load(archivo)
        except Exception:
            new_personal = []
    else:
        new_personal = []
    return new_personal

def agregar_personal_gui(nombre, rol, area, hrs_cont, sueldo, password):
    """
    Función optimizada para la Interfaz Gráfica (Tkinter).
    Procesa, valida los tipos de datos y guarda en personal.json.
    """
    global new_personal
    
    # 1. Cargamos el archivo JSON actual
    new_personal = abre_inventario_personal()

    # 2. Asignamos ID autoincremental
    if new_personal:
        # Convertimos los ID a entero para encontrar el máximo de forma segura
        ids_existentes = [int(emp.get("id_emp", 0)) for emp in new_personal if str(emp.get("id_emp", "0")).isdigit()]
        nuevo_id = max(ids_existentes, default=0) + 1
    else:
        nuevo_id = 1

    # 3. Formateamos y convertimos los valores
    try:
        h_cont_num = int(hrs_cont) if str(hrs_cont).isdigit() else 0
        sueldo_num = float(sueldo) if sueldo else 0.0
    except ValueError:
        return False, "Las horas contratadas y sueldo deben ser números válidos."

    empleado_nuevo = {
        "id_emp": str(nuevo_id),
        "nombre": nombre,
        "rol": rol,
        "area": area,
        "hrs_cont": h_cont_num,
        "hrs_trab": 0,       # Inicializado por defecto
        "sueldo": sueldo_num,
        "ausencias": 0,      # Inicializado por defecto
        "pasword": password
    }

    # 4. Agregamos a la lista y guardamos
    new_personal.append(empleado_nuevo)
    exito, msj = guardar_inventario_personal(new_personal)
    
    if exito:
        return True, f"Empleado '{nombre}' agregado exitosamente con ID: {nuevo_id}"
    else:
        return False, msj