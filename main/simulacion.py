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
        #self.parametros = Parametros()
        #self.yacimiento = Yacimiento()
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
    
    
    
    
    
    