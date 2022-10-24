# Martin Muñoz Codazzi
# 23/10/2022

"""
Realizar un programa que cargue un vector de 15 posiciones.
"""

import array as arr

# array1 recibe 15 enteros
array1 = arr.array("i",range(15))

# Aprovecho que lo cargué con un range para usarlo como indice
for valor in array1:
    array1[valor] = int(input(f"Ingrese el valor número {valor +1} :"))

print(array1)