# 16/04/2023
# Martín Nahuel Muñoz Codazzi

"""
Se debe cargar las notas de un examen realizado a 10 alumnos. Realizar un
algoritmo que muestre el promedio del grupo y los nombres de los alumnos que tienen
una nota por debajo del promedio.
    Matricula
    Apellido y nombre del alumno
    Nota
"""

class TDAEstudiante:

    def __init__ (self, matricula, apellido, nombre, nota):
        self.matricula = self.checkParam("matricula", matricula, "str")
        self.apellido = self.checkParam("apellido", apellido, "str", 25)
        self.nombre = self.checkParam("nombre", nombre, "str",25)
        self.nota = self.checkParam("nota", nota, "float")

    def checkParam(self, nombreParam, param, tipo, largo=0):
        while True:
            try:
                match tipo:
                    case "int":
                        int(param)
                    case "str":
                        str(param)
                    case "float":
                        float(param)
                # Esto sirve para chequear el largo de los nombres como el de los teléfonos
                if largo != 0 and len(param) > largo:
                    raise Exception
            except TypeError:
                match tipo:
                    case "int":
                        param = input(
                            f'ERROR: En {nombreParam} debe ingresar un entero: ')
                    case "float":
                        param = input(
                            f'ERROR: En {nombreParam} debe ingresar un entero o un flotante separdo con ".": ')
                continue # No sé si está de más, creo que sí...

            except:
                param = input(
                    f'ERROR: en {nombreParam} se deben ingresar, como mucho {largo} caracteres: ')
                continue # No sé si está de más, creo que sí...

            else:
                match tipo:
                    case "int":
                        return int(param)
                    case "str":
                        return str(param)
                    case "float":
                        return float(param)

    def getNota(self):
        return self.nota
    
    def getNombreCompleto(self) -> str: #Parece que esto es un typehint
        return f'{self.apellido}, {self.nombre}'


def cargaEstudiante():
    matriculaSinTestear = input('Ingrese la matrícula del estudiante: ')
    apellidoSinTestear = input('Ingrese el apellido del estudiante: ')
    nombreSinTestear = input('Ingrese el nombre del estudiante: ')
    notaSinTestear = input('Ingrese la nota: ')
    estudiante = TDAEstudiante(matriculaSinTestear, apellidoSinTestear, nombreSinTestear, notaSinTestear)
    print(f'### {estudiante.getNombreCompleto()} cargado correctamente ###')
    return estudiante

def calcularPromedio(vector):
    promedio = 0
    for estudiante in vector:
        promedio += estudiante.getNota()
    return promedio / len(vector)

### PROGRAMA PRINCIPAL ###

cantidad = 10
estudiantes = [0] * cantidad
for i in range(cantidad):
    estudiantes[i] = cargaEstudiante()

promedio = calcularPromedio(estudiantes)
print(f'\nEl promedio del grupo fue {promedio}')

for estudiante in estudiantes:
    if estudiante.getNota() < promedio:
        print(f'{estudiante.getNombreCompleto()} está por debajo del promedio, con un {estudiante.getNota()}')