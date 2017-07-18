'''
Created on 12 jul. 2017

@author: Luis
'''
import math
class Simulacion:
    
    def __init__(self):
        self.log = Log("log")
        self.diaNumero = 0
        self.scheduler = Scheduler()
        self.contexto = Contexto()
        
    def comenzar(self):
        self.log.comenzar()
    
    def simularDia(self):
        self.log.escribirLinea("Comienza el dia " + self.diaNumero)
        self.scheduler.ejecutarPoliticas(self.contexto)
        self.diaNumero += 1
        
class Excavacion:
    def __init__(self,parcela):
        self.parcela = parcela
        self.metrosExcavados = 0
    def excavar(self,metros):
        self.metrosExcavados = self.metrosExcavados + metros
        if (self.metrosRestantes())<=0:
            self.parcela.pozo = Pozo(self)
    def metrosRestantes(self):
        return (self.parcela.profundidad - self.metrosExcavados)

class Log:
    def __init__(self, archivo):
        self.miArchivo = archivo
        self.dineroGanado = 0
        self.dineroPerdido = 0
        
    def comenzar(self):
        with open(self.miArchivo , "w") as file:
            file.write("Comienzo de simulacion \n")
            
        return "Comienzo de simulacion\n"          
            
    def escribirLinea(self, texto):
        with open(self.miArchivo , "a") as file:
            file.write(texto + "\n")
        return texto + "\n"
    def venta(self,dinero):
        self.dineroGanado += dinero
        self.escribirLinea



class Scheduler:
    def __init__(self):
        self.politicas = []
        
    def ejecutarPoliticas(self,contexto):
        for politica in self.politicas:
            politica.decidir(contexto)
    
    def agregarPolitica(self, politica):
        self.politicas.append(politica)


class Contexto:
    def __init__(self):
        self.formulas = Formulas()
        self.yacimiento = Yacimiento()
        #self.parametros = Parametros()
        #self.rigs = []
        #self.estructuras = Estructuras()
    
    
class Formulas:
    def __init__(self, alpha1 = 0.1, alpha2 = 0.01): 
        #deberian estar aca??
        if (0.1 <= alpha1 <= 0.6):
            self.alpha1 = alpha1 
        else:
            raise ValueError
        
        if (0.005 <= alpha2 <= 0.01):
            self.alpha2 = alpha2
        else:
            raise ValueError
        
     
    def potencialVolDiarioXPozo(self,presionAnterior,volumenRi,numPozos):
        pbcti = self.presionAlSiguienteDia(presionAnterior, volumenRi, numPozos)
        sumando1 = self.alpha1 * (pbcti/numPozos)
        sumando2 = self.alpha2 * ((pbcti/numPozos)^2)
        return sumando1 + sumando2
        
    
    def presionAlSiguienteDia(self, presionAnterior,volumenRi,numPozos):
        betaI = self.betaI(volumenRi, numPozos)
        return presionAnterior * (math.e ^ -(betaI))
    
    def betaI(self, volumenR, volumenRi, numPozos):
        return (0.1 * (volumenRi / volumenR)) / ((numPozos)^(2/3))


class Yacimiento:
    def __init__(self):

        #Habria que pasarle los parametros con los que se construye
        self.parcelas = [] 
        self.volumen = 0
        self.porcentajePetroleo = 100
        self.porcentajeGas = 0
        self.porcentajeAgua = 0
        self.globalExtraido = 0
        self.globalReinyectado = 0
        

    def parcelas(self):
        return self.parcelas

    def volumenInicial(self):
    	return self.volumenInicial

	def volumenActual(self):
    	return self.volumenActual

	def globalExtraido(self):
    	return self.globalExtraido

    def globalReinyectado():
    	return self.globalReinyectado

    def extraer(cantProducto):
        self.volumenActual -= cantProducto
        self.globalExtraido += cantProducto

    def reinyectarAgua(cantAgua):
        #sacar las cuentas para cambiar el porcentaje y volumen
        volumenNuevo = self.volumenActual + cantAgua

        porcNuevoAgua = float(self.volumenActual * float(self.porcentajeAgua) / 100+ cantAgua) / volumenNuevo
        porcNuevoGas = float(self.volumenActual * float(self.porcentajeGas) / 100) / volumenNuevo
        porcNuevoProducto = float(self.volumenActual * float(self.porcentajePetroleo) / 100) / volumenNuevo

        self.volumenActual = volumenNuevo
        self.porcentajeAgua = porcNuevoAgua
        self.porcentajePetroleo = porcNuevoProducto
        self.porcentajeGas = porcNuevoGas
        self.globalReinyectado += cantAgua

        for p in self.parcelas:
        	p.reinyeccion()

    def reinyectarGas(cantGas):
        #sacar las cuentas para cambiar el porcentaje y volumen
        volumenNuevo = self.volumenActual + cantGas

        porcNuevoAgua = float(self.volumenActual * float(self.porcentajeAgua)) / volumenNuevo
        porcNuevoGas = 100 * float(self.volumenActual * float(self.porcentajeGas) / 100 + cantGas) / volumenNuevo
        porcNuevoPetroleo = float(self.volumenActual * float(self.porcentajePetroleo)) / volumenNuevo

        self.volumenActual = volumenNuevo
        self.porcentajeAgua = porcNuevoAgua
        self.porcentajePetroleo = porcNuevoPetroleo
        self.porcentajeGas = porcNuevoGas
        self.globalReinyectado += cantGas

		for p in self.parcelas:
        	p.reinyeccion()

    #Si tengo un solo yacimiento y un solo reservorio, no tiene sentido mandar la informacion
    #de reservorio a una clase separada, dejaria a yacimiento vacio


