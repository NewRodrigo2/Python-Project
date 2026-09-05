'''logic.py
datos necesarios para Copilot: este es mi script main.py, es el mas actualizado, se realizo un git pull al inicio de la joranada, 
rama activa class_pyton, todos los script , clases , metodos que se importan estan actualizados

Indicacion para Copilot: dejaremos pendiente instanciar la ruta en class MaintenanceManager: hasta que se cree el archivo correspondiente
Pregunta para Copilot: en el  def cargar_inventario(self): se utiliza os.path.exists(self.archivo_dato), es correcto?
'''
import json
import os
from pathlib import Path
from datetime import datetime
# ...................... Estableciendo la ruta de los archivos .json  ..........
ruta_actual = Path(__file__).parent 
ruta_datos = Path(__file__).parent / "datos"

CARPETA_DATOS = ruta_datos

ARCHIVO_DATOS = CARPETA_DATOS / "inventario.json"    # total de autos de la compañia, class InventoryManager:
ARCHIVO_CONTROL = CARPETA_DATOS / "control.json"     # inventario de autos rentados y no rentados, class RentalManager:
ARCHIVO_TEX = CARPETA_DATOS / "autos_ordenados.txt"  # informe de autos rentados hasta el momento
PERSONAL = CARPETA_DATOS / "personal.json"           # plantilla de personal
ARCHIVO_MTTO = CARPETA_DATOS / "mtto.json"
#..........
PURPLE = "\033[95m"
V_B = "\033[92m"
RESET = "\033[0m"
#..........

print(f"<DEBUG:logic.py> CARPETA DE DATOS,....  {CARPETA_DATOS}")
print(f"<DEBUG:logic.py>RUTA DEL ARCHIVO PERSONAL,....{ PERSONAL}")

# -------------------------------
# Clase para autenticación, # logic.py
# -------------------------------
class AuthManager:
    def __init__(self, archivo_personal=PERSONAL):
        self.archivo_personal = archivo_personal
#..DEBUG....
        print(f"{PURPLE}[DEBUG:logic.py/AuthManager] ..inicializado con archivo:{V_B} {self.archivo_personal}{RESET}")
        print(f"[DEBUG:logic.py/AuthManager] Ruta absoluta esperada:", Path(self.archivo_personal).resolve())

    def validar_usuario(self, usuario, password, rol):

        print(f"[DEBUG:logic.py/AuthManager/validar_usuario] validar_usuario llamado con usuario='{usuario}', password='{password}', rol='{rol}'")
        print(f"{PURPLE}[DEBUG:logic.py/AuthManager/validar_usuario] ..inicializado con archivo:{V_B} {self.archivo_personal}{RESET}")

        try:
# .....DEBUG            
            print("Ruta absoluta usada:", Path(self.archivo_personal).resolve())
            print("Existe el archivo?:", Path(self.archivo_personal).exists())

            with open(self.archivo_personal, "r", encoding="utf-8") as archivo:
                usuarios_db = json.load(archivo)
                print(f"{PURPLE}[DEBUG] Archivo cargado, total usuarios: {len(usuarios_db)}{RESET}")

            for user in usuarios_db:
                print(f"{PURPLE}[DEBUG:logic.py] Comparando con registro: {user}{RESET}")
                db_nombre = str(user.get("nombre", "")).strip().lower()
                db_id = str(user.get("id_emp", "")).strip().lower()
                db_password = str(user.get("pasword", "")).strip()
                db_area = str(user.get("area", "")).strip().lower()

                print(f"[DEBUG:logic.py] db_nombre='{db_nombre}', db_id='{db_id}', db_password='{db_password}', db_area='{db_area}'")

                match_usuario = (db_nombre == usuario or db_id == usuario)
                match_password = (db_password == password)
                match_area = (db_area == rol.lower())

                if match_usuario and match_password and match_area:
                    return True  # Usuario válido

            return False  # Si no encontró coincidencia

        except FileNotFoundError:
            print("Error crítico: El archivo personal.json no existe en la ruta.")
            return False
        except json.JSONDecodeError:
            print("Error crítico: El archivo personal.json tiene un formato inválido.")
            return False

