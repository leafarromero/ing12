from .constructor import Constructor
from .politica_ejecucion import PoliticaEjecucion

class PoliticaConstruccionTanquesGas(PoliticaEjecucion):

    def decidir(self,contexto, constructor):
        pass

class PoliticaGasPost80(PoliticaConstruccionTanquesGas):

    def __init__(self):
        pass

    def decidir(self,contexto, constructor):
        if self.estan_al_limite(contexto.estructuras().dame_tanques_agua()):
            constructor.contruir_tanque_gas(1,1,1)

    def estan_al_limite(tanques):

        for tanque in tanques:
            if tanque.litros() < tanque.cantidadQuePuedeAlmacenar() * 0.8:
                return False
        return True
