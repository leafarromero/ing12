"""
Created on 12 jul. 2017

@author: Luis
"""

from bombeador import Bombeador
from constructor import Constructor
from rigsYExcavadores import Excavador, RigManager, AdministradorDeRigs
from vendedor_gas import VendedorGas
from yacimiento import Yacimiento


class Simulacion:
    def __init__(self, politicaAlquilerRigs, politicaExcavacion, politicaBombeo, politicaConstruccionPlantas,
                 politicaConstruccionTanquesAgua, politicaConstruccionTanquesGas, politicaVentaGas):
        self.log = Log("log")
        self.diaNumero = 0
        self.contexto = Contexto("./config/")
        self.scheduler = Scheduler(self.log, self.contexto, politicaAlquilerRigs, politicaExcavacion, politicaBombeo,
                                   politicaConstruccionPlantas, politicaConstruccionTanquesAgua,
                                   politicaConstruccionTanquesGas, politicaVentaGas, "./config/")
        self.finalizacion = Finalizacion()

    def comenzar(self):
        self.log.comenzar()

    def simularDia(self):
        self.log.escribirLinea("Comienza el dia " + str(self.diaNumero))
        self.scheduler.ejecutarPoliticas(self.contexto)
        self.contexto.pasarDia(self.log)
        self.diaNumero += 1

    def finalize(self):
        fin = self.finalizacion.finalize()
        if fin:
            self.log.ventas()
            self.log.gastos()
            self.log.balance()
        return fin


class CriterioFinalizacion:

    def finalize(self,contexto,dilusion_critica):
        pass


class Finalizacion(CriterioFinalizacion):
    def __init__(self):
        pass

    def finalize(self, contexto, dilusion_critica):
        if contexto.yacimiento.porcentajePetroleo < dilusion_critica:
            return True
        return False


class Log:
    def __init__(self, archivo):
        self.miArchivo = archivo
        self.dineroGanado = 0
        self.dineroPerdido = 0

    def comenzar(self):
        with open(self.miArchivo, "w") as file:
            file.write("Comienzo de simulacion \n")

        return "Comienzo de simulacion\n"

    def escribirLinea(self, texto):
        with open(self.miArchivo, "a") as file:
            file.write(texto + "\n")
        return texto + "\n"

    def venta(self, dinero):
        self.dineroGanado += dinero
        self.escribirLinea("Ingreso de dolares: " + str(dinero) + "\n")

    def gasto(self, dinero):
        self.dineroGanado -= dinero
        self.escribirLinea("Gasto de dolares: " + str(dinero) + "\n")

    def ventas(self):
        self.log.escribirLinea("dolares obtenidos hasta la fecha: " + str(self.dineroGanado))

    def gastos(self):
        self.log.escribirLinea("dolares gastados hasta la fecha: " + str(self.dineroPerdido))

    def balance(self):
        self.log.escribirLinea("ganancias hasta la fecha: " + str(self.dineroGanado - self.dineroPerdido))


class CompradorDeAgua:
    def __init__(self, log, confPath):
        self.log = log
        archivo = confPath + "compradorDeAgua.txt"
        with open(archivo, "r") as file:
            linea = file.readLine()
            self.dolaresPorLitroDeAgua = float(linea)

    def comprar(self, litrosDeAgua):
        self.log.escribirLinea("se compro " + str(litrosDeAgua) + "litros de agua\n")
        self.log.gasto(self.dolaresPorLitroDeAgua * litrosDeAgua)


class Scheduler:
    def __init__(self, log, contexto, politicaAlquilerRigs, politicaExcavacion, politicaBombeo,
                 politicaConstruccionPlantas, politicaConstruccionTanquesAgua, politicaConstruccionTanquesGas,
                 politicaVentaGas, confPath):
        self.excavador = Excavador(log, confPath)
        self.bombeador = Bombeador(log, contexto.estructuras, contexto.yacimiento, CompradorDeAgua(log, confPath))
        self.constructor = Constructor(log, contexto.estructuras, confPath)
        self.rigManager = RigManager(log, contexto.administradorDeRig)
        self.vendedorDeGas = VendedorGas(log, contexto.estructuras, confPath)

        self.politicaVentaGas = politicaVentaGas
        self.politicaAlquilerRigs = politicaAlquilerRigs
        self.politicaExcavacion = politicaExcavacion
        self.politicaBombeo = politicaBombeo
        self.politicaConstruccionPlantas = politicaConstruccionPlantas
        self.politicaConstruccionTanquesAgua = politicaConstruccionTanquesAgua
        self.politicaConstruccionTanquesGas = politicaConstruccionTanquesGas

    def ejecutarPoliticas(self, contexto):
        self.politicaVentaGas.decidir(contexto, self.vendedorDeGas)
        self.politicaAlquilerRigs.decidir(contexto, self.rigManager)
        self.politicaExcavacion.decidir(contexto, self.excavador)
        self.politicaBombeo.decidir(contexto, self.bombeador)
        self.politicaConstruccionPlantas.decidir(contexto, self.constructor)
        self.politicaConstruccionTanquesAgua.decidir(contexto, self.constructor)
        self.politicaConstruccionTanquesGas.decidir(contexto, self.constructor)


