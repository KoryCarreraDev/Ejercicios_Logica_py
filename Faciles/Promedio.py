"""
Promedio — Pide N números y calcula su promedio.
"""

def promedio_de_n_numeros(numeros): #Definimos la función

    cantidad_registros = len(numeros) #Obtenemos la cantidad de datos del array (empieza desde el 1)
    suma_registros = 0 #Inicializamos una variable para asignarle valor mas adelante (en 0 para no alterar resultado)

    for num in numeros: #Recorremos el array con los numeros del usuario
        suma_registros = suma_registros + num #Sumamos registro por registro

    promedio = suma_registros / cantidad_registros #Se calcula el promedio haciendo total sobre cantidad de registros

    print(promedio) #Se imprime en pantalla

string = input("Ingrese los numeros que desea promediar separados por una coma y un espacio (2, 3): ") #Se solicita al usuario los numeros

array = string.split(", ") #se divide con el patron de ", " para separar los numeros

array_numb = [] #Inicializamos un array vacio para luego guardar los strings transformados a numeros

for num in array: #Recorremos el array separado por comas y espacio
    array_numb.append(int(num)) #Empujamos el string separado transformado en int

promedio_de_n_numeros(array_numb) #Ejecutamos la función
