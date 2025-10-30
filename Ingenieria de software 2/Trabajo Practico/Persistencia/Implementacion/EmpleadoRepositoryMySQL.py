from ..Repository.IEmpleadoRepository import IEmpleadoRepository

# Implementación de IEmpleadoRepository para MySQL
class EmpleadoRepositoryMySQL(IEmpleadoRepository):
    def __init__(self):
        self.db = "Conexión a la base de datos MySQL"

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
