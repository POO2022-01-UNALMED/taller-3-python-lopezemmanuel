class Marca:
    def __init__(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre