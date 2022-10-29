# 28/10/2022
# Martin Nahuel Muñoz Codazzi

"""
Crear un programa con un vector de 5 posiciones que lea todas las posiciones y
luego imprima el doble de los valores leídos en cada una de sus posiciones.
"""

import array, random
#Inicializo variables
miVector = array.array("i",range(5))
miVector2 = array.array("i",range(5))

#Carga del vector
for i in range(len(miVector)):
    #miVector[valor] = int(input(f"Ingrese el valor número {valor + 1} :"))
    miVector[i] = int(random.random() * 100)

#Proceso
for i in range(len(miVector)):
    miVector2[i] = miVector[i] * 2

#Informe del resultado
print(miVector)
print(miVector2)