"""
Promedio — Pide N números y calcula su promedio.
"""

def promedio_de_n_numeros(numeros):

    cantidad_registros = len(numeros)
    suma_registros = 0

    for let in numeros:
        suma_registros = suma_registros + let

    promedio = suma_registros / cantidad_registros

    print(promedio)

string = input("Ingrese los numeros que desea promediar separados por una coma y un espacio (2, 3): ")

array = string.split(", ")

array_numb = []

for let in array:
    array_numb.append(int(let))

promedio_de_n_numeros(array_numb)
