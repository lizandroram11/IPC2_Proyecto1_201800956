# ================================================
# Archivo: frecuencia.py
# Comentarios agregados en estilo docente para explicar
# cada clase, método y variables principales.
# ================================================

# Definición de la clase Frecuencia, representa una entidad del sistema
class Frecuencia:
# Método __init__: se encarga de una funcionalidad específica de la clase o del flujo principal
    def __init__(self, id_estacion, valor):
        self.id_estacion = id_estacion
        self.valor = int(valor)

# Método __str__: se encarga de una funcionalidad específica de la clase o del flujo principal
    def __str__(self):
        return f"{self.id_estacion}:{self.valor}"