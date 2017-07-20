class ModeloDeRig:
	def __init__(self,nombre,metrosPorDia,minimoDias,costoAlquiler,litrosCombustiblePorDia):
		self._nombre = nombre
		self._metrosPorDia = metrosPorDia
		self._minimoDias = minimoDias
		self._costoAlquiler = costoAlquiler
		self._litrosCombustiblePorDia = litrosCombustiblePorDia
	def nombre(self):
		return self._nombre

	def metrosPorDias(self):
		return self._metrosPorDia
	def minimoDias(self):
		return self._minimoDias
	def costoAlquiler(self):
		return self._costoAlquiler
	def litrosCombustiblePorDia(self):
		return self._litrosCombustiblePorDia


def cargarModelosDeRig(confPath):
	miArchivo = confPath + "modelos_de_rig.txt"
	res = set()
	file =open(miArchivo, "r")
	while True:
		linea = file.readline()
		if not linea:
			file.close()
			return res
		lineaParseada = linea.split(" ")
		res.add(ModeloDeRig(lineaParseada[0],float(lineaParseada[1]),float(lineaParseada[2]),float(lineaParseada[3]),float(lineaParseada[4])))