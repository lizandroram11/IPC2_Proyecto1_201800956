from clases.nodo import ListaEnlazada

# Definición de la clase Sensor, representa una entidad del sistema
class Sensor:
# Método __init__: se encarga de una funcionalidad específica de la clase o del flujo principal
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre
        self.frecuencias = ListaEnlazada()

# Método get_id: se encargara de obtener el id desde el archivo xml
    def get_id(self):
        return self.__id

# Método get_nombre:
    def get_nombre(self):
        return self.__nombre

# Método agregar_frecuencia: agregara una frecuencia a la lista enlazada
    def agregar_frecuencia(self, frecuencia):
        self.frecuencias.insertar(frecuencia)