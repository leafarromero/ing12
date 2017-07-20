class Bombeador:
    def __init__(self, log, estructuras, yacimiento,compradorDeAgua):
        self.estructuras = estructuras
        self.yacimiento = yacimiento
        self.log = log
        self.compradorDeAgua = compradorDeAgua

    def extraer(self, pozos):
        for poz in pozos:
            composicionDeCrudo = (
                self.yacimiento.porcentajePetroleo(), self.yacimiento.porcentajeGas(), self.yacimiento.porcentajeAgua())
            materialesSeparados = self.estructuras.procesarCrudo(composicionDeCrudo, poz.extraer(len(pozos)))
            litrosDeAgua = materialesSeparados[0]
            litrosDeGas = materialesSeparados[1]
            self.log.escribirLinea("litros de gas destilados: " + str(litrosDeGas) + "\n")
            self.log.escribirLinea("litros de agua destilados: " + str(litrosDeAgua) + "\n")
            self.estructuras.almacenarAgua(litrosDeAgua)
            self.estructuras.almacenarGas(litrosDeGas)

    def reinyectarGas(self,litrosGas):
        gas = self.estructuras.retirarGas(litrosGas)
        self.yacimiento.reinyectarGas(gas)

    def reinyectarAgua(self,litrosAgua):
        if self.estructuras.litrosDeAguaAlmacenado() < litrosDeAgua:
            self.compradorDeAgua.comprar(litrosDeAgua - self.estructuras.litrosDeAguaAlmacenado())
        self.reinyectarAgua(litrosDeAgua)