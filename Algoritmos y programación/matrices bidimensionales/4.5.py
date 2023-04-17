# 16/04/2023
# Martín Nahuel Muñoz Codazzi
# Ayudado por CodeWhisperer

"""
Desarrollar una matriz de 3X3. Ingresar números enteros. Solicitar al usuario que
ingrese un número de fila y obtener el número mayor ingresado en dicha fila.
"""

import numpy as np
import random


def cargamatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = random.randint(1, 100)

def mayorfila(matriz, fila):
    mayor = matriz[fila][-1]
    for i in range(len(matriz) -1 ):
        if matriz[fila][i] > mayor:
            mayor = matriz[fila][i]
    return mayor

def imprimirmatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" | ")
        print()


### PROGRAMA PRINCIPAL ###
matriz = np.zeros((3, 3), dtype=int)
cargamatriz(matriz)
while True:
    try:
        fila = int(input("Ingrese un nÃ®mero de fila: "))
        if fila < 0 or fila > 3:
            raise ValueError             
    except ValueError:
       print("Ingrese un nÃ®mero de fila entre 1 y 3")
    else:
        break
print(f'el mayor número cargado en la fila {fila} es {mayorfila(matriz, fila -1)}')
imprimirmatriz(matriz)



