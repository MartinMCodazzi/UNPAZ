# Martín Nahuel Muñoz Codazzi
# 23/09/2022

"""
Hacer un algoritmo que permita ingresar diez (10) números, luego muestre por
pantalla cuántos eran mayores a cero y cuántos son menores a cero.
"""
mayoresACero = 0
menoresACero = 0

for i in range(10):
    numero = int(input("Ingrese un número :"))
    print("*"*25)
    if (numero > 0):
        mayoresACero += 1
    elif (numero < 0):
        menoresACero += 1

print("En la tanda ingresada, se ingresaron",mayoresACero,"números mayores a 0")
print("En la tanda ingresada, se ingresaron",menoresACero,"números menores a 0")

exit(0)
