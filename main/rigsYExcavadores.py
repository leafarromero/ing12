class Rig:
	def __init__(self,modelo,diasRestantes):
		self.modelo = modelo
		self._diasRestantes = diasRestantes

	def costoAlquiler(self):
		return self.modelo.costoAlquiler

	def litrosCombustiblePorDia(self):
		return self.modelo.litrosCombustiblePorDia

	def excavar(self,parcela):
		parcela.pozo.excavar(parcela,self.modelo.metrosPorDia)

	def diasRestantes():
		return self._fechaFinDeAlquiler

	def pasarDia():
		self._diasRestantes = self._diasRestantes - 1

class Excavador:
	def __init__(self,log,dolaresPorLitroDeCombustible):
		self.dolaresPorLitroDeCombustible = dolaresPorLitroDeCombustible
		self.log = log

	def excavar(self,parcela,rig):
		rig.excavar(parcela)
		self.log.gasto(rig.litrosCombustiblePorDia*self.dolaresPorLitroDeCombustible)


class RigManager:
	def __init__(self,log,administradorDeRig):
		self.log = log
		self.administradorDeRig = administradorDeRig
	def alquilar(self,modelo,cantidadDeDias,administradorDeRig):
		self.log.gasto((modelo.costoAlquilerPorDia)*cantidadDeDias)
		self.administradorDeRig.agregarRig(Rig(modelo,cantidadDeDias))
	def pasarDia(self):
		rigsABorrar = {}
		for rig in self.administradorDeRig.rigs:
			rig.pasarDia()
			if diasRestantes==0:
				rigsABorrar.add(rig)
		for rig in rigsABorrar:
			self.administradorDeRig.quitarRig(rig)


class AdministradorDeRigs:
	def __init__(self):
		self.rigs = {}
	def agregarRig(self,rig):
		self.rigs.add(rig)

	def quitarRig(self,rig):
		self.rigs.discart(rig)