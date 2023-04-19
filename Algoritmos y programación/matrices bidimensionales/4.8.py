# 18/04/2023
# Martin Nahuel Muñox Codazzi
"""
Dada una matriz de 3X4, desarrollar un programa que solicite al usuario el ingreso
de números enteros. Al finalizar se obtiene la suma de todos los números positivos
ingresados y la suma de los números negativos.
"""
import random
import numpy as np

def cargaMatriz(matriz):
    for fila in (range(len(matriz))):
        for columna in range(len(matriz[0])):
            matriz[fila][columna] = int(random.randrange(-10,10)) 

def procesarMatriz(matriz):
    positivos = 0
    negativos = 0
    for fila in (range(len(matriz))):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] > 0: 
                positivos += matriz[fila][columna] # Suma de valores positivos.
            else:
                negativos += matriz[fila][columna] # Suma de valores negativos.

    print(f'La suma de los numeros positivos es: {positivos} \nMientras que la suma de los negativos es {negativos}')



matriz = np.zeros((3,4)) 
cargaMatriz(matriz)
print(matriz) 
procesarMatriz(matriz)