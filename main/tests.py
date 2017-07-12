'''
Created on 12 jul. 2017

@author: Luis
'''
import unittest
import main.simulacion as simulacion

class TestsSimulacion(unittest.TestCase):
    def test01(self):
        miSim = simulacion.Simulacion()
        log = miSim.miLog
        lineaEscrita = log.comenzar()
        
        self.assertEqual(lineaEscrita, "Comienzo de simulacion\n")
        
    def test02(self):
        miSim = simulacion.Simulacion()
        log = miSim.miLog
        log.comenzar()
        lineaEscrita = log.escribirLinea("lalalalalalal")
        self.assertEqual(lineaEscrita, "lalalalalalal\n")
        
    def test03(self):
        miSim = simulacion.Simulacion()
        log = miSim.miLog
        log.comenzar()
        lineaEscrita = log.escribirLinea("lalalalalalal")
        lineaEscrita = log.escribirLinea("hello there")
        self.assertNotEqual(lineaEscrita, "lalalalalalal\n")
        self.assertEqual(lineaEscrita, "hello there\n")