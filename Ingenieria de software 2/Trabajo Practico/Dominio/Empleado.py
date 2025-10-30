import Persona

class Empleado(Persona):
    def __init__(self, nombre, email, idEmpleado):
        super().__init__(nombre, email)
        self.idEmpleado = idEmpleado