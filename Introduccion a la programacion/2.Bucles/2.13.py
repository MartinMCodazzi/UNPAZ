# Martín Nahuel Muñoz Codazzi
# 23/09/2022

"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, # y
muestre por pantalla el número de veces que aparece la letra en la frase.
"""

frase = input("Ingrese una frase :").lower()
letra = input("Ingrese una letra :").lower()
letra = letra[0]
veces = 0

for i in range(0,len(frase)):
    if (letra == frase[i]):        
        veces += 1

if (veces != 1):
    print("La letra",letra,"aparece",veces,"veces en",frase)
else:
    print("La letra\"",letra,"\"aparece",veces,"vez en",frase)

exit(0)