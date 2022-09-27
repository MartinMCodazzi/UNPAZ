# Martin Nahuel Muñoz Codazzi
# 27/09/2022

"""
2.19 Hacer un algoritmo que permita ingresar por pantalla cinco (5) números y luego
calcular su media.
"""

acumulador = 0
for i in range(5):
    acumulador += int(input("Ingrese 5 números para calcular su media :"))
print("La media de los números ingresados es:",acumulador/5)

exit(0)