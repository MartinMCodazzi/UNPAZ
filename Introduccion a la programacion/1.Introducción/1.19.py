# Martin Nahuel Muñoz Codazzi
# 15/08/2022

pares = 0

while True:
    ingreso = int(input('Ingrese los pares de zapatillas, 0 para salir :'))
    if ingreso == 0:
        break
    pares += ingreso
    
print('Se tienen',pares,'pares de zapatillas')

exit(0)