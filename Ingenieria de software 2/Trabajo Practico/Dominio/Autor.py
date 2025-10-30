import Persona

class Autor(Persona):
    def __init__(self, nombre, email, idAutor, especialidad, nacionalidad):
        super().__init__(nombre, email)
        self.idAutor = idAutor
        self.especialidad = especialidad
        self.nacionalidad = nacionalidad