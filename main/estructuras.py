class Estructuras:
	def __init__(self):
		self.tanquesDeAgua = {}
		self.tanquesDeGas = {}
		self.plantasSeparadoras = {}
		self.tanquesDeAguaEnConstruccion = {}
		self.tanquesDeGasEnConstruccion = {}
		self.plantasSeparadorasEnConstruccion = {}

	def capacidadMaximaDeTanquesDeAgua(self):
		res = 0
		for tanque in self.tanquesDeAgua:
			res = res + tanque.litrosMaximo()
		return res

	def litrosDeAguaAlmacenado(self):
		res = 0
		for tanque in self.tanquesDeAgua:
			res = res + tanque.litros()
		return res

	def capacidadMaximaDeTanquesDeGas(self):
		res = 0
		for tanque in self.tanquesDeGas:
			res = res + tanque.litrosMaximo()
		return res

	def litrosDeGasAlmacenado(self):
		res = 0
		for tanque in self.tanquesDeGas:
			res = res + tanque.litros()
		return res

	def litrosPorDiaDePlantas(self):
		res = 0
		for planta in self.plantasProcesadoras:
			res = res + planta.litrosPorDia()
		return res

	def cantidadQuePuedeProcesarEnDia(self):
		res = 0
		for planta in self.plantasProcesadoras:
			res = res + planta.cantidadQuePuedeProcesarEnDia()
		return res

	def almacenarAgua(self):
		res = 0
		for planta in self.plantasProcesadoras:
			res = res + planta.cantidadQuePuedeProcesarEnDia()
		return res

    def almacenarGas(self, litrosDeGas):
        for tanq in self.tanquesDeGas:
            cant = min(tanq.cantidadQuePuedeAlmacenar(), litrosDeGas)
            if cant != 0:
                tanq.almacenar(composicionDeCrudo, cant)
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo == 0:
                break

    def almacenarAgua(self, litrosDeAgua):
        for tanq in self.tanquesDeAgua:
            cant = min(tanq.cantidadQuePuedeAlmacenar(), litrosDeAgua)
            if cant != 0:
                tanq.almacenar(composicionDeCrudo, cant)
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo == 0:
                break

    def retirarGas(self, litrosDeGas):
        for tanq in self.tanquesDeGas:
            cant = min(tanq.litrosAlmacenados(), litrosDeGas)
            if cant != 0:
                tanq.retirar(composicionDeCrudo, cant)
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo == 0:
                break

    def retirarAgua(self, litrosDeAgua):
        for tanq in self.tanquesDeAgua:
            cant = min(tanq.litrosAlmacenados(), litrosDeAgua)
            if cant != 0:
                tanq.retirar(composicionDeCrudo, cant)
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo == 0:
                break


    def procesarCrudo(self, composicionDeCrudo, litrosDeCrudo):
        materialesSeparados = (0, 0)

        for planta in (self.plantasSeparadoras):
            cant = min(planta.cantidadQuePuedeProcesarEnDia(), litrosDeCrudo)
            if cant != 0:
                materialesSeparadosEnPlanta = planta.procesar(composicionDeCrudo, cant)
                materialesSeparados[0] = materialesSeparados[0] + materialesSeparadosEnPlanta[0]
                materialesSeparados[1] = materialesSeparados[1] + materialesSeparadosEnPlanta[1]
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo == 0:
                break
        return materialesSeparados