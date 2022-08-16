# Martin Nahuel Muñoz Codazzi
# 15/08/2022

letra_uno = input('Ingrese una letra :')
letra_dos = input('Ingrese otra letra :')

if letra_uno[0] < letra_dos[0]:
    print('El orden es :',letra_uno[0],letra_dos[0])
else:
    print('El orden es :',letra_dos[0],letra_uno[0])

exit(0)
