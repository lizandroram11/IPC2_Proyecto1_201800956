from clases.nodo import ListaEnlazada

class CampoAgricola:
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre
        self.estaciones = ListaEnlazada()

    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre

    def agregar_estacion(self, estacion):
        self.estaciones.insertar(estacion)

    def mostrar_estaciones(self):
        for estacion in self.estaciones.recorrer():
            print(f"- {estacion.get_nombre()} (ID: {estacion.get_id()})")
