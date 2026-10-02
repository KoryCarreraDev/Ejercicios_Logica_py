"""
Número invertido — Dado un número (ej: 1234), muéstralo invertido (4321)
"""

def invertir_un_numero(numero): #Definimos la función

    caracteres = list(str(numero)) #Transformamos en string y en lista al numero entregado
    longitud = len(caracteres) - 1 #Calculamos la longitud del array y le restamos 1 para obtener sus indices
    array_ordenado = [] #Inicializamos un array vacio

    for c in caracteres: #recorremos los numeros extraidos
        array_ordenado.append(caracteres[longitud]) #Metemos de atras hacia adelante en el array usando longitud -1
        longitud = longitud - 1 #Restamos 1 a la longitud para obtener el siguiente dato

    texto_ordenado = "".join(array_ordenado) #Integramos los numeros a un string usando .join y sin espacios

    print(int(texto_ordenado)) #Imprimimos en pantalla 

numeros = int(input("Ingrese el numero que desa invertir: ")) #Solicitamos el input y de una lo transformamos en int

invertir_un_numero(numeros) #Llamamos y ejecutamos