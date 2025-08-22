# clases/nodo.py
class Nodo:
# Método __init__: se encarga de una funcionalidad específica de la clase o del flujo principal
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# Definición de la clase ListaEnlazada,
class ListaEnlazada:
# Método __init__: se encarga de una funcionalidad específica de la clase o del flujo principal
    def __init__(self):
        self.primero = None
        self._tamanio = 0

# Método esta_vacia: se encarga de una funcionalidad específica de la clase o del flujo principal
    def esta_vacia(self):
        return self.primero is None

# Método tamanio: se encarga de una funcionalidad específica de la clase o del flujo principal
    def tamanio(self):
        return self._tamanio

# Método insertar: se encarga de una funcionalidad específica de la clase o del flujo principal
    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

# Método recorrer: se encarga de una funcionalidad específica de la clase o del flujo principal
    def recorrer(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

# Método buscar: se encarga de una funcionalidad específica de la clase o del flujo principal
    def buscar(self, predicado):
        for dato in self.recorrer():
            if predicado(dato):
                return dato
        return None

# Método contiene: se encarga de una funcionalidad específica de la clase o del flujo principal
    def contiene(self, predicado):
        return self.buscar(predicado) is not None