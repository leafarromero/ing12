from politica_ejecucion import PoliticaEjecucion
from vendedor_gas import VendedorGas

class PoliticaVentaGas(PoliticaEjecucion):

    def decidir(self,contexto, vendedor):
        pass

class UnaPoliticaVentaGas(PoliticaVentaGas):
    def __init__(self):
        pass

    def decidir(self,contexto, vendedor):
        max_gas = 2000
        almacenada = contexto.estructuras.litrosDeGasAlmacenado()
        if almacenada > max_gas:
            vendedor.vender(almacenada - max_gas)