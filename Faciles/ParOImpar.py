"""
Par o Impar — Determina si un número ingresado es par o impar.
"""

def verificar_par_impar(num1): #Definimos la función
    division = num1 % 2 #Residuo del numero (Cualquier numero par, dividido por 2 su residuo será 0)

    if division == 0: #Comprobamos si es igual a 0 (Par)
        return "par" 
    else:   #Devolvemos el tipo de numero que corresponda (Par o Impar)
        return "impar"

print("Ingrese un numero para verificar si es par o impar")

numero = int(input("Numero: "))

resultado = verificar_par_impar(numero)

print(resultado)