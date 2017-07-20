class Formulas:    
    def __init__(self, alpha1 = 0.35, alpha2 = 0.0075): 
        if (0.1 <= alpha1 <= 0.6):
            self.alpha1 = alpha1 
        else:
            raise ValueError
        if (0.005 <= alpha2 <= 0.01):
            self.alpha2 = alpha2
        else:
            raise ValueError
        
    def potencialVol(self,presion,volumenRi,numPozos):
        sumando1 = self.alpha1 * (presion/numPozos)
        sumando2 = self.alpha2 * ((presion/numPozos)^2)
        return sumando1 + sumando2
        
    def presionAlSiguienteDia(self, presionAnterior, volumenR, volumenRi,numPozos):
        betaI = self.betaI(volumenR, volumenRi, numPozos)
        return presionAnterior * (math.e ^ -(betaI))
    
    def betaI(self, volumenR, volumenRi, numPozos):
        return (0.1 * (volumenRi / volumenR)) / ((numPozos)^(2/3))

    def reinyeccion(self, presionInicial, volumenActual, volumenInicial):
        return presionInicial * float(volumenActual) / volumenInicial

class Yacimiento:
    def __init__(self, confPath):
        #Leer yacimiento y definir volumen, porcentajes y parcelas
        with open(confPath+'yacimiento.txt') as file:
            params = file.readline().split()
            self.volumen = float(params[0])
            self.porcentajePetroleo = float(params[1])
            self.porcentajeGas = float(params[2])
            self.porcentajeAgua = float(params[3])

            params = file.readline().split()
            alfa1 = float(params[0])
            alfa2 = float(params[1])
            formulas = Formulas(alfa1, alfa2)
            
            self.parcelas = []
            for line in file:
                profundidad = float(line[0])
                presionInicial = float(line[1])
                resistencia = float(line[2])
                self.parcelas.append(Parcela(profundidad, presionInicial, resistencia, self, formulas))

    def parcelas(self):
        return self.parcelas

    def porcentajePetroleo(self):
        return self.porcentajePetroleo

    def porcentajeAgua(self):
        return self.porcentajeGas

    def porcentajeGas(self):
        return self.porcentajeAgua

    def volumenInicial(self):
        return self.volumenInicial

    def volumenActual(self):
        return self.volumenActual

    def pasarDia(self):
        for p in self.parcelas:
            p.pasarDia()

    def extraer(self, cantProducto):
        self.volumenActual -= cantProducto

    def reinyectarAgua(self, cantAgua):
        # sacar las cuentas para cambiar el porcentaje y volumen
        volumenNuevo = self.volumenActual + cantAgua

        porcNuevoAgua = float(self.volumenActual * self.porcentajeAgua + cantAgua * 100) / volumenNuevo
        porcNuevoGas = float(self.volumenActual * self.porcentajeGas) / volumenNuevo
        porcNuevoProducto = float(self.volumenActual * self.porcentajePetroleo) / volumenNuevo

        self.volumenActual = volumenNuevo
        self.porcentajeAgua = porcNuevoAgua
        self.porcentajePetroleo = porcNuevoProducto
        self.porcentajeGas = porcNuevoGas

        for p in self.parcelas:
            p.reinyeccion()

    def reinyectarGas(self, cantGas):
        # sacar las cuentas para cambiar el porcentaje y volumen
        volumenNuevo = self.volumenActual + cantGas

        porcNuevoAgua = float(self.volumenActual * self.porcentajeAgua) / volumenNuevo
        porcNuevoGas = float(self.volumenActual * self.porcentajeGas + cantGas * 100) / volumenNuevo
        porcNuevoPetroleo = float(self.volumenActual * self.porcentajePetroleo) / volumenNuevo

        self.volumenActual = volumenNuevo
        self.porcentajeAgua = porcNuevoAgua
        self.porcentajePetroleo = porcNuevoPetroleo
        self.porcentajeGas = porcNuevoGas

        for p in self.parcelas:
            p.reinyeccion()

    def numPozos(self):
        res = 0
        for p in self.parcelas:
            res = res + 1 if p.tienePozo() else res
        return res


class Parcela:
    def __init__(self, profundidad, presionInicial, resistencia, yacimiento, formulasParcela):
        self.presionInicial = presionInicial
        self.presion = presionInicial
        self.profundidad = profundidad
        self.resistencia = resistencia
        self.yacimiento = yacimiento
        self.pozo = Excavacion(self)
        self.formulas = formulasParcela

    def extraer(self,numPozos):
        potencial = self.formulas.potencial(self.presion, numPozos)
        self.yacimiento.extraer(potencial)
        return potencial

    def reinyeccion():
    	presion = self.formulas.reinyeccion(self.presionInicial, self.yacimiento.volumenActual(), self.yacimiento.volumenInicial())

    def abrirPozo():
        self.pozo = Pozo(self)

    def tienePozo(self):
        return type(self.pozo) is Pozo

    def pasarDia(self):
        volumenR = self.yacimiento.volumenInicial()
        volumenRi = self.yacimiento.volumenActual()
        numPozos = self.yacimiento.numPozos()
        presion = self.formulas.presionAlSiguienteDia(self.presion, volumenR, volumenRi, numPozos)


class Excavacion:
    def __init__(self, parcela):
        self.parcela = parcela
        self.metrosExcavados = 0
   
    def excavar(self,metros):
        self.metrosExcavados = min(self.metrosExcavados + metros, self.parcela.profundidad())
        if (self.metrosRestantes())==0:
            self.parcela.abrirPozo()

    def metrosRestantes(self):
        return (self.parcela.profundidad() - self.metrosExcavados)


class Pozo:
    def __init__(self, parcela):
        self.parcela = parcela

    def extraer(self,numPozos):
        # El extractor hace la verificacion si se puede extraer de acuerdo a las estructuras disponibles
        productoExtraido = self.parcela.extraer(numPozos)
        return productoExtraido