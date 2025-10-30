from ..Repository.IPrestamoRepository import IPrestamoRepository

# Implementación de IPrestamoRepository para MSSQL
class PrestamoRepositoryMSSQL(IPrestamoRepository):
    def __init__(self):
        self.db = "Conexión a la base de datos MSSQL"

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