from .constructor import Constructor
from .politica_ejecucion import PoliticaEjecucion

class PoliticaConstruccionTanquesSep(PoliticaEjecucion):

    def decidir(self,contexto, constructor):
        pass

class PoliticaSepPost80(PoliticaConstruccionTanquesSep):

    def __init__(self):
        pass

    def decidir(self,contexto, constructor):
        pass
