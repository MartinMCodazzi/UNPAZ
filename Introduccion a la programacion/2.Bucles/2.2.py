# Martin Nahuel Muñoz Codazzi
# 15/08/2022

while True:
    print('\n**********************************')
    print('Ingrese dos números, si ambos son iguales, se interrumpe el ciclo')
    numero1 = int(input('Primer número :'))
    numero2 = int(input('Segundo número :'))
    if numero1 == numero2:
        break
    if numero1 < numero2:
        print(numero1,'es menor')
    else:
        print(numero2,'es menor')

exit(0)