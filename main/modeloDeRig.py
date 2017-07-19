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


def cargarModelosDeRig(configuracion):
	res = {}
	with open(self.miArchivo, "r") as file:
		while True:
			linea = file.readLine()
			if not linea:
				return res
			lineaParseada = linea.split(" ")
			res.add(ModeloDeRig(lineaParseada[0],int(lineaParseada[1]),int(lineaParseada[2]),int(lineaParseada[3]),int(lineaParseada[4])))