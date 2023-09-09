# Lanzamiento-de-Moneda
Un simulador en python para determinar el resultado de un lanzamiento de monedas, mostrando la frecuencia de cada resultado.

## Programación Orientada a Objetos

La estructura de programación que se ha utilizado en este código es conocida como "programación orientada a eventos" o "event-driven programming". Esta es una forma común de diseñar aplicaciones de interfaz de usuario (UI) interactivas y fáciles de mantener. Facilita la organización del código, la interacción con el usuario y la expansión de la funcionalidad, lo que la hace una elección sólida para aplicaciones de este tipo.

## Estructura del código

Iniciamos con las importaciones de las librerías necesarias para el funcionamiento.

`import random`, el cual importa la librería **random**, que se utiliza para generar números aleatorios.

`import tkinter as tk`, Aquí importamos el módulo `tkinter` y lo renombramos como `tk`. **tkinter** es una biblioteca gráfica que se utiliza para crear interfaces de usuario en Python.

Se crea una instancia de la clase `Tk` de tkinter, que representa la ventana principal de la aplicación.
```
ventana = tk.Tk()
```
Ahora se establece el título de la ventana principal.
```
ventana.title("Simulación de lanzamiento de moneda")
```
Se crean varios widgets de tkinter:
- `etiqueta`: Una etiqueta de texto para indicar al usuario que ingrese el número de lanzamientos. 
- `entrada`: Un campo de entrada de texto para que el usuario pueda ingresar el número de lanzamientos.
- `boton`: Un botón que el usuario debe presionar para realizar la simulación.
- `resultado_caras`: Una etiqueta que mostrará la frecuencia relativa de caras.
- `resultado_cruces`: Una etiqueta que mostrará la frecuencia relativa de cruces.
- `cantidad_caras`: Una etiqueta que mostrará la cantidad de veces que cayó cara.
- `cantidad_cruces`: Una etiqueta que mostrará la cantidad de veces que cayó cruz.

Estas líneas colocan los widgets en la ventana principal utilizando el método `pack()`. Esto determina su posición y distribución en la ventana.
```
etiqueta.pack(), entrada.pack(), boton.pack(), resultado_caras.pack(), 
resultado_cruces.pack(), cantidad_caras.pack(), cantidad_cruces.pack()
```
A continuación, se define una función llamada `simular_lanzamientos(n)`, que simula el lanzamiento de una moneda `n` veces. Dentro de esta función:
- Se inicializan dos contadores, `caras` y `cruces`, para llevar un registro de cuántas veces cae cara y cuántas veces cae cruz.
- Se utiliza un bucle `for` para realizar `n` lanzamientos de moneda
- En cada lanzamiento, se utiliza `random.choice(['cara', 'cruz'])` para obtener un resultado aleatorio que puede ser 'cara' o 'cruz'.
- Se actualizan los contadores `caras` y `cruces` según el resultado del lanzamiento.
- Se calculan las frecuencias relativas de caras y cruces dividiendo las cuentas por `n`.
- Se actualizan las etiquetas `resultado_caras` y `resultado_cruces` con las frecuencias relativas calculadas.
- También se actualizan las etiquetas `cantidad_caras` y `cantidad_cruces` con las cantidades totales de caras y cruces.

Finalmente, se inicia el bucle principal de tkinter, que mantiene la ventana abierta y responde a las interacciones del usuario.
 ```
ventana.mainloop()
```
