'''logic.py
datos necesarios para Copilot: este es mi script logic.py, es el mas actualizado, se realizo un git pull al inicio de la joranada, 
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

# -------------------------------
# Clase para autenticación, # logic.py
# -------------------------------
class AuthManager:
    def __init__(self, archivo_personal=PERSONAL):
        self.archivo_personal = archivo_personal

    def validar_usuario(self, usuario, password, rol):

        try:
            with open(self.archivo_personal, "r", encoding="utf-8") as archivo:
                usuarios_db = json.load(archivo)

            for user in usuarios_db:
                db_nombre = str(user.get("nombre", "")).strip().lower()
                db_id = str(user.get("id_emp", "")).strip().lower()
                db_password = str(user.get("pasword", "")).strip()
                db_area = str(user.get("area", "")).strip().lower()

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
        self.ARCHIVO_CONTROL = os.path.join(self.carpeta_datos, "control.json")  # ✅ Definir ruta

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

#--- Cargar datos al instanciar
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

#--- Asegura que el inventario esté cargado
    def obtener_autos_disponibles(self):
        self.cargar_inventario()
        return [auto for auto in self.inventario if auto.get("disponible", False)]

#--- Devuelve la lista de autos que están actualmente rentados (disponible = False)."""
    def obtener_autos_rentados(self):
        self.cargar_inventario()
        return [auto for auto in self.inventario if not auto.get("disponible", True)]

#--- Renta un auto actualizando su estado y guardando los cambios."""
    def procesar_renta(self, id_auto, dias_p_renta):
        if dias_p_renta <= 0:
            return False, "Los días de renta deben ser mayores que cero."

        for auto in self.inventario:
            if auto["id"] == id_auto:
                if auto["disponible"]:
                    auto["disponible"] = False
                    auto["dias"] = dias_p_renta
                    # Conservamos los días pactados para compararlos con los días reales al devolver.
                    auto["dias_pactados"] = dias_p_renta
                    auto.pop("dias_reales", None)
                    auto.pop("dias_cobrados", None)
                    auto["km"] = 0
                    # Durante la renta, venta muestra el importe provisional de esta operación.
                    auto["venta"] = dias_p_renta * auto["precio_dia"]
                    self.guardar_inventario()
                    return True, f"¡Éxito! Ha rentado el {auto['marca']} {auto['modelo']}."
                else:
                    return False, "Lo sentimos, este auto ya está rentado."
        return False, "El ID introducido no existe."

    def calcular_presupuesto_regreso(self, id_auto, dias_reales, km_nuevos):
        """Calcula el cobro de una devolución sin modificar ni guardar el inventario."""
        try:
            id_auto = int(id_auto)
            dias_reales = int(dias_reales)
            km_nuevos = float(km_nuevos)
        except (TypeError, ValueError):
            return None, "Ingresa un ID, días y kilómetros válidos."

        if dias_reales <= 0:
            return None, "Los días reales deben ser mayores que cero."
        if km_nuevos < 0:
            return None, "Los kilómetros no pueden ser negativos."

        self.cargar_inventario()
        auto = next(
            (a for a in self.inventario if int(a["id"]) == id_auto and not a.get("disponible", True)),
            None,
        )
        if auto is None:
            return None, "El ID no corresponde a un auto rentado."

        # El cobro respeta al menos los días pactados, mientras guardamos aparte los reales.
        dias_pactados = int(auto.get("dias_pactados", auto.get("dias", 0)))
        dias_cobrados = max(dias_reales, dias_pactados)
        presupuesto = (auto["precio_dia"] * dias_cobrados) + km_nuevos
        return presupuesto, "OK"

    def procesar_regreso(self, id_regresar, dias_reales, km_nuevos):
        """Confirma una devolución, actualiza inventario y agrega su registro de control."""
        presupuesto, mensaje = self.calcular_presupuesto_regreso(
            id_regresar, dias_reales, km_nuevos
        )
        if presupuesto is None:
            return False, mensaje

        id_regresar = int(id_regresar)
        dias_reales = int(dias_reales)
        km_nuevos = float(km_nuevos)
        auto = next(
            a for a in self.inventario
            if int(a["id"]) == id_regresar and not a.get("disponible", True)
        )
        dias_pactados = int(auto.get("dias_pactados", auto.get("dias", 0)))
        dias_cobrados = max(dias_reales, dias_pactados)

        # El campo dias refleja los días reales; los días cobrados quedan explícitos.
        auto["disponible"] = True
        auto["dias"] = dias_reales
        auto["dias_reales"] = dias_reales
        auto["dias_pactados"] = dias_pactados
        auto["dias_cobrados"] = dias_cobrados
        auto["km"] = auto.get("km", 0) + km_nuevos
        # Sustituimos el importe provisional de la renta por el cobro final, sin duplicarlo.
        auto["venta"] = presupuesto
        self.guardar_inventario()

        # Conservamos el historial de devoluciones en control.json.
        try:
            with open(self.ARCHIVO_CONTROL, "r", encoding="utf-8") as archivo:
                control = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            control = []

        num_transaccion = len(control) + 1
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        control.append({
            "transaccion_id": num_transaccion,
            "c_id": auto["id"],
            "c_marca": auto["marca"],
            "c_modelo": auto["modelo"],
            "km_recorridos": km_nuevos,
            "c_venta_total": presupuesto,
            "c_fecha_renta": fecha_actual,
            "c_dias": dias_reales,
            "c_dias_pactados": dias_pactados,
            "c_dias_cobrados": dias_cobrados,
        })
        self.guarda_control(control)

        return True, f"Devolución confirmada. Transacción {num_transaccion}; total ${presupuesto:.2f}."

    def calcular_precio(self, id_auto, dias):
        self.cargar_inventario()
        if int(dias) <= 0:
            return None
        auto = next((a for a in self.inventario if int(a["id"]) == int(id_auto) and a["disponible"]), None)
        if auto:
            return auto["precio_dia"] * dias
        return None



#--- ----------------------------
#---    Clase para Rentas
#--- ----------------------------
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
    def __init__(self, archivo_mantenimiento = ARCHIVO_MTTO):
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
