from ..Repository.ILibroRepository import ILibroRepository

# Implementación de ILibroRepository para PostgreSQL
class LibroRepositoryPostgreSQL(ILibroRepository):
    def __init__(self):
        self.db = "Conexión a la base de datos PostgreSQL"

    def crear(self, entidad):
        pass

    def destruir(self, entidad):
        pass

    def editar(self, entidad):
        pass

    def listar(self, id):
        pass

    def obtener_todos(self):
        pass
