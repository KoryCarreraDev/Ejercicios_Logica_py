"""
Par o Impar — Determina si un número ingresado es par o impar.
"""

def verificar_par_impar(num1):
    division = num1 % 2

    if division == 0:
        return "par"
    else:
        return "impar"

print("Ingrese un numero para verificar si es par o impar")

numero = int(input("Numero: "))

resultado = verificar_par_impar(numero)

print(resultado)