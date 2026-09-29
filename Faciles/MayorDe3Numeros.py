"""
Mayor de tres números — Dados tres números, indica cuál es el mayor (sin usar max()).
"""


def mayor_tres_numeros(num1, num2, num3): #Definimos la función
    numero_alto = num1 if num1 > num2 else num2 #encontramos el numero mas alto entre los dos primeros numeros y lo guardamos en una variable

    numero_mayor = num3 if num3 > numero_alto else numero_alto #Comparamos con el 3 luego dejamos el mas alto en la variable

    return numero_mayor #Retornamos el numero mayor


num1 = int(input("Ingrese el primer numero: ")) #Input #1

num2 = int(input("Ingrese el primer numero: ")) #Input #2

num3 = int(input("Ingrese el primer numero: ")) #Input #3

resultado = mayor_tres_numeros(num1, num2, num3) #Llamamos a la función

print(resultado) #Imprimimos el resultado en terminal