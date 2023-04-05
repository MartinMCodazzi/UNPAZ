# Martín Nanhuel Muñoz Codazzi
# 20/03/2023

import numpy as np

#Al declararlos, deben tener el mismo "ancho", ya que cada elemento que se declara es una fila
#Si no se respeta esto, arrojará error
#miArray = np.matrix([[1,2,3],[1,2,3]],dtype=int) #Esto no me funcionó
#print (miArray)

#Si se declara con range, no se tiene que usar corchetes para encerrarlos
miArray = np.matrix([range(4),range(4)],dtype=int)
print (len(miArray))
