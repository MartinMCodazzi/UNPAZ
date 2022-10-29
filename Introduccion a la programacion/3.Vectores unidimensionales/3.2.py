# Martin Muñoz Codazzi
# 23/10/2022

"""
Desarrollar un algoritmo que permita la carga de un vector de 10 posiciones.
Generar una rutina que transcriba el contenido del vector a otro vector en orden
inverso.
"""

import array, random

array1 = array.array("i",range(10))
array2 = array.array("i",range(10))

for valor in array1:
    #array1[valor] = int(input(f"Ingrese el valor número {valor + 1} :"))
    array1[valor] = int(random.random() * 100)

for i in range(len(array2)-1,-1,-1):
    array2[i] = array1[len(array1) - i-1]

print(array1)
print(array2)