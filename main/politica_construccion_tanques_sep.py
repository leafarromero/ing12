from .constructor import Constructor
from .politica_ejecucion import PoliticaEjecucion


class PoliticaConstruccionTanquesSep(PoliticaEjecucion):

    def __init__(self):
        _constructor = Constructor()

    def decidir(self):
        pass
