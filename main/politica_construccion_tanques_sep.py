from constructor import Constructor
from politica_ejecucion import PoliticaEjecucion

class PoliticaConstruccionTanquesSep(PoliticaEjecucion):

    def decidir(self,contexto, constructor):
        pass

class PoliticaSepPost80(PoliticaConstruccionTanquesSep):

    def __init__(self):
        pass

    def decidir(self,contexto, constructor):
        estructuras = contexto.estructuras()

        cant_puede_procesar = estructuras.cantidadQuePuedeProcesarEnDiaAFuturo() \
                              + estructuras.cantidadQuePuedeProcesarEnDia()

        cant_almacenar_gas = estructuras.capacidadMaximaDeTanquesDeAgua() \
                            + estructuras.capacidadMaximaDeTanquesDeAguaAFuturo()
        cant_almacenar_agua = estructuras.capacidadMaximaDeTanquesDeGas() \
                            +  estructuras.capacidadMaximaDeTanquesDeGasAFuturo()

        if cant_puede_procesar >= cant_almacenar_gas or cant_puede_procesar >= cant_almacenar_agua:
            constructor.construirPlantaSeparadora(30)
