# 28/10/2022
# Martin Nahuel Muñoz Codazzi

"""
Diseñe un programa que lea un vector de 10 posiciones, luego determine la primera
posición que contenga un número múltiplo de 3. En caso que no lo contenga deberá
informar por pantalla “No existe”
"""

import array, random
#Inicializo variables
miVector = array.array("i",range(10))
posicion = False

#Carga del vector
for i in range(len(miVector)):
    #miVector[valor] = int(input(f"Ingrese el valor número {valor + 1} :"))
    miVector[i] = int(random.random() * 10)

#Evaluacion
for i in range(len(miVector)):
    if (miVector[i] % 3 == 0):
        posicion = i
        break

#Informe del resultado
print(miVector)
if posicion:
    print(f"El primer múltiplo de 3 es {miVector[posicion]}, el cual está en la posición {posicion}")
else:
    print("No existe múltiplo de 3 en el vector cargado")