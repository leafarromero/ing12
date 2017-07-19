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
        self.metrosExcavados = min(self.metrosExcavados + metros,self.parcela.profundidad)
        if (self.metrosRestantes())==0:
            self.parcela.pozo = Pozo(self.parcela)
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
        self.escribirLinea("Ingreso de dolares: " + Str(dinero)  + "\n")

    def gasto(self,dinero):
        self.dineroGanado -= dinero
        self.escribirLinea("Gasto de dolares: " + Str(dinero)  + "\n")

    def ventas(self):
        self.log.escribirLinea("dolares obtenidos hasta la fecha: " + Str(self.dineroGanado))

    def gastos(self):
        self.log.escribirLinea("dolares gastados hasta la fecha: " + Str(self.dineroPerdido))

    def balance(self):
        self.log.escribirLinea("ganancias hasta la fecha: " + Str(self.dineroGanado - self.dineroPerdido))



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
    def __init__(self, alpha1 = 0.3, alpha2 = 0.01): 
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


class Bombeador:
    def __init__(self,tanquesAgua,tanquesGas,plantasSeparadoras,yacimiento,log):
        self.tanquesAgua = tanquesAgua
        self.tanquesGas = tanquesGas
        self.plantasSeparadoras = plantasSeparadoras
        self.yacimiento = yacimiento
        self.log = log
    
    def extraer (pozos):
        for poz in pozos:
            composicionDeCrudo = (self.yacimiento.porcentajePetroleo,self.yacimiento.porcentajeGas,self.yacimiento.porcentajeAgua)
            materialesSeparados = self.procesar(poz.extraer())
            self.log.escribirLinea("litros de gas destilados: " + Str(litrosDeGas) + "\n")
            self.log.escribirLinea("litros de agua destilados: " + Str(litrosDeAgua) + "\n")
            self.almacenarAgua(materialesSeparados[0])
            self.almacenarGas(materialesSeparados[1])
    
    def procesar (self,composicionDeCrudo,litrosDeCrudo):
        materialesSeparados = (0,0)

        for planta in (self.plantasSeparadoras):
            cant = min(planta.cantidadQuePuedeProcesarEnDia(),litrosDeCrudo)
            if cant!=0:
                materialesSeparadosEnPlanta = planta.procesar(composicionDeCrudo,cant)
                materialesSeparados[0] = materialesSeparados[0] + materialesSeparadosEnPlanta[0]
                materialesSeparados[1] = materialesSeparados[1] + materialesSeparadosEnPlanta[1]
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo==0:
                break
        return materialesSeparados
   
    def almacenarGas(self,litrosDeGas):
        for tanq in self.tanquesGas:
            cant = min(tanq.cantidadQuePuedeAlmacenar(),litrosDeGas)
            if cant!=0:
                tanq.almacenar(composicionDeCrudo,cant)
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo==0:
                break

    def almacenarAgua(self,litrosDeAgua):
        for tanq in self.tanquesAgua:
            cant = min(tanq.cantidadQuePuedeAlmacenar(),litrosDeAgua)
            if cant!=0:
                tanq.almacenar(composicionDeCrudo,cant)
                litrosDeCrudo = litrosDeCrudo - cant
            if litrosDeCrudo==0:
                break
class Tanque:
    def __init__(self,capacidadEnLitros):
        self.capacidadEnLitros = capacidadEnLitros
        self.litrosAlmacenados = 0
    def cantidadQuePuedeAlmacenar(self):
        self.capacidadEnLitros - self.litrosAlmacenados
    def almacenar(self,litros):
        if (self.litrosAlmacenados+litros > self.capacidadEnLitros):
            raise ValueError
        else:
            self.litrosAlmacenados = self.litrosAlmacenados+litros

    def retirar(litros):
        if(litrosAlmacenados < litros):
            raise ValueError
        else:
            self.litrosAlmacenados = self.litrosAlmacenados - litros

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
        #return MaterialesSeparados(litrosDeAgua,litrosDeGas)
        return (litrosDeAgua,litrosDeGas)
    def pasarDia(self):
        self.litrosProcesadosEnDia = 0


#class MaterialesSeparados:
#    def __init__(self,litrosDeAgua,litrosDeGas):
#        self.litrosDeAgua = litrosDeAgua
#        self.litrosDeGas = litrosDeGas
#
#    def agregar(otrosMaterialesSeparados):
#        litrosDeAgua = self.litrosDeAgua + otrosMaterialesSeparados.litrosDeAgua
#        litrosDeGas = self.litrosDeGas + otrosMaterialesSeparados.litrosDeGas
#        return MaterialesSeparados(litrosDeAgua,litrosDeGas)

class VendedorDePetroleo:
    def __init__(self,dolarPorLitro,log):
        self.dolarPorLitro = dolarPorLitro
        self.log = log
    def vender(litrosDePetroleo):
        log.escribirLinea("litros de petroleo destilados: " + Str(litrosDePetroleo) + "\n")
        dinero = self.dolarPorLitro*litrosDePetroleo
        log.venta(dinero)