def Tanque(Estructura):
    def capacidad(self):
        pass

    def litros(self):
        pass

    def llenar(self, volumen):
        pass

    def retirar(self, volumen):
        pass


def TanqueGas(Tanque):
    def __init__(self, capacidad):
        self._capacidad = capacidad
        self._litros = 0

    def capacidad(self):
        return self._capacidad

    def litros(self):
        return self._litros

    def llenar(self, volumen):
        self._litros += volumen

    def retirar(self, volumen):
        self._litros -= volumen


def TanqueAgua(Tanque):
    def __init__(self, capacidad):
        self._capacidad = capacidad
        self._litros = 0

    def capacidad(self):
        return self._capacidad

    def litros(self):
        return self._litros

    def llenar(self, volumen):
        self._litros += volumen

    def retirar(self, volumen):
        self._litros -= volumen


class Estructuras(object):
    def __init__(self, estructuras):
        self._estructuras = estructuras


class Contexto:
    def __init__(self, confPath):
        self.yacimiento = Yacimiento(confPath)
        self.administradorDeRigs = AdministradorDeRigs(confPath)
        self.estructuras = Estructuras(confPath)

    def pasarDia(self, log):
        self.yacimiento.pasarDia()
        self.administradorDeRigs.pasarDia(log)
        self.estructuras.pasarDia()

    def yacimiento(self):
        return self.yacimiento

    def administradorDeRigs(self):
        return self.administradorDeRigs

    def estructuras(self):
        return self.estructuras


class Tanque:
    def __init__(self, capacidadEnLitros):
        self.capacidadEnLitros = capacidadEnLitros
        self._litrosAlmacenados = 0

    def cantidadQuePuedeAlmacenar(self):
        return self.capacidadEnLitros - self._litrosAlmacenados

    def almacenar(self, litros):
        if (self._litrosAlmacenados + litros > self.capacidadEnLitros):
            raise ValueError
        else:
            self._litrosAlmacenados = self._litrosAlmacenados + litros

    def retirar(self, litros):
        if (self._litrosAlmacenados < litros):
            raise ValueError
        else:
            self._litrosAlmacenados = self._litrosAlmacenados - litros

    def litrosAlmacenados(self):
        return self._litrosAlmacenados


class PlantaProcesadora:
    def __init__(self, litrosPorDia, vendedorDePetroleo):
        self._litrosPorDia = litrosPorDia
        self.litrosProcesadosEnDia = 0
        self.vendedorDePetroleo = vendedorDePetroleo

    def cantidadQuePuedeProcesarEnDia(self):
        return (self._litrosPorDia) - (self.litrosProcesadosEnDia)

    def procesarCrudo(self, composicionDeCrudo, litrosDeCrudo):
        if (litrosDeCrudo > self.cantidadQuePuedeProcesarEnDia()):
            raise ValueError
        litrosDePetroleo = composicionDeCrudo[0] * litrosDeCrudo / 100
        litrosDeAgua = composicionDeCrudo[1] * litrosDeCrudo / 100
        litrosDeGas = composicionDeCrudo[2] * litrosDeCrudo / 100
        self.vendedorDePetroleo.vender(litrosDePetroleo)
        return (litrosDeAgua, litrosDeGas)

    def pasarDia(self):
        self.litrosProcesadosEnDia = 0

    def litrosPorDia(self):
        return self._litrosPorDia


class VendedorDePetroleo:
    def __init__(self, dolarPorLitro, log):
        self.dolarPorLitro = dolarPorLitro
        self.log = log

    def vender(self, litrosDePetroleo):
        self.log.escribirLinea("litros de petroleo destilados: " + str(litrosDePetroleo) + "\n")
        dinero = self.dolarPorLitro * litrosDePetroleo
        self.log.venta(dinero)
