from .politica_ejecucion import PoliticaEjecucion
from .simulacion import Bombeador, TanqueAgua

class PoliticaBombeo(PoliticaEjecucion):

    def decidir(self,contexto):
        pass

class UnaPoliticaBombeo(PoliticaBombeo):
    def __init__(self,
                 volumen_maximo_reinyeccion,
                 presion_critica,
                 tanques_agua,
                 tanques_gas,
                 plantas_separadoras,
                 yacimiento,
                 log,
                 dilusion_critica,
                 ):

        self._bombeador = Bombeador(
            tanques_agua,
            tanques_gas,
            plantas_separadoras,
            yacimiento,
            log,
        )
        self._volumen_maximo_reinyeccion = volumen_maximo_reinyeccion
        self._presion_critica = presion_critica
        self._dilusion_critica = dilusion_critica

    def decidir(self,contexto):
        # Chequear que el pozo no este en dilusion critica

        unYacimiento = contexto.yacimiento
        if self._dilusion_critica > unYacimiento.porcentajePetroleo:
            return

        # Chequear si algun pozo hay que reinyectar
        if self.hay_que_reinyectar(unYacimiento):
            # en caso afirmativo no se puede extraer

            # Se reinyecta con agua comprada o  agua y gas almacenada en los tanques
            if self.tengo_agua_gas_almacenada(contexto):
                # Usar usa agua
                pass
            else:
                # Comprar agua
                pass


        else:
            # en caso negativo se extrae de los pozos
            pass

    def hay_que_reinyectar(self,yacimiento):
        __reinyectar = False
        for parcela in filter((lambda x: x.tienePozo()), yacimiento.parcelas()):
            if parcela.presion() < self._presion_critica:
                reinyectar = True
        return reinyectar

    def tengo_agua_gas_almacenada(self,contexto):
        for tanque_agua in contexto.estructuras.dame_tanques_agua():
            if tanque_agua.litros() > 0
                return True

        for tanque_gas in contexto.dame_tanques_gas():
            if tanque_gas.litros() > 0:
                return True

        return False
