# Martin Nahuel Muñoz Codazzi
# 15/08/2022

numero_uno = float(input('Ingrese un precio :$'))
numero_dos = float(input('Ingrese otro precio :$'))

if numero_uno > numero_dos:
    print(numero_uno,'es mayor que',numero_dos)
elif numero_uno < numero_dos:
    print(numero_dos,'es mayor que',numero_uno)
else:
    print('Los números son iguales')

exit(0)