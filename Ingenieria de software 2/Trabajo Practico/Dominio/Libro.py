import Autor
import Genero

class Libro:
    def __init__(self,idLibro, titulo, autor: Autor, genero: Genero, isbn, stock=0):
        self.idLibro = idLibro
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.isbn = isbn
        self.stock = stock