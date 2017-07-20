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

    def decidir(self,contexto, bombeador):
        # Chequear que el pozo no este en dilusion critica
        
        unYacimiento = contexto.yacimiento()
        if self._dilusion_critica > unYacimiento.porcentajePetroleo:
            return

        # Chequear si algun pozo hay que reinyectar
        if self.hay_que_reinyectar(contexto,unYacimiento):
            # en caso afirmativo no se puede extraer
            volumen_a_reinyectar = min(self._volumen_maximo_reinyeccion,contexto.yacimiento().volumenInicial()-contexto.yacimiento().volumenActual())

            # Usar Agua almacenada
            agua_almacenada = contexto.estructuras().litrosDeAguaAlmacenada()
            min2 = min(agua_almacenada, volumen_a_reinyectar)
            bombeador.reinyectarAgua(min2)
            volumen_a_reinyectar -= min2
            
            # porcentaje_gas almacenada en los tanques
            gas_almacenado = contexto.estructuras().litrosDeGasAlmacenado()
            min1 = min(gas_almacenado, volumen_a_reinyectar)
            bombeador.reinyectarGas(min1)
            volumen_a_reinyectar -= min1

            # Comprar porcentaje_agua e inyectar
            bombeador.reinyectarAgua(volumen_a_reinyectar)



        else:
            parcelasConPozo = filter((lambda x: x.tienePozo()), unYacimiento.parcelas())

            if parcelasConPozo:
                parcela = parcelasConPozo[0]
                potencial = parcela.formulas().potencial(parcela.presion(), unYacimiento.volumenActual())

                # en caso negativo se extrae de los pozos

                capacidad_almacenaje_agua = contexto.estructuras().capacidadMaximaDeTanquesDeAgua()
                litros_agua = contexto.estructuras().litrosDeAguaAlmacenada()
                max_agua_puedo_extraer = capacidad_almacenaje_agua - litros_agua

                capacidad_almacenaje_gas = contexto.estructuras().capacidadMaximaDeTanquesDeGas()
                litros_gas = contexto.estructuras().litrosDeGasAlmacenado()
                max_gas_puedo_extraer = capacidad_almacenaje_gas - litros_gas
                
                capacidad_procesamiento = contexto.estructuras().litrosPorDiaDePlantas()

                porcentaje_agua = contexto.yacimiento().porcentajeAgua()
                porcentaje_petroleo = contexto.yacimiento().porcentajePetroleo()
                porcentaje_gas = contexto.yacimiento().porcentajeGas()

                cant_pozos_limitado_agua = max_agua_puedo_extraer / potencial * porcentaje_agua
                cant_pozos_limitado_gas = max_gas_puedo_extraer / potencial * porcentaje_gas
                cant_pozos_limitado_petroleo = capacidad_procesamiento / potencial * porcentaje_petroleo

                pozos_necesarios_agua = min(cant_pozos_limitado_gas, cant_pozos_limitado_petroleo,
                                            cant_pozos_limitado_agua)

                pozos = filter(lambda parcela: parcela.tienePozo(),contexto.yacimiento().parcelas())
                bombeador.extraer(pozos[1:pozos_necesarios_agua])

    def hay_que_reinyectar(self,contexto,yacimiento):
        _reinyectar = False
        volumenMaximo = min(self._volumen_maximo_reinyeccion,contexto.yacimiento().volumenInicial()-contexto.yacimiento().volumenActual())
        if volumenMaximo==0:
            return False
        if contexto.numPozos()==0:
            return False
        for parcela in filter((lambda parcela: parcela.tienePozo()), yacimiento.parcelas()):
            if parcela.presion() < self._presion_critica:
                _reinyectar = True
        return _reinyectar


