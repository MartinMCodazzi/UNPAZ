# Martin Nahuel Muñoz Codazzi
# 15/08/2022

extras = 0
horas = int(input('Ingrese las horas trabajadas :'))
precio = float(input('Ingrese el valor hora : $'))

if horas > 40:
    extras = horas - 40
    horas = 40

print('la paga que corresponde es $', horas * precio + extras * (precio * 1.5))

exit(0)