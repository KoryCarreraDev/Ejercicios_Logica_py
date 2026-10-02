"""
Validar contraseña — Mínimo 8 caracteres, una mayúscula, una minúscula y un número.
"""

def validar_contrasena(contrasena):
    contrasena_limpia = contrasena.strip() #Quitamos espacios a inicio y final
    tiene_8_caracteres = False if len(contrasena_limpia) < 8 else True #Validamos los 9 caracteres
    #Cumple el resto
    tiene_mayuscula = False 
    tiene_minuscula = False
    tiene_numero = False
    cumple = False

#Recorremos letra a letra haciendo las validaciones
    for c in contrasena_limpia:
        tiene_numero = True if c.isdigit() else tiene_numero
        if c.isupper():
            tiene_mayuscula = True
        elif c.islower():
            tiene_minuscula = True

    #Validamos que si todo es correcto, pasamos el "cumple"
    cumple = True if tiene_8_caracteres == True and tiene_mayuscula == True and tiene_minuscula == True and tiene_numero == True else False
    
    return cumple

print('Escriba su contraseña segura para el sistema')

contrasena = input('Ingrese su contrasena: ')

segura_insegura = validar_contrasena(contrasena)

if segura_insegura == True:
    print("¡Su contraseña es segura!")
else:
    print("¡Contraseña insegura!")