"""
Suma del 1 al 100 — Calcula la suma de todos los números del 1 al 100 usando un bucle.
"""

def suma_del_1_al_100():

    resultado_final = 0
    for i in range(1, 101):
        resultado_final = resultado_final + i

    print(resultado_final)

suma_del_1_al_100()