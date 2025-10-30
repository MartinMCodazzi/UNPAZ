import Persona

class Socio(Persona):    
    def __init__(self, nombre, email, idSocio):
        super().__init__(nombre, email)
        self.idSocio = idSocio