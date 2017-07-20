class EstructuraConstruccion:
	def __init__(self,tiempo,litros,metodoConstruir,borrarConstructor):
		self._diasRestantes = tiempo
		self.metodoConstruir = metodoConstruir
		self.borrarConstructor = borrarConstructor
		self._litros = litros

	def diasRestantes(self):
		return self._diasRestantes

	def litros(self):
		return self._litros

	def pasarDia(self):
		self._diasRestantes = self._diasRestantes - 1
		if self._diasRestantes == 0:
			metodo = self.metodoConstruir
			borrarConstructor = self.borrarConstructor
			metodo()
			borrarConstructor(self)