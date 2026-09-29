"""
Suma del 1 al 100 — Calcula la suma de todos los números del 1 al 100 usando un bucle.
"""

def suma_del_1_al_100(): #Definimos la función

    resultado_final = 0 #Inicializamos una variable con valor 0
    for i in range(1, 101): #Iteramos sobre x empezando desde uno hasta el 100 "(1,101)"
        resultado_final = resultado_final + i #Resultado anterior + nuevo numero

    print(resultado_final) #Lo imprimimos en terminal

suma_del_1_al_100() #llamamos la función