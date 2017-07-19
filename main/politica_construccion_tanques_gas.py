from .constructor import Constructor
from .politica_ejecucion import PoliticaEjecucion


class PoliticaConstruccionTanquesGas(PoliticaEjecucion):

    def __init__(self):
        self._constructor = Constructor()

    def decidir(self,admin_tanques_gas):
        if admin_tanques.gas.estan_al_limite():
            self._constructor.contruir_tanque_gas(1,1,1)