class Parcela:
    def __init__(self, profundidad, presionInicial, resistencia, yacimiento):
        self.presionInicial = presionInicial
        self.presionActual = presionInicial
        self.profundidad = profundidad
        self.resistencia = resistencia
        self.yacimiento = yacimiento
        self.pozo = Excavacion(self)

    def extraer():
        #Cambiar presion
        #TODO
        producto = "HACER LOS CALCULOS DEL POTENCIAL DE PRODUCTO"
        self.yacimiento.extraer(producto)
        return producto

    def reinyeccion():
    	pass

class pozo:
    def __init__(self, parcela):
        self.parcela = parcela

    def extraer():
        #El extractor hace la verificacion si se puede extraer de acuerdo a las estructuras disponibles
        productoExtraido = self.parcela.extraer()
        return productoExtraido

        
    def reinyectarGas():
        #El extractor hace la verificacion si se puede reinyectar de acuerdo a las estructuras disponibles
        self.parcela.reinyectarGas()

    def reinyectarAgua(cantAgua):
        #El extractor hace la verificacion si se puede reinyectar de acuerdo a las estructuras disponibles
        self.parcela.reinyectarAgua(cantAgua)


class Bombeador:
    def __init__(self,tanquesAgua,tanquesGas,plantasSeparadoras,yacimiento):
        self.tanquesAgua = tanquesAgua
        self.tanquesGas = tanquesGas
        self.plantasSeparadoras = plantasSeparadoras
        self.yacimiento = yacimiento
    
    def extraer (pozos):
        for poz in pozos:
            composicionDeCrudo = (self.yacimiento.porcentajePetroleo,self.yacimiento.porcentajeGas,self.yacimiento.porcentajeAgua)
            materialesSeparados = self.procesar(poz.extraer())
            self.almacenarAgua(materialesSeparados.litrosDeAgua)
            self.almacenarGas(materialesSeparados.litrosDeGas)
            #self.vender(materialesSeparados.litrosDePetroleo)
    
    def procesar (self,composicionDeCrudo,litrosDeCrudo):
        materialesSeparados = MaterialesSeparados(0,0)

        for planta in (self.plantasSeparadoras):
            cant = min(cantidadQuePuedeProcesarEnDia(planta),litrosDeCrudo)
            if cant!=0:
                materialesSeparados = agregar(materialesSeparados, planta.procesar(composicionDeCrudo,cant))
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo==0:
                break
        return materialesSeparados
   
    def almacenarGas(self,litrosDeGas):
        for tanq in self.tanquesGas:
            cant = min(cantidadQuePuedeAlmacenar(tanq),litrosDeGas)
            if cant!=0:
                tanq.almacenar(composicionDeCrudo,cant)
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo==0:
                break

    def almacenarAgua(self,litrosDeAgua):
        for tanq in self.tanquesAgua:
            cant = min(cantidadQuePuedeAlmacenar(tanq),litrosDeAgua)
            if cant!=0:
                tanq.almacenar(composicionDeCrudo,cant)
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo==0:
                break

class PlantaProcesadora:
    def __init__(self,litrosPorDia,vendedorDePetroleo):
        self.litrosPorDia = litrosPorDia
        self.litrosProcesadosEnDia = 0
        self.vendedorDePetroleo = vendedorDePetroleo
    def cantidadQuePuedeProcesarEnDia(self):
        return (self.litrosPorDia) - (self.litrosProcesadosEnDia)

    def procesar(self,composicionDeCrudo,litrosDeCrudo):
        if (litrosDeCrudo > self.cantidadQuePuedeProcesarEnDia()):
            raise ValueError
        litrosDePetroleo = composicionDeCrudo[0] * litrosDeCrudo/100
        litrosDeAgua = composicionDeCrudo[1] * litrosDeCrudo/100
        litrosDeGas = composicionDeCrudo[2] * litrosDeCrudo/100
        self.vendedorDePetroleo.vender(litrosDePetroleo)
        return MaterialesSeparados(litrosDeAgua,litrosDeGas)
    def pasarDia(self):
        self.litrosProcesadosEnDia = 0


class MaterialesSeparados:
    def __init__(self,litrosDeAgua,litrosDeGas):
        self.litrosDeAgua = litrosDeAgua
        self.litrosDeGas = litrosDeGas

    def agregar(otrosMaterialesSeparados):
        litrosDeAgua = self.litrosDeAgua + otrosMaterialesSeparados.litrosDeAgua
        litrosDeGas = self.litrosDeGas + otrosMaterialesSeparados.litrosDeGas
        return MaterialesSeparados(litrosDeAgua,litrosDeGas)

class VendedorDePetroleo:
    def __init__(self,dolarPorLitro,log):
        self.dolarPorLitro = dolarPorLitro
        self.log = log
    def vender(litrosDePetroleo):
        dinero = self.dolarPorLitro*litrosDePetroleo
        log.venta(dinero)

class ComposicionDeCrudo:
    def __init__(self,porcentajePetroleo,porcentajeGas):
        if (0<=porcentajePetroleo+ porcentajeGas<=100):
            self.porcentajePetroleo = porcentajePetroleo
            self.porcentajeGas = porcentajeGas
            self.porcentajeAgua = 100 - porcentajePetroleo - porcentajeGas
        else:
            raise ValueError


