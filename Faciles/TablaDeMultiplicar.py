"""
Tabla de multiplicar — Muestra la tabla de multiplicar de un número del 1 al 10.
"""

def tabla_de_multiplicar(num1): #Definimos la función
    for i in range(11): #Iteramos sobre i 11 veces, empezando desde el 0 terminando en el 10
        print(f"{num1} x {i} = {num1 * i}") #imprimimos y multiplicamos 5 x 2 = 10

num1 = int(input("Ingrese el numero para ver su tabla del 1 al 10: ")) #Capturamos el numero

tabla_de_multiplicar(num1) #llamamos la función con el numero