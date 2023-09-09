import random
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Simulación de lanzamiento de moneda")

# Crear los widgets
etiqueta = tk.Label(ventana, text="Ingrese el número de lanzamientos:")
entrada = tk.Entry(ventana)
boton = tk.Button(ventana, text="Lanzar", command=lambda: simular_lanzamientos(int(entrada.get())))
resultado_caras = tk.Label(ventana, text="")
resultado_cruces = tk.Label(ventana, text="")
# Agregar las etiquetas para mostrar la cantidad de veces que cae cara y cruz
cantidad_caras = tk.Label(ventana, text="")
cantidad_cruces = tk.Label(ventana, text="")

# Ubicar los widgets en la ventana
etiqueta.pack()
entrada.pack()
boton.pack()
resultado_caras.pack()
resultado_cruces.pack()
# Ubicar las etiquetas adicionales en la ventana
cantidad_caras.pack()
cantidad_cruces.pack()

# Función para simular los lanzamientos
def simular_lanzamientos(n):
    # Inicializar contadores
    caras = 0
    cruces = 0

    # Simular los lanzamientos
    for i in range(n):
        resultado = random.choice(['cara', 'cruz'])
        if resultado == 'cara':
            caras += 1
        else:
            cruces += 1

    # Calcular la frecuencia relativa
    frecuencia_caras = caras / n
    frecuencia_cruces = cruces / n

    # Actualizar las etiquetas con los resultados
    resultado_caras.config(text=f'Frecuencia relativa de caras: {frecuencia_caras:.2f}')
    resultado_cruces.config(text=f'Frecuencia relativa de cruces: {frecuencia_cruces:.2f}')
    # Actualizar las etiquetas adicionales con la cantidad de veces que cae cara y cruz
    cantidad_caras.config(text=f'Cantidad de caras: {caras}')
    cantidad_cruces.config(text=f'Cantidad de cruces: {cruces}')

# Mostrar la ventana
ventana.mainloop()  
