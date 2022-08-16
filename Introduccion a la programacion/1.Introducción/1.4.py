# Martin Nahuel Muñoz Codazzi
# 15/08/2022

numero_uno = int(input('ingrese el primer número :'))
numero_dos = int(input('ingrese el segundo número :'))

while numero_dos == 0 :
    print("\nel segundo número no puede ser cero")
    numero_dos = int(input('ingrese el segundo número :'))

print('\nla suma entre' , numero_uno , 'y' , numero_dos , 'da como resultado', numero_uno + numero_dos)
print('la resta entre' , numero_uno , 'y' , numero_dos , 'da como resultado', numero_uno - numero_dos)
print('la multiplicación entre' , numero_uno , 'y' , numero_dos , 'da como resultado', numero_uno * numero_dos)
print('la división entre' , numero_uno , 'y' , numero_dos , 'da como resultado', numero_uno / numero_dos)

exit(0)