from clases.nodo import ListaEnlazada

class Sensor:
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre
        self.frecuencias = ListaEnlazada()

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def agregar_frecuencia(self, frecuencia):
        self.frecuencias.insertar(frecuencia)
