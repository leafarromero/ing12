from .politica_ejecucion import PoliticaEjecucion
from .vendedor_gas import VendedorGas


class PoliticaVentaGas(PoliticaEjecucion):
    def __init__(self):
        self._vendedor_gas = VendedorGas()

    def decidir(self):
        pass
