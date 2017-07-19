class Constructor:
	def __init__(self,log,estructuras,confPath):
		self.log = log
		self.estructuras = estructuras
		archivo = confPath + "estructuras.txt"
		with open(archivo, "r") as file:
			linea = file.readLine()
			lineaParseada = linea.split(" ")
			self.costoTanqueAguaPorLitro = lineaParseada[1]
			self.costoTanqueGasPorLitro = lineaParseada[3]
			self.costoPlantaPorLitro = lineaParseada[5]

	def construirTanqueAgua(self,litros):
		log.escribirLinea("comienzo a construir tanque de agua, litros: " + str(litros) + "\n")
		log.gasto(self.costoTanqueAguaPorLitro*litros)
		self.estructuras.construirTanqueAgua(litros,log)

	def construirTanqueGas(self,litros):
		log.escribirLinea("comienzo a construir tanque de gas, litros: " + str(litros) + "\n")
		log.gasto(self.costoTanqueGasPorLitro*litros)
		self.estructuras.construirTanqueGas(litros,log)
	def construirPlantaSeparadora(self):
		log.escribirLinea("comienzo a construir planta separadora, litros: " + str(litros) + "\n")
		log.gasto(self.costoPlantaPorLitro*litros)
		self.estructuras.construirPlantaSeparadora(litros,log)