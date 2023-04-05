# 04/04/2023
# Martín Nahuel Muñoz Codazzi

"""
Efectuar la carga de una matriz de 3x2 desde teclado. Obtener como resultado la
matriz transpuesta. Mostrarla por pantalla.
"""
import numpy as np
import random

#Defino funciones

def UDFCargaMatriz(matriz, randomizado = False ):    
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if not randomizado:
                matriz[fila][columna] = int(input("Ingrese un número :"))
            else:
                matriz[fila][columna] = int(random.random() * 10)

def UDFMultiplicacionMatrices(matrizA, matrizB, matrizResultado):
    sumatoria = 0
    for fila in range(len(matrizA)):
        for columna in range(len(matrizA[0])):
            for auxiliar in range(len(matrizA)):
                sumatoria += matrizA[fila][auxiliar] * matrizB[auxiliar][columna] #AHHH LPM!!!                
            matrizResultado[fila][columna] = sumatoria
            sumatoria = 0

def UDFMuestraMatriz(matriz):
    for fila in range(len(matriz)):        
        for columna in range(len(matriz[0])):        
            print(matriz[fila][columna],end="|")      
        print("\n")

#Programa principal

miMatriz = np.zeros(shape=(3,3),dtype=int)
miSegundaMatriz = np.zeros(shape=(3,3),dtype=int)
miResultadoMatriz = np.zeros(shape=(3,3),dtype=int)

UDFCargaMatriz(miMatriz,True)
UDFCargaMatriz(miSegundaMatriz,True)
print("Primer matriz:")
UDFMuestraMatriz(miMatriz)
print("Segunda matriz:")
UDFMuestraMatriz(miSegundaMatriz)
UDFMultiplicacionMatrices(miMatriz,miSegundaMatriz,miResultadoMatriz)
print("Matriz resultado:")
UDFMuestraMatriz(miResultadoMatriz)