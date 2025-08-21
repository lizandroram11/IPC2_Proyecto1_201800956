from clases.nodo import ListaEnlazada

class Estacion:
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre
        self.sensores_suelo = ListaEnlazada()
        self.sensores_cultivo = ListaEnlazada()

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def agregar_sensor_suelo(self, sensor):
        # Evitar duplicados por id
        if not self.sensores_suelo.contiene(lambda s: s.get_id() == sensor.get_id()):
            self.sensores_suelo.insertar(sensor)

    def agregar_sensor_cultivo(self, sensor):
        if not self.sensores_cultivo.contiene(lambda s: s.get_id() == sensor.get_id()):
            self.sensores_cultivo.insertar(sensor)
