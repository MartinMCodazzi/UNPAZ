# Martin Nahuel Muñoz Codazzi
# 15/08/2022

numero_uno = float(input('Ingrese el tiempo del auto 1 :'))
numero_dos = float(input('Ingrese el tiempo del auto 2 :'))

if numero_uno > numero_dos:
    print('el auto 1 llegó primero')
elif numero_uno < numero_dos:
        print('el auto 2 llegó primero')
else:
    print('Los autos llegaron al mismo tiempo')

exit(0)