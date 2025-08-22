
from clases.sensor import Sensor

# Definición de la clase SensorCultivo
class SensorCultivo(Sensor):
# Método __init__
    def __init__(self, id, nombre):
        super().__init__(id, nombre)