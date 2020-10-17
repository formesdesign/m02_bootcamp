#per definir un objecte primer definin una classe class
#el nom de la classe sempre comença per mayuscula
# i sempre té la funcio def __init__ (funció constructora)
#sempre fiquem self, xq s'entengui el parametros d'aquesta classe es de python

class Gos():
    def __init__ (self, nom, edat, pes):
        self.nom = nom
        self.edat = edat
        self.pes = pes
        
    def lladrar(self):
        if self.pes >=8:
            print("GUAU, GUAU")
        else:
            print("Guau, guau")
            
    def __str__(self):
        return "Gos {}, edat: {}, pes{}" .format(self.nom, self.edat, self.pes)


#Herencia i subclasses
    #estem deient que herede de la classe Gos    
class GosAssistencia(Gos):
    trabajando = False

    def __init__ (self, nom, edat, pes, amo):
        Gos.__init__ (self, nom, edat, pes)
        self.amo = amo
       
    def __str__(self):
        return "Gos d'assistècia {}" .format(self.amo)
    
    def passetjar(self):
        print("{} ajude al meu amo, {} a passetjar".format(self.nom, self.amo))

    def lladrar(self):
        if self.__trabajando:
            print("Uyyyy, no puc lladrar")
        else:
            Gos.lladrar(self)
            
 #Estem creant un "metodo" para informar: es un atribut privat, només té les ratlles davant
            
    def trabajando(self, valor=None):
        if valor ==None:
            return self.__trabajando
        else:
            Gos.__trabajando = valor
            
            
class Timit():
    def __init__(self, nombre):
        sefl.__nombre = nombre
        
    def preguntatnom(self):
        return self.__nombre



