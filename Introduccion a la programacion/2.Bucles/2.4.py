# Martin Nahuel Muñoz Codazzi
# 15/08/2022

palabra = input('Ingrese una palabra que será repetida :')

for i in range(10):
    print(i,'(for)',palabra)

print('***********************************************')

veces = 1
while veces <= 10:
    print(veces,'(while)',palabra)
    veces += 1

exit(0)