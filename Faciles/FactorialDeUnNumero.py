"""
Factorial — Calcula el factorial de un número N (ej: 5! = 120).
"""

def calcular_factorial_de_un_numero(num1): #Definimos la función
    resultado = 1 # le damos un valor inicial al resultado para evitar errores
    for i in range(1, num1 + 1): #Le damos rango +1 a la i para alcanzar al numero original e iterar lo necesario
        resultado = resultado * i #1*1=1 / 1*2=2 / etc

    print(resultado) #Imprimimos el resultado en pantalla

calcular_factorial_de_un_numero(5) #Prueba