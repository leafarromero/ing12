from politica_ejecucion import PoliticaEjecucion
from simulacion import Bombeador, TanqueAgua

class PoliticaBombeo(PoliticaEjecucion):

    def decidir(self,contexto, bombeador, comprador):
        pass

class UnaPoliticaBombeo(PoliticaBombeo):
    def __init__(self,
                 volumen_maximo_reinyeccion,
                 presion_critica,
                 log,
                 dilusion_critica,
                 ):

        self._volumen_maximo_reinyeccion = volumen_maximo_reinyeccion
        self._presion_critica = presion_critica
        self._dilusion_critica = dilusion_critica
        self._log = log

    def decidir(self,contexto, bombeador, comprador):
        # Chequear que el pozo no este en dilusion critica
        
        unYacimiento = contexto.yacimiento
        if self._dilusion_critica > unYacimiento.porcentajePetroleo:
            return

        # Chequear si algun pozo hay que reinyectar
        if self.hay_que_reinyectar(unYacimiento):
            # en caso afirmativo no se puede extraer
            volumen_a_reinyectar = self._volumen_maximo_reinyeccion

            # Se reinyecta con agua comprada o  agua y gas almacenada en los tanques
            gas_almacenado = contexto.estructuras.litrosDeGasAlmacenado()
            min1 = min(gas_almacenado, volumen_a_reinyectar)
            bombeador.reinyectarGas(min1)
            volumen_a_reinyectar -= min1

            # Usar Agua almacenada
            agua_almacenada = contexto.estructuras.litrosDeAguaAlmacenada()
            min2 = min(agua_almacenada, volumen_a_reinyectar)
            bombeador.reinyectarAgua(min2)
            volumen_a_reinyectar -= min2
            
            # Comprar agua
            comprador.compradorDeAgua(volumen_a_reinyectar)
            bombeador.reinyectarAgua(volumen_a_reinyectar)



        else:
            # en caso negativo se extrae de los pozos
            pozos = contexto.extructuras.
            bombeador.extraer()

    def hay_que_reinyectar(self,yacimiento):
        __reinyectar = False
        for parcela in filter((lambda x: x.tienePozo()), yacimiento.parcelas()):
            if parcela.presion() < self._presion_critica:
                reinyectar = True
        return reinyectar


class CompradorAgua:

    def __init__(self):
        pass

    def comprar_agua(self,cantidad):
        pass