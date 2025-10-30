from ..Repository.ISocioRepository import ISocioRepository

# Implementación de ISocioRepository para SQLite
class SocioRepositorySQLite(ISocioRepository):
    def __init__(self):
        self.db = "Conexión a la base de datos SQLite"

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
