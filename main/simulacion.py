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
        

class Log:
    def __init__(self, archivo):
        self.miArchivo = archivo
        
    def comenzar(self):
        with open(self.miArchivo , "w") as file:
            file.write("Comienzo de simulacion \n")
            
        return "Comienzo de simulacion\n"          
            
    def escribirLinea(self, texto):
        with open(self.miArchivo , "a") as file:
            file.write(texto + "\n")
            
        return texto + "\n"


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
        self.porcentajeProducto = 100
        self.porcentajeGas = 0
        self.porcentajeAgua = 0
        

    def parcelas(self):
        return self.parcelas

    def extraer(cantProducto):
        #sacar las cuentas para cambiar el porcentaje y volumen
        #TODO
        pass

    def reinyectarAgua(cantAgua):
        #sacar las cuentas para cambiar el porcentaje y volumen
        #TODO
        pass

    def reinyectarGas(cantGas):
        #sacar las cuentas para cambiar el porcentaje y volumen
        #TODO
        pass

    #Si tengo un solo yacimiento y un solo reservorio, no tiene sentido mandar la informacion
    #de reservorio a una clase separada, dejaria a yacimiento vacio


class Parcela:
    def __init__(self, profundidad, presion, resistencia, yacimiento):
        self.presion = presion
        self.profundidad = profundidad
        self.resistencia = resistencia
        self.yacimiento = yacimiento

    def abrirPozo(self, pozo):
        self.pozo = Pozo(self)

    def extraer():
        #Cambiar presion
        #TODO
        producto = "HACER LOS CALCULOS DEL POTENCIAL DE PRODUCTO"
        self.yacimiento.extraer(producto)
        return producto

    def reinyectarAgua(cantAgua):
        #Cambiar presion
        #TODO
        self.yacimiento.reinyectarAgua(cantAgua)


    def reinyectarGas(cantGas):
        #Cambiar presion
        #TODO
        self.yacimiento.reinyectarGas(cantGas)


class Pozo:
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
    def __init__(self,tanquesAgua,tanquesGas,plantasSeparadoras):
        self.tanquesAgua
        self.tanquesGas
        self.plantasSeparadoras
    
    def extraer (pozos):
        for poz in pozos:
            materialesSeparados = self.procesar(poz.extraer())
            self.almacenarAgua(materialesSeparados.litrosDeAgua)
            self.almacenarGas(materialesSeparados.litrosDeGas)
            self.vender(materialesSeparados.litrosDePetroleo)
    
    def procesar (self,composicionDeCrudo,litrosDeCrudo):
        materialesSeparados = MaterialesSeparados(0,0,0)
        
        for planta in (self.plantasSeparadoras):
            cant = min(cantidadQuePuedeProcesar(planta),litrosDeCrudo)
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



class MaterialesSeparados:
    def __init__(self,litrosDeAgua,litrosDeGas,litrosDePetroleo):
        self.litrosDeAgua = litrosDeAgua
        self.litrosDeGas = litrosDeGas
        self.litrosDePetroleo = litrosDePetroleo

    def agregar(otrosMaterialesSeparados):
        litrosDeAgua = self.litrosDeAgua + otrosMaterialesSeparados.litrosDeAgua
        litrosDeGas = self.litrosDeGas + otrosMaterialesSeparados.litrosDeGas
        litrosDePetroleo = self.litrosDePetroleo + otrosMaterialesSeparados.litrosDePetroleo
        return MaterialesSeparados(litrosDeAgua,litrosDeGas,litrosDePetroleo)