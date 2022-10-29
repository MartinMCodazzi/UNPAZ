# 28/10/2022
# Martin Nahuel Muñoz Codazzi

"""
Crear un programa con un vector ORIGEN de 10 posiciones que lea todas las
posiciones y luego traslade el doble de los valores en aquellas posiciones impares a
otro vector DESTINO.
"""

import array, random
#Inicializo variables
vectorOrigen = array.array("i",range(10))
vectorDestino = array.array("i",range(10))

#Carga del vector
for i in range(len(vectorOrigen)):
    #miVector[valor] = int(input(f"Ingrese el valor número {valor + 1} :"))
    vectorOrigen[i] = int(random.random() * 100)

#Proceso
#Lo informo ahora porque al igualarlos, se pasan por referencia
print (vectorOrigen)
vectorDestino = vectorOrigen
for i in range(len(vectorOrigen)):
    if (i % 2 != 0):      
        vectorDestino[i] = vectorDestino[i] * 2

#Informo
print(vectorDestino)
