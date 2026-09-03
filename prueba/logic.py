'''logic.py

Indicacion para Copilot: dejaremos pendiente instanciar la ruta en class MaintenanceManager: hasta que se cree el archivo correspondiente
Pregunta para Copilot: ninguna
'''
import json
import os
from pathlib import Path
# ...................... Estableciendo la ruta de los archivos .json  ..........
ruta_actual = Path(__file__).parent 
CARPETA_DATOS = ruta_actual / "datos"

ARCHIVO_DATOS = CARPETA_DATOS / "inventario.json"    # total de autos de la compañia, class InventoryManager:
ARCHIVO_CONTROL = CARPETA_DATOS / "control.json"     # inventario de autos rentados y no rentados, class RentalManager:
ARCHIVO_TEX = CARPETA_DATOS / "autos_ordenados.txt"  # informe de autos rentados hasta el momento
PERSONAL = CARPETA_DATOS / "personal.json"           # plantilla de personal

print("<DEBUG:logic.py> CARPETA DE DATOS",CARPETA_DATOS)
print("<DEBUG:logic.py>RUTA DEL ARCHIVO PERSONAL", PERSONAL)

PURPLE = "\033[95m"
V_B = "\033[92m"
RESET = "\033[0m"

# -------------------------------
# Clase para autenticación, # logic.py
# -------------------------------
class AuthManager:
    def __init__(self, archivo_personal=PERSONAL):
        self.archivo_personal = archivo_personal
        print(f"{PURPLE}[DEBUG:logic.py] AuthManager inicializado con archivo:{V_B} {self.archivo_personal}{RESET}")
        print(f"[DEBUG:logic.py] Ruta absoluta esperada:", Path(self.archivo_personal).resolve())

    def validar_usuario(self, usuario, password, rol):
        """
        Valida usuario, contraseña y rol contra el archivo JSON.
        Retorna True si la validación es correcta, False en caso contrario.
        """
        print(f"[DEBUG:logic.py] validar_usuario llamado con usuario='{usuario}', password='{password}', rol='{rol}'")
        try:
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
    def __init__(self, archivo_inventario=ARCHIVO_DATOS):
        self.archivo_inventario = archivo_inventario

    def agregar_auto(self, datos_auto):
        """Agrega un nuevo auto al inventario."""
        pass

    def eliminar_ticket(self, ticket_id):
        """Elimina un ticket del control."""
        pass

    def generar_informe(self):
        """Genera un informe de autos o rentas."""
        pass


# -------------------------------
# Clase para Rentas
# -------------------------------
class RentalManager:
    def __init__(self, archivo_rentas=ARCHIVO_CONTROL):
        self.archivo_rentas = archivo_rentas

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
    def __init__(self, archivo_mantenimiento):
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
