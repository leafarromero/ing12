from main.politica_ejecucion import PoliticaEjecucion


class PoliticaExcavacion(PoliticaEjecucion):

    def decidir(self):
        pass


class UnaPoliticaExcavacion(PoliticaExcavacion):

    def __init__(self):
        pass

    def decidir(self,contexto,excavador):
        pass