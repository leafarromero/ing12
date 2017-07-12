'''
Created on 12 jul. 2017

@author: Luis
'''
import unittest
import main.simulacion as simulacion

class TestsLog(unittest.TestCase):
    def test01(self):
        log = simulacion.Log("log")
        lineaEscrita = log.comenzar()
        
        self.assertEqual(lineaEscrita, "Comienzo de simulacion\n")
        
    def test02(self):
        log = simulacion.Log("log")
        log.comenzar()
        lineaEscrita = log.escribirLinea("lalalalalalal")
        self.assertEqual(lineaEscrita, "lalalalalalal\n")
        
    def test03(self):
        log = simulacion.Log("log")
        log.comenzar()
        lineaEscrita = log.escribirLinea("lalalalalalal")
        lineaEscrita = log.escribirLinea("hello there")
        self.assertNotEqual(lineaEscrita, "lalalalalalal\n")
        self.assertEqual(lineaEscrita, "hello there\n")

    def test04(self):
        log = simulacion.Log("log")
        log.comenzar()
        log.escribirLinea("algo")
        

        
        
