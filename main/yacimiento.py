class Yacimiento:
    def __init__(self):

        #Habria que pasarle los parametros con los que se construye
        self.parcelas = [] 
        self.volumen = 0
        self.porcentajePetroleo = 100
        self.porcentajeGas = 0
        self.porcentajeAgua = 0
        

    def parcelas(self):
        return self.parcelas

    def volumenInicial(self):
    	return self.volumenInicial

	def volumenActual(self):
    	return self.volumenActual

    def pasarDia():
        for p in self.parcelas:
            p.pasarDia()

    def extraer(self, cantProducto):
        self.volumenActual -= cantProducto
        

    def reinyectarAgua(self, cantAgua):
        #sacar las cuentas para cambiar el porcentaje y volumen
        volumenNuevo = self.volumenActual + cantAgua

        porcNuevoAgua = float(self.volumenActual * float(self.porcentajeAgua) / 100+ cantAgua) / volumenNuevo
        porcNuevoGas = float(self.volumenActual * float(self.porcentajeGas) / 100) / volumenNuevo
        porcNuevoProducto = float(self.volumenActual * float(self.porcentajePetroleo) / 100) / volumenNuevo

        self.volumenActual = volumenNuevo
        self.porcentajeAgua = porcNuevoAgua
        self.porcentajePetroleo = porcNuevoProducto
        self.porcentajeGas = porcNuevoGas

        for p in self.parcelas:
        	p.reinyeccion()

    def reinyectarGas(self, cantGas):
        #sacar las cuentas para cambiar el porcentaje y volumen
        volumenNuevo = self.volumenActual + cantGas

        porcNuevoAgua = float(self.volumenActual * float(self.porcentajeAgua)) / volumenNuevo
        porcNuevoGas = 100 * float(self.volumenActual * float(self.porcentajeGas) / 100 + cantGas) / volumenNuevo
        porcNuevoPetroleo = float(self.volumenActual * float(self.porcentajePetroleo)) / volumenNuevo

        self.volumenActual = volumenNuevo
        self.porcentajeAgua = porcNuevoAgua
        self.porcentajePetroleo = porcNuevoPetroleo
        self.porcentajeGas = porcNuevoGas

		for p in self.parcelas:
        	p.reinyeccion()

    def numPozos(self):
        for p in self.parcelas:
            p.tienePozo()



class Parcela:

    def __init__(self, profundidad, presionInicial, resistencia, yacimiento, formulasParcela):
        self.presionInicial = presionInicial
        self.presion = presionInicial
        self.profundidad = profundidad
        self.resistencia = resistencia
        self.yacimiento = yacimiento
        self.pozo = Excavacion(self)
        self.formulas = formulasParcela

    def extraer(numPozos):
        potencial = self.formulas.potencial(self.presion, numPozos)
        self.yacimiento.extraer(potencial)
        return potencial

    def reinyeccion():
    	presion = presionInicial * float(self.yacimiento.volumenActual())/ self.yacimiento.volumenInicial()

    def tienePozo():
        return type(self.pozo) is Pozo

    def pasarDia():
    	volumenR = self.yacimiento.volumenInicial()
    	volumenRi = self.yacimiento.volumenActual()
    	numPozos = self.yacimiento.numPozos()
    	presion = self.formulas.presionAlSiguienteDia(self.presion, volumenR, volumenRi, numPozos)

class Pozo:
    def __init__(self, parcela):
        self.parcela = parcela

    def extraer(numPozos):
        #El extractor hace la verificacion si se puede extraer de acuerdo a las estructuras disponibles
        productoExtraido = self.parcela.extraer(numPozos)
        return productoExtraido
