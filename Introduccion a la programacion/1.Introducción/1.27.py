# Martin Nahuel Muñoz Codazzi
# 15/08/2022

numero_uno = float(input('Ingrese un número :'))
numero_dos = float(input('Ingrese otro número :'))

if numero_uno < numero_dos:
    print(numero_uno,'es menor que',numero_dos)
elif numero_dos < numero_uno:
    print(numero_dos,'es menor que',numero_uno)
else:
    print('Los números son iguales')

exit(0)