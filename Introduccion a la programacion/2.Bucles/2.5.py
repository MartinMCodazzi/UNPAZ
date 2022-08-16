# Martin Nahuel Muñoz Codazzi
# 15/08/2022

resultado = ''
numero = int(input('Ingrese un número entero y positivo :'))

for i in range(numero):
    if i % 2 != 0 :
        resultado = resultado + str(i) + ','

print(resultado[:-1])

exit(0)