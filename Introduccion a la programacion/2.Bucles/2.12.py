# Martín Nahuel Muñoz Codazzi
# 23/09/2022

"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
una a una las letras de la palabra introducida empezando por la última.
"""

texto = input("Ingrese un texto :")

for i in range(len(texto),0,-1):
    print(texto[i-1])