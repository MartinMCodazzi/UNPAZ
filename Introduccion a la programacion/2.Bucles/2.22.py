# Martin Nahuel Muñoz Codazzi
# 27/09/2022

"""
Hacer un algoritmo que pida la nota de un examen (un no real entre 0 y 10) muestre
por pantalla la calificación de la siguiente forma:
● Si la nota es menor que 5 la leyenda “En suspenso”
● Si la nota se encuentra entre 5 inclusive y 7 sin incluir la leyenda
“Aprobado”
● Si la nota se encuentra entre 7 inclusive y 9 sin incluir la leyenda
“Notable”
● Si la nota se encuentra entre 9 inclusive y 10 sin incluir la leyenda
“Sobresaliente”
● Si la nota es un 10 la leyenda “Matrícula de honor” .
Terminar el algoritmo cuando se ingresa cero como nota. En caso que no, vuelve a
pedir una nota.
"""

nota = 1
while nota != 0 :
    nota = float(input("Ingrese la nota :"))
    if ((nota > 0) and (nota < 5)):
        print("En suspenso")
    elif ((nota >= 5) and (nota < 7)):
        print("Aprobado")
    elif((nota >= 7) and (nota < 9)):
        print("Notable")
    elif((nota >= 9) and (nota < 10)):
        print("Sobresaliente")
    elif(nota == 10):
        print("Matrícula de honor")
    elif(nota == 0):
        print("Gracias!")
    else:
        print("Fuera de rango, debe introducir de 1 a 10, ingrese 0 para salir")

exit(0)