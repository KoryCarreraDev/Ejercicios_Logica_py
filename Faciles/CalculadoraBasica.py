"""
Calculadora básica — Suma, resta, multiplicacion y division usando funciones separadas.
"""

import re #Importamos Regex

#Definimos las funciones de operación

def suma(a, b): 
    return a + b

def multiplicacion(a, b):
    return a*b

def resta(a, b):
    return a - b

def division(a, b):
    return a / b

#Especificamos los operadores permitidos
print("Operadores permitidos: +, -, / y x")

#Recibimos el input
operacion = input('Ingrese una operacion sencilla (Suma, resta, division y multiplicacion) de dos numeros, ejem "2x5": ')

#creamos un array con los operadores permitidos
operadores = ['+', '-', '/', 'x']

#Separar la operacion por signos y conselvar el signo
array_operación = re.split(r"([+/x-])", operacion)

#Verificamos la longitud para identificar termino, operador, termino
if len(array_operación) != 3:
    print("Datos Insuficientes")
    exit()

#Verificamos que el operador sea valido
if(array_operación[1] not in operadores):
    print("Operación invalida")
    exit()

#tratamos de transformar los terminos en int, si no, lanza excepción
try:
    array_ordenado = [int(array_operación[0]), array_operación[1], int(array_operación[2])]
except:
    print('¡Numeros no validos!')
    exit()

#Operamos segun el signo
if array_ordenado[1] == '+':
    resultado = suma(array_ordenado[0], array_ordenado[2])
    print(resultado)

elif array_ordenado[1] == '-':
    resultado = resta(array_ordenado[0], array_ordenado[2])
    print(resultado)

elif array_ordenado[1] == 'x':
    resultado = multiplicacion(array_ordenado[0], array_ordenado[2])
    print(resultado)

else:
    resultado = division(array_ordenado[0], array_ordenado[2])
    print(resultado)
