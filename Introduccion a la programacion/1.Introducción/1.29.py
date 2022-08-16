# Martin Nahuel Muñoz Codazzi
# 15/08/2022

from math import sqrt

cateto1 = float(input('Ingrese la logitud del cateto adyacente :'))
cateto2 = float(input('Ingrese la logitud del cateto opuesto :'))

print('La hipotenusa mide', sqrt((cateto1 ** 2) + (cateto2 ** 2)))

exit(0)
