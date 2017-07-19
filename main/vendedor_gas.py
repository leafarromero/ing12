from .tanques_gas import TanquesGas

class VendedorGas:

    def __init__(self):
        pass

    def vender_gas(self,tanques,cantidad):
        for tanque in tanques:
            xyz = max(cantidad,tanque.litros())
            tanque.retirar(xyz)
            cantidad -= xyz
