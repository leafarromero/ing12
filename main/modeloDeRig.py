class ModeloDeRig:
	def __init__(self,metrosPorDia,minimoDias,costoAlquiler,litrosCombustiblePorDia):
		self.metrosPorDia = metrosPorDia
		self.minimoDias = minimoDias
		self.costoAlquiler = costoAlquiler
		self.litrosCombustiblePorDia = litrosCombustiblePorDia


def cargarModelosDeRig(configuracion):
	res = {}
	with open(self.miArchivo, "r") as file:
		while True:
			linea = file.readLine()
			if not linea:
				return res
			lineaParseada = linea.split(" ")
			res.add(ModeloDeRig(int(lineaParseada[0]),int(lineaParseada[1]),int(lineaParseada[2]),int(lineaParseada[3])))