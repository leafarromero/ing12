from .politica_ejecucion import PoliticaEjecucion


from main.yacimiento import Formulas


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

            # Usar Agua almacenada
            agua_almacenada = contexto.estructuras.litrosDeAguaAlmacenada()
            min2 = min(agua_almacenada, volumen_a_reinyectar)
            bombeador.reinyectarAgua(min2)
            volumen_a_reinyectar -= min2
            
            # gas almacenada en los tanques
            gas_almacenado = contexto.estructuras.litrosDeGasAlmacenado()
            min1 = min(gas_almacenado, volumen_a_reinyectar)
            bombeador.reinyectarGas(min1)
            volumen_a_reinyectar -= min1

            # Comprar agua e inyectar
            comprador.compradorDeAgua(volumen_a_reinyectar)
            bombeador.reinyectarAgua(volumen_a_reinyectar)



        else:
            # en caso negativo se extrae de los pozos
            cant_extraer_por_pozo = Formulas().potencialVol()

            capacidad_almacenaje_agua = contexto.estructuras.capacidadMaximaDeTanquesDeAgua()
            litros_agua = contexto.estructuras.litrosDeAguaAlmacenada
            max_agua_puedo_extraer = capacidad_almacenaje_agua - litros_agua

            capacidad_almacenaje_gas = contexto.estructuras.capacidadMaximaDeTanquesDeGas()
            litros_gas = contexto.estructuras.litrosDeGasAlmacenado
            max_gas_puedo_extraer = capacidad_almacenaje_gas - litros_gas
            
            capacidad_procesamiento = contexto.estructuras.litrosPorDiaDePlantas()

            %agua = contexto.yacimiento.porcentajeAgua()
            %petroleo = contexto.yacimiento.porcentajePetroleo()
            %gas = contexto.yacimiento.porcentajeGas()

            cant_pozos_limitado_agua = max_agua_puedo_extraer / cant_extraer_por_pozo * %agua
            cant_pozos_limitad_gas = max_gas_puedo_extraer / cant_extraer_por_pozo * %gas
            cant_pozos_limitad_petroleo = capacidad_procesamiento / cant_extraer_por_pozo * %petroleo

            pozos_necesarios_agua = min(cant_pozos_limitad_gas, cant_pozos_limitad_petroleo,
                                        cant_pozos_limitad_petroleo)

            pozos = filter(lambda parcela: parcela.tienePozo(),contexto.yacimiento.parcelas())
            bombeador.extraer(pozos[1:pozos_necesarios_agua])

    def hay_que_reinyectar(self,yacimiento):
        __reinyectar = False
        for parcela in filter((lambda parcela: parcela.tienePozo()), yacimiento.parcelas()):
            if parcela.presion() < self._presion_critica:
                reinyectar = True
        return reinyectar


class CompradorAgua:

    def __init__(self):
        pass

    def comprar_agua(self,cantidad):
        pass