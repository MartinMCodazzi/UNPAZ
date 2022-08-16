# Martin Nahuel Muñoz Codazzi
# 15/08/2022

numero_uno = int(input('Ingrese un número :'))
numero_dos = int(input('Ingrese otro número :'))

if ((numero_uno % 3) == 0) or ((numero_dos % 3) == 0):
    print('Alguno de los números es divisible por 3')
else:
    print('Ninguno de los números es divisible por 3')

exit(0)