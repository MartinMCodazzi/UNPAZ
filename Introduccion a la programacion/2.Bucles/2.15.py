# Martín Nahuel Muñoz Codazzi
# 23/09/2022

"""
Hacer un algoritmo que se ingrese 10 letras. Mostrar cuál es la mayor letra
ingresada.
"""

mayor = input("Ingrese un caracter :").lower()[0]
for i in range(9):
    caracter = input("Ingrese un caracter :").lower()[0]
    if caracter > mayor:
        mayor = caracter
print("El caracter más grande ingresado fue :",mayor)

exit(0)
