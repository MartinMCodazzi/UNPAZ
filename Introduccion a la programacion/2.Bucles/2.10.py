# Martín Nahuel Muñoz Codazzi
# 21/09/2022

"""
2.10.
Dado un número natural x, contar la cantidad de dígitos que posee.
Realizarlo mediante
A) método matemático (división sucesiva de 10)
B) Uso de la función len
C) Uso del ciclo for.

"""
numeroA = 0
contadorA = 0

try:
    numero = int(input("Ingrese un número: "))
    if numero < 0:
        raise Exception
except:
    print("Se debe ingresar un número natural")
else:
    numeroA = numero
    while numeroA >= 10:
        numeroA /= 10
        contadorA += 1
         
    print("Usando el método matemático,",numero,"tiene",contadorA + 1,"dígito/s")
    print("Usando el método len()",numero,"tiene",len(str(numero)),"digito/s")

exit(0)