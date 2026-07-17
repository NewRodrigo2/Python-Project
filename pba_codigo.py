import os
from pathlib import Path  # <-- ¡Esta es la línea que te falta!

# Ahora Python ya sabe qué es "Path"
ruta_actual = Path.cwd()
print(f"Ruta completa: {ruta_actual}")



# Opción clásica con os
ruta_actual = os.getcwd()
print(f"Ruta completa: {ruta_actual}")

a = input('Enter para continuar')

ruta_actual = os.getcwd()
unidad, resto = os.path.splitdrive(ruta_actual)

print(f"Unidad actual: {unidad}")


a = input ('Enter para continuar')



# Obtiene la ruta del directorio de trabajo
ruta_actual = Path.cwd()
print(f"Ruta completa: {ruta_actual}")

# Obtiene la unidad (en Windows devolverá 'C:' o similar; en Linux/Mac devolverá '/')
unidad = ruta_actual.drive
print(f"Unidad actual: {unidad}")

a = input ('Enter para continuar')

