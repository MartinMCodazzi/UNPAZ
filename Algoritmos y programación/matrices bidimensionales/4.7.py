# 17/4/2023
# Martin Nahuel Muñoz Codazzi

"""
Efectuar un programa en C el cual permita la carga de una matriz de 3x3 desde
teclado. A esta matriz la llamaremos MatOrigen.
Una vez cargada la matriz, obtener como resultado un vector de 2 posiciones al que
llamaremos VecDestino, el cual deberá alojar en la posición 0 la SUMA de los
valores origen Impares y en la posición 1 la suma de los valores origen pares.
Mostrar el resultado de Vecdestino por pantalla.
"""
import numpy as np
import array,random

matOrigen = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]],dtype=int) # 3x3
vecDestino = array.array('i',[0,0])

def cargaMatriz(matriz):
    for filas in range(len(matriz)):
        for columnas in range(len(matriz[0])):
            matriz[filas][columnas] = random.randrange(1,10) 

def calcularVector(matriz,vector):
     for filas in range(len(matriz)):
        for columnas in range(len(matriz[0])):
            if matriz[filas][columnas] % 2 == 0: # pares
                vector[0] += matriz[filas][columnas] # suma pares
            else: # impares
                vector[1] += matriz[filas][columnas] # suma impares

### PROGRAMA PRINCIPAL ###
cargaMatriz(matOrigen)
calcularVector(matOrigen,vecDestino) # Calcula el vector de destino.
print(matOrigen)
print(f'Los pares en la matriz de origen suman {vecDestino[0]}.\nmientras que los impares suman {vecDestino[1]}.')