# Martin Nahuel Muñoz Codazzi
# 21/09/2022

try:
    numero = int(input("Ingrese un número: "))
except:
    print("Ocurrió un error, vuelva a ingresar un número")
else:
    print("El último dígito ingresado, usando el método de slicing es:", str(numero)[-1:])
    print("El último dígito ingresado, usando el método matemático es:", numero % 10)

""" 
    while (numero >= 10):
        numero = numero % 10
    
    print("El último dígito ingresado, usando el método matemático es:", numero)
"""

exit(0)