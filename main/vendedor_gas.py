from .tanques_gas import TanqueGas

class VendedorGas:

    def __init__(self,log,estructuras,confPath):
        self.estructuras = estructuras
        self.log = log
        archivo = confPath + "vendedorDeGas.txt"
        with open(archivo, "r") as file:
        	linea = file.readLine()
        	self.dolaresPorLitroDeGas = float(linea)

    def vender_gas(self,cantidad):
        aVender = max(self.estructuras.litrosDeGasAlmacenado(),cantidad)
        self.estructuras.retirarGas(aVender)
        self.log.escribirLinea("litros de gas vendidos: " + str(aVender) + "\n")
        self.log.venta(aVender*self.dolaresPorLitroDeGas)
