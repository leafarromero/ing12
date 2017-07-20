from main.politica_ejecucion import PoliticaEjecucion
from main.rigsYExcavadores import RigManager


class PoliticaAlquilerRig(PoliticaEjecucion):

    def decidir(selfs, contexto):
        pass


class UnaPoliticaAlquilerRig(PoliticaAlquilerRig):

    def __init__(self):
        pass

    def decidir(self,contexto,rigManager):
        if len(contexto.administradorDeRigs().rigs()) == 0 :
			modelo = contexto.administradorDeRigs().modelosDeRigs().pop()
			rigManager.alquilar(modelo,12)

