from .politica_ejecucion import PoliticaEjecucion
from .simulacion import Bombeador


class PoliticaBombeo(PoliticaEjecucion):
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
        _bombeador = Bombeador(
            tanques_agua,
            tanques_gas,
            plantas_separadoras,
            yacimiento,
            log,
        )
        _volumen_maximo_reinyeccion = volumen_maximo_reinyeccion
        _presion_critica = presion_critica
        _dilusion_critica = dilusion_critica

    def decidir(self,contexto):
        pass
        # Chequear que el pozo no este en dilusion critica
        # Chequear si algun pozo hay que reinyectar
        # en caso afirmativo no se puede extraer
        # en caso negativo se extrae de los pozos

        # Se reinyecta con agua comprada o  agua y gas almacenada en los tanques
        # La presion despues de reinyectar es
    # "Presion inicial" * (VolR - VolGlobalExtraido + VolTotal Reinyectado)/ VolR
    # donde VolGlobalReinyectado < VolGlobalExtraido

    # Luego cambian los valores de los pozos:
    #