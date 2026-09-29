"""
Contador de vocales — Pide una palabra y cuenta cuántas vocales tiene
"""

def contar_vocales_palabra(palabra):
    letras = list(palabra) #Separamos la palabra en letras con una funcion interna de python
    total_letras = len(letras) #Calculamos su cantidad de indices (se cuentan y suman, no trae el ultimo indice)

    vocales = ["a", "e", "i", "o", "u"] #Definimos las vocales
    vocales_totales = 0 #Inicializamos en 0 una variable donde guardaremos las vocales totales

    for let in letras: #Recorremos letra por letra 
        for x in range(5): #cantidad de indices en el array de vocales (Empezando desde 0)
            vocales_totales = vocales_totales + 1 if let == vocales[x] else vocales_totales #Si coincide, +1 en vocales totales, si no, conserva el valor
    
    print(vocales_totales) #Mostramos en pantalla

contar_vocales_palabra("esternocleidomastoideo") #Prueba de la función
