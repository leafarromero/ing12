from .constructor import Constructor
from .politica_ejecucion import PoliticaEjecucion


class PoliticaConstruccionTanquesAgua(PoliticaEjecucion):

    def __init__(self):
        self._constructor = Constructor()

    def decidir(self,admin_tanques_agua):
        if admin_tanques_agua.estan_al_limite():
            self._constructor.construir_tanque_agua(1,1,1)
