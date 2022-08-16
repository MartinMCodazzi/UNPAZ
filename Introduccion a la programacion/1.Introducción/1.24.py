# Martin Nahuel Muñoz Codazzi
# 15/08/2022

numero_uno = int(input('Ingrese el primer número :'))
numero_dos = int(input('Ingrese el segundo número :'))
numero_tres = int(input('Ingrese el tercer número :'))

if (numero_uno < numero_dos) and (numero_dos < numero_tres):
    print('Los números fueron ingresados de menor a mayor')
else:
    print('Los números no fueron ingresados de menor a mayor')

exit(0)