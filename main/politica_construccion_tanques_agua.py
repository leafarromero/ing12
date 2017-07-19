from .constructor import Constructor
from .politica_ejecucion import PoliticaEjecucion


class PoliticaConstruccionTanquesAgua(PoliticaEjecucion):

    def __init__(self):
        self._constructor = Constructor()

    def decidir(self,contexto):
        if self.estan_al_limite(contexto.estructuras().dame_tanques_agua()):
            self._constructor.construir_tanque_agua(1,1,1)
