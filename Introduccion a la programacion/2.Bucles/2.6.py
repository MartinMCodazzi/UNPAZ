# Martin Nahuel Muñoz Codazzi
# 15/08/2022

resultado = ''
numero = int(input('Ingrese un número entero positivo :'))

for i in range(numero,-1,-1):
    resultado = resultado + str(i) + ','

print(resultado[:-1])

exit(0)