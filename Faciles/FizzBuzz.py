"""
FizzBuzz — Imprime del 1 al 100, pero: Divisible por 3 → "Fizz", Divisible por 5 → "Buzz" Divisible por ambos → "FizzBuzz"
"""

def fizzbuzz(): #Definimos la función
    resultado = [] #Inicializamos un array vacio
    
    for i in range(1, 101): #Recorremos los numeros del 1 al 100
        F_and_B = "FizzBuzz" if i % 3 == 0 and  i % 5 == 0 else i #Primeramente validamos si cumple ambas condiciones

        if isinstance(F_and_B, str): #Validamos si es string (si devuelve string es FizzBuzz, si no, continuamos)
            resultado.append(F_and_B) #Insertamos el dato
        elif isinstance(F_and_B, int): #Validamos de que sea int 
            F_and_B = "Fizz" if i % 3 == 0 else ("Buzz" if i % 5 == 0 else i) #Comprobamos Fizz y Buzz
            resultado.append(F_and_B) #Insertamos el dato
    
    print(resultado) #Imprimimos el resultado

fizzbuzz() #Ejecutamos

