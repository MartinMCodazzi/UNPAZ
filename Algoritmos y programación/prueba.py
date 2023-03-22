
import numpy as np

#Al declararlos, deben tener el mismo "ancho", ya que cada elemento que se declara es una fila
#Si no se respeta esto, arrojará error
miArray = np.matrix([[1,2,3],[1,2,3]],dtype=int)

rng = np.random.default_rng()
arrayPrueba = rng.integers(low=0, high=1000, size=(3,5))

print(arrayPrueba)