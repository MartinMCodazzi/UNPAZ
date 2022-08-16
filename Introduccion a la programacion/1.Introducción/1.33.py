# Martin Nahuel Muñoz Codazzi
# 15/08/2022

nombre = input('Ingrese el nombre del empleado :')
antiguedad = int(input('Ingrese la antiguedad del empleado :'))
valorHora = float(input('Ingrese el valor hora del empleado :$'))
horasTrabajadas = float(input('Ingrese la cantidad de horas trabajadas en el mes :'))

bruto = horasTrabajadas * valorHora + antiguedad * 30
print('\n******************************')
print('Recibo de sueldo de:',nombre)
print('Antiguedad:',antiguedad,'años')
print('******************************')
print('Total a cobrar en bruto :$',bruto)
print('Total descuentos (13%) :$',bruto*0.13)
print('******************************')
print('Total a cobrar :$',bruto - bruto*0.13)

exit(0)