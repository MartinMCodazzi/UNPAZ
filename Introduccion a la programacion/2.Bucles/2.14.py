# Martín Nahuel Muñoz Codazzi
# 23/09/2022

"""
Dado un número natural x, contar la cantidad de dígitos pares e impares que posee.
"""

pares = 0
impares = 0

while True:
    try:
        numero = int(input("Ingrese un número natural :"))
        if numero <= 0:
            raise Exception        
        numero = str(numero)
    except:
        print("Debe ingresar un número natural")
    else:
        for i in range(len(numero)):
            if ((int(numero[i]) % 2) == 0):
                pares += 1
            else:
                impares += 1
        print("La cantidad de dígitos pares en",numero,"es",pares)
        print("La cantidad de dígitos impares en",numero,"es",impares)
        break

exit(0)    