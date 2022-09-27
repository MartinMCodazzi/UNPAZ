# Martin Nahuel Muñoz Codazzi
# 27/09/2022

"""
2.20 Hacer un algoritmo que se ingresan 50 números enteros, calcular cuántos números
impares se ingresaron
"""
acumulador = 0
for i in range(50):
    numero = int(input("Ingrese un número :"))
    if ((numero % 2) != 0):
        acumulador += 1
print("Se ingresaron", acumulador, "números impares")

exit(0)