# Martin Nahuel Muñoz Codazzi
# 27/09/2022

"""
2.21 Hacer un algoritmo que se ingresan 20 números enteros, calcular cuántos números
impares y cuántos números pares fueron ingresados
"""

acumuladorPares = 0
acumuladorImpares = 0
for i in range(20):
    numero = int(input("Ingrese un número :"))
    if ((numero % 2) == 0):
        acumuladorPares += 1
    else:
        acumuladorImpares += 1

print("Se ingresaron", acumuladorImpares, "números impares")
print("Se ingresaron", acumuladorPares, "números pares")


exit(0)