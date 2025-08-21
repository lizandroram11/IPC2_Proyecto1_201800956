# clases/nodo.py
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self._tamanio = 0

    def esta_vacia(self):
        return self.primero is None

    def tamanio(self):
        return self._tamanio

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

    def recorrer(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def buscar(self, predicado):
        for dato in self.recorrer():
            if predicado(dato):
                return dato
        return None

    def contiene(self, predicado):
        return self.buscar(predicado) is not None
