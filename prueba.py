# =====================================================================
# APP: MI CARRITO EN RENTA (Fase 1)
# =====================================================================
import os

def limpiar_pantalla():
    # 'nt' significa Windows, 'posix' es para Mac o Linux
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def pts():
    print(" .")
    print(" .")
    print(" .")
    print(" .")
    print(" .")


# Inventario inicial: Lista de diccionarios para gestionar los autos
inventario = [
    {"id": 1, "marca": "Toyota", "modelo": "Yaris", "precio_dia": 45, "disponible": True},
    {"id": 2, "marca": "Nissan", "modelo": "Versa", "precio_dia": 50, "disponible": True},
    {"id": 3, "marca": "Chevrolet", "modelo": "Aveo", "precio_dia": 40, "disponible": False}
]

def mostrar_inventario():
    print("\n--- INVENTARIO DE AUTOS ---")
    for auto in inventario:
        estado = "Disponible" if auto["disponible"] else "Rentado"
        print(f"[{auto['id']}] {auto['marca']} {auto['modelo']} - ${auto['precio_dia']}/día ({estado})")

def rentar_auto():
    mostrar_inventario()
    try:
        id_renta = int(input("\nIngrese el ID del auto que desea rentar: "))
        for auto in inventario:
            if auto["id"] == id_renta:
                if auto["disponible"]:
                    auto["disponible"] = False  # cambia a falso
                    print(f"\n¡Éxito! Ha rentado el {auto['marca']} {auto['modelo']}.")
                    return
                else:
                    print("\nLo sentimos, este auto ya está rentado.")
                    return
        print("\nEl ID introducido no existe.")
    except ValueError:
        print("\nPor favor, introduzca un número válido.")
        # sleep (60)

# Bucles y Condiciones: Menú de interacción con el usuario
def menu_principal():
    while True:
        limpiar_pantalla()
        print("\n=================================")
        print("   BIENVENIDO A MI CARRITO EN RENTA   ")
        print("=================================")
        print("1. Ver autos disponibles")
        print("2. Rentar un auto")
        print("3. Entregar un auto")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == "1":
            limpiar_pantalla()
            mostrar_inventario()
        elif opcion == "2":
            rentar_auto()
        elif opcion =="3":
            print("pronto veras la opcion de entregar / EN PROCESO")
        elif opcion == "4":
            limpiar_pantalla()
            print("\n¡Gracias por usar Mi Carrito en Renta! Hasta pronto.")
            pts()
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")
         

# Iniciar la aplicación
if __name__ == "__main__":
    menu_principal()
