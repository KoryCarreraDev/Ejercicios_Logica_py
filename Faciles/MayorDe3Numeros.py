"""
Mayor de tres números — Dados tres números, indica cuál es el mayor (sin usar max()).
"""


def mayor_tres_numeros(num1, num2, num3):
    numero_alto = num1 if num1 > num2 else num2

    numero_mayor = num3 if num3 > numero_alto else numero_alto

    return numero_mayor


num1 = int(input("Ingrese el primer numero: "))

num2 = int(input("Ingrese el primer numero: "))

num3 = int(input("Ingrese el primer numero: "))

resultado = mayor_tres_numeros(num1, num2, num3)

print(resultado)