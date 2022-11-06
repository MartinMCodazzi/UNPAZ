# 5/11/2022
# Martín Nahuel Muñoz Codazzi

"""Dado un vector de 10 posiciones se debe reemplazar los valores impares con una 0"""

import array, random
#Inicializo variables
vectorOrigen = array.array("i",range(10))
vectorDestino = array.array("i",range(10))

#Carga del vector
for i in range(len(vectorOrigen)):
    #miVector[valor] = int(input(f"Ingrese el valor número {valor + 1} :"))
    vectorOrigen[i] = int(random.random() * 100)

#Proceso el vector
for i in range(len(vectorOrigen)):
    if (vectorOrigen[i] % 2 == 0 ):
        vectorDestino[i] = vectorOrigen[i]
    else:
        vectorDestino[i] = 0

# Imprimo resultado
print(vectorOrigen)
print(vectorDestino)
