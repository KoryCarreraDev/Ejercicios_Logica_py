"""
Tabla de multiplicar — Muestra la tabla de multiplicar de un número del 1 al 10.
"""

def tabla_de_multiplicar(num1):
    for i in range(11):
        print(f"{num1} x {i} = {num1 * i}")

num1 = int(input("Ingrese el numero para ver su tabla del 1 al 10: "))

tabla_de_multiplicar(num1)