"""
Suma de dos números — Pide dos números y muestra su suma.
"""

def suma_de_dos_numeros(num1, num2):
    return num1 + num2

print("Hola desde Python, porfavor coloque los numeros que desea sumar")

numero1 = int(input("Primer numero: "))
numero2 = int(input("Segundo numero: "))

resultado = suma_de_dos_numeros(numero1, numero2)

print(resultado)