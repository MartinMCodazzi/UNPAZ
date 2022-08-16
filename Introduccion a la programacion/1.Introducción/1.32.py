# Martin Nahuel Muñoz Codazzi
# 15/08/2022

lado1 = int(input('Ingrese la longitud del primer lado (menor) :'))
lado2 = int(input('Ingrese la longitud del segundo lado (menor) :'))
lado3 = int(input('Ingrese la longitud del tercer lado (mayor):'))


if (lado1 + lado2) >= lado3:
    if (lado1 == lado2) and (lado2 == lado3) :
        print('El triángulo es equilátero')
    elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
        print('El triángulo es isósceles')
    else:
        print('El triángulo es escaleno')
else:
    print('Los números ingresados no corresponden a un triángulo')

