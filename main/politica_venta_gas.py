from .politica_ejecucion import PoliticaEjecucion
from .vendedor_gas import VendedorGas


class PoliticaVentaGas(PoliticaEjecucion):
    def __init__(self):
        self._vendedor_gas = VendedorGas()

    def decidir(self,admin_tanques_gas,vendedor_de_gas):
        max_gas = 2000
        almacenada = admin_tanques_gas.cantidad_almacenada()
        if almacenada > max_gas:
            vendedor_de_gas.vender(almacenada - max_gas)
