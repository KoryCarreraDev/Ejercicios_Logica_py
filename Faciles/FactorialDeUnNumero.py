"""
Factorial — Calcula el factorial de un número N (ej: 5! = 120).
"""

def calcular_factorial_de_un_numero(num1): #Definimos la función
    resultado = 1 # le damos un valor inicial al resultado para evitar errores
    for i in range(1, num1 + 1):
        resultado = resultado * i
        """
        1*1=1 / 1*2=2 / etc
        """

    print(resultado)

calcular_factorial_de_un_numero(5)