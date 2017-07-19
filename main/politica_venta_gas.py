from .politica_ejecucion import PoliticaEjecucion
from .vendedor_gas import VendedorGas

class PoliticaVentaGas(PoliticaEjecucion):

    def decidir(self,contexto, vendedor):
        pass

class UnaPoliticaVentaGas(PoliticaVentaGas):
    def __init__(self):
        pass

    def decidir(self,contexto, vendedor):
        max_gas = 2000
        tanques_gas = contexto.estructuras.dame_tanques_gas()
        almacenada = gas_almacenado(tanques_gas)
        if almacenada > max_gas:
            vendedor_gas.vender(almacenada - max_gas)

        def gas_almacenado(tanques_gas):
            litros = 0
            for tanque in tanques_gas:
                litros += tanque.litros()
