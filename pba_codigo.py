import tkinter as tk

ventana = tk.Tk()
ventana.title("Animación en Canvas")
ventana.geometry("400x300")

canvas = tk.Canvas(ventana, width=400, height=300, bg="white")
canvas.pack(fill="both", expand=True)

# Creamos una pelotita (un óvalo) en la coordenada inicial x=50, y=130
pelota = canvas.create_oval(50, 130, 90, 170, fill="red")

# Variable para controlar la velocidad de movimiento
velocidad_x = 3

def animar():
    global velocidad_x
    
    # Movemos la pelota en la dirección X e Y (dx, dy)
    canvas.move(pelota, velocidad_x, 0)
    
    # Obtenemos las coordenadas actuales de la pelota para que reote en los bordes
    posicion = canvas.coords(pelota)
    x1, y1, x2, y2 = posicion
    
    # Si choca con el borde derecho o izquierdo, invertimos la dirección
    if x2 >= 400 or x1 <= 0:
        velocidad_x = -velocidad_x
        
    # Llamamos a esta misma función cada 20 milisegundos para crear el efecto de movimiento
    ventana.after(20, animar)

# Iniciamos la animación
animar()

ventana.mainloop()