import Libro
import Socio
from datetime import date

class Prestamo:
    def __init__(self, libro: Libro, idPrestamo, fechaInicio: date, fechaFin: date | None, socio: Socio):
        self.libro = libro
        self.idPrestamo = idPrestamo
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.socio = socio