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
		self.log.escribirLinea("Efectuada excavacion")
		self.log.gasto(rig.litrosCombustiblePorDia*self.dolaresPorLitroDeCombustible)


class RigManager:
	def __init__(self,log,administradorDeRig):
		self.log = log
		self.administradorDeRig = administradorDeRig
	def alquilar(self,modelo,cantidadDeDias,administradorDeRig):
		self.log.escribirLinea("Nuevo rig alquilado")
		self.log.gasto((modelo.costoAlquilerPorDia)*cantidadDeDias)
		self.administradorDeRig.agregarRig(Rig(modelo,cantidadDeDias))
	def pasarDia(self):
		rigsCauducados = self.administradorDeRig.pasarDia()
		if rigsCauducados!=0:
			self.log.escribirLinea("rigs caudicaron alquiler: " + Str(rigsCauducados))


class AdministradorDeRigs:
	def __init__(self):
		self.rigs = {}
	def agregarRig(self,rig):
		self.rigs.add(rig)

	def pasarDia(self):
		rigsABorrar = {}
		for rig in self.rigs:
			rig.pasarDia()
			if diasRestantes==0:
				rigsABorrar.add(rig)
		for rig in rigsABorrar:
			self.rigs.discart(rig)
		return len(rigsABorrar)