# -------------------------------
# Clase para gestión de roles
# -------------------------------
class RoleManager:
    def __init__(self, archivo_personal=PERSONAL):
        self.archivo_personal = archivo_personal

        # Lista centralizada de roles
        self.roles = ["Mostrador", "Director", "Mecánico", "Administrador", "Supervisor"]

        # Diccionario de permisos asociados a cada rol
        self.permisos = {
            "mostrador": ["renta"],
            "administrador": ["admin"],
            "mecanico": ["taller"],
            "supervisor": ["utilerias"],
            "director": ["admin", "renta", "utilerias"]
        }

    def obtener_roles(self):
        """Devuelve la lista de roles disponibles para la interfaz."""
        return self.roles

    def aplicar_permisos(self, rol):
        """Devuelve qué acciones están habilitadas según el rol."""
        if not rol:
            return []

        # Normalizamos el rol (quitamos acentos y espacios)
        rol_procesado = (
            rol.lower()
            .replace("á", "a")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ú", "u")
            .strip()
        )
        return self.permisos.get(rol_procesado, [])

# -------------------------------
# Clase para Recursos Humanos
# -------------------------------
class HRManager:
    def __init__(self, archivo_personal=PERSONAL):
        self.archivo_personal = archivo_personal


    def agregar_personal(self, nombre, rol, area, hrs_cont, sueldo, password):
        """Agrega nuevo personal al archivo JSON."""
        pass

    def calcular_nomina(self):
        """Calcula la nómina del personal registrado."""
        pass

# -------------------------------
# Clase para Inventario
# -------------------------------

class InventoryManager:
    def __init__(self, archivo_path=ARCHIVO_DATOS):
        self.archivo_datos = archivo_path
        self.carpeta_datos = CARPETA_DATOS
      
        self.INVENTARIO_DEFECTO = [
            {"id": 1, "marca": "Toyota", "modelo": "Yaris", "precio_dia": 45, "disponible": True, "dias": 0, "km": 0, "venta": 0},
            {"id": 2, "marca": "Nissan", "modelo": "Versa", "precio_dia": 50, "disponible": True, "dias": 0, "km": 0, "venta": 0},
            {"id": 3, "marca": "Chevrolet", "modelo": "Aveo", "precio_dia": 40, "disponible": False, "dias": 0, "km": 0, "venta": 0}
        ]
        
        self.AUTO_CONTROL = [
            {
                "c_id": 1, 
                "km_recorridos": 0, 
                "c_venta_total": 0, 
                "c_fecha_renta": "01/01/2026",
                "c_dias": 0
            } 
        ]
        
