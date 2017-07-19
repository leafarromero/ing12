from .politica_ejecucion import PoliticaEjecucion
from .simulacion import Bombeador

class PoliticaBombeo(PoliticaEjecucion):

    def __init__(self):
        _bombeador = Bombeador()

    def decidir(self):
        pass
