from .constructor import Constructor
from .politica_ejecucion import PoliticaEjecucion

class PoliticaConstruccionTanquesAgua(PoliticaEjecucion):

    def decidir(self,contexto):
        pass


class PoliticaAguaPost80(PoliticaConstruccionTanquesAgua):

    def __init__(self):
        pass

    def decidir(self,contexto, constructor):
        if self.estan_al_limite(contexto.estructuras().dame_tanques_agua()):
            constructor.construir_tanque_agua(1,1,1)

    def estan_al_limite(tanques):

        for tanque in tanques:
            if tanque.litros() < tanque.cantidadQuePuedeAlmacenar() * 0.8:
                return False
        return True