# Cargar datos al instanciar
        self.cargar_inventario()
        self.verificar_control()

    def cargar_inventario(self):
        """Lee el inventario.json o carga los valores por defecto si no existe."""
        if not Path(self.archivo_datos).exists():
            os.makedirs(self.carpeta_datos)

        if Path(self.archivo_datos).exists():
            try:
                with open(self.archivo_datos, "r", encoding="utf-8") as archivo:
                    self.inventario = json.load(archivo)
            except Exception:
                self.inventario = self.INVENTARIO_DEFECTO
        else:
            self.inventario = self.INVENTARIO_DEFECTO
            self.guardar_inventario()

    def guardar_inventario(self):
        with open(self.archivo_datos, "w", encoding="utf-8") as archivo:
            json.dump(self.inventario, archivo, indent=4, ensure_ascii=False)

    def verificar_control(self):
        """Verifica que control.json no esté vacío; si lo está, agrega la lista por defecto."""
        if os.path.exists(self.carpeta_datos):
            try:
                with open(self.ARCHIVO_CONTROL, "r", encoding="utf-8") as archivo:
                    control = json.load(archivo)
                    if not control: # Si está vacío []
                        self.guarda_control(self.AUTO_CONTROL)
            except Exception:
                self.guarda_control(self.AUTO_CONTROL)
        else:
            self.guarda_control(self.AUTO_CONTROL)

    def guarda_control(self, datos=None):
        if datos is None:
            datos = self.AUTO_CONTROL
        with open(ARCHIVO_CONTROL, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def obtener_autos_disponibles(self):
        """Devuelve únicamente la lista de autos que tienen disponible = True."""
        self.cargar_inventario()
        return [auto for auto in self.inventario if auto.get("disponible", False)]

    def obtener_autos_rentados(self):
        """Devuelve la lista de autos que están actualmente rentados (disponible = False)."""
        self.cargar_inventario()
        return [auto for auto in self.inventario if not auto.get("disponible", True)]

    def procesar_renta(self, id_auto, dias_p_renta):
        """Renta un auto actualizando su estado y guardando los cambios."""
        for auto in self.inventario:
            if auto["id"] == id_auto:
                if auto["disponible"]:
                    auto["disponible"] = False
                    auto["dias"] = dias_p_renta
                    auto["venta"] = dias_p_renta * auto["precio_dia"]
                    auto["km"] = 0
                    self.guardar_inventario()
                    return True, f"¡Éxito! Ha rentado el {auto['marca']} {auto['modelo']}."
                else:
                    return False, "Lo sentimos, este auto ya está rentado."
        return False, "El ID introducido no existe."

    def procesar_regreso(self, id_regresar, dias_reales, km_nuevos):
        """Calcula costos, actualiza inventario y añade un registro a control.json."""
        for auto in self.inventario:
            if auto["id"] == id_regresar and not auto["disponible"]:
                # Calcular días a cobrar (el mayor entre los días pactados y los utilizados)
                d_dias = dias_reales if dias_reales > auto["dias"] else auto["dias"]
                costo_total = (auto["precio_dia"] * d_dias) + km_nuevos

                # Actualizar auto
                auto["disponible"] = True
                auto["dias"] = d_dias
                auto["km"] += km_nuevos
                auto["venta"] += costo_total
                self.guardar_inventario()

                # Cargar control actual para agregar el ticket nuevo
                try:
                    with open(self.ARCHIVO_CONTROL, "r", encoding="utf-8") as f:
                        control = json.load(f)
                except Exception:
                    control = []

                num_transaccion = len(control) + 1
                fecha_actual = datetime.now().strftime("%d/%m/%Y")

                nueva_renta = {
                    "transaccion_id": num_transaccion,
                    "c_id": auto["id"],
                    "c_marca": auto["marca"],
                    "c_modelo": auto["modelo"],
                    "km_recorridos": km_nuevos,
                    "c_venta_total": costo_total,
                    "c_fecha_renta": fecha_actual,
                    "c_dias": dias_reales
                }
                control.append(nueva_renta)
                self.guarda_control(control)

                return True, num_transaccion, costo_total

        return False, 0, 0

# -------------------------------
# Clase para Rentas
# -------------------------------
class RentalManager:
    def __init__(self, archivo_control=ARCHIVO_CONTROL):
        self.archivo_control = archivo_control

    def registrar_renta(self, datos_renta):
        """Registra una nueva renta."""
        pass

    def registrar_entrega(self, renta_id):
        """Registra la entrega de un auto rentado."""
        pass


# -------------------------------
# Clase para Mantenimiento
# -------------------------------
class MaintenanceManager:
    def __init__(self, ARCHIVO_MTTO):
        self.archivo_mantenimiento = archivo_mantenimiento

    def registrar_mantenimiento(self, datos_mantenimiento):
        """Registra un mantenimiento realizado."""
        pass


# -------------------------------
# Clase para Utilerías
# -------------------------------
class UtilitiesManager:
    def __init__(self):
        pass

    def generar_reporte_general(self):
        """Genera un reporte general del sistema."""
        pass
