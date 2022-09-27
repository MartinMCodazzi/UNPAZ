# Martin Nahuel Muñoz Codazzi
# 27/09/2022

"""
2.23.Hacer un algoritmo que permita ingresar por pantalla números naturales al finalizar
informar:
● ¿Cuántos están entre el 50 y 75, ambos inclusive?
● ¿Cuántos mayores de 80?
● ¿Cuántos menores de 30?
El algoritmo debe finalizar cuando se ingresa el número 0.
"""
acumulador1 = 0
acumulador2 = 0
acumulador3 = 0

while True :
    numero = int(input("Ingrese un número, para finalizar, ingrese 0 :"))
    if ((numero >= 50) and (numero <= 75)):
        acumulador1 += 1
    elif (numero > 80):
        acumulador2 += 1
    elif ((numero < 30) and (numero > 0)):
        acumulador3 += 1
    elif (numero == 0):
        break
    
print("Se ingresaron",acumulador1,"números entre 50 y 75 inclusive")
print("Se ingresaron",acumulador2,"números mayores a 80")
print("Se ingresaron",acumulador3,"menores a 30")

exit(0)
