# Martin Nahuel Muñoz Codazzi
# 15/08/2022

pares = 0

print('Ingrese 10 números, al finalizar indicaré cuántos de estos son pares')
for i in range(10):
    numero = int(input())
    if (numero % 2) == 0:
        pares += 1
    
print('La cantidad de números pares ingresados es :',pares)

exit(0)