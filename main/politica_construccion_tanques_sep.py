from .constructor import Constructor
from .politica_ejecucion import PoliticaEjecucion

class PoliticaConstruccionTanquesSep(PoliticaEjecucion):

    def decidir(self,contexto):
        pass

class PoliticaSepPost80(PoliticaConstruccionTanquesSep):

    def __init__(self):
        _constructor = Constructor()

    def decidir(self,contexto):
        pass
