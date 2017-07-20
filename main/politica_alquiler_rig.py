from main.politica_ejecucion import PoliticaEjecucion
from main.rigsYExcavadores import RigManager


class PoliticaAlquilerRig(PoliticaEjecucion):

    def decidir(selfs, contexto):
        pass


class UnaPoliticaAlquilerRig(PoliticaAlquilerRig):

    def __init__(self):
        pass

    def decidir(self,contexto):
        if len(contexto.administradorDeRigs.rigs()) == 0 :
            RigManager.alquilar("modelo_nuevo",12)

