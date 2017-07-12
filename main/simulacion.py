'''
Created on 12 jul. 2017

@author: Luis
'''
class Simulacion:
    
    def __init__(self):
        self.miLog = Log("log")
        
    
    def comenzar(self):
        pass
    
    def simularDia(self):
        pass
    
    def contexto(self):
        pass
    

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