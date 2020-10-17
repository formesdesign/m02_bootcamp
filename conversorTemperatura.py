# Conversor de temperatura

class Termometre():
    def __init__(self):
        self.__unidadM = "C"
        self.__temperatura = 0
        
    def __conversor (self, temperatura, unidad):
        if unidad == "C":
            return "{}º F".format(temperatura * 9/5 + 32)
        elif unidad == "F":
            return "{}º C".format((temperatura -32) * 5/9)
        else:
            return "uniadad incorrecta"
        
    def __str__(self):
        return "{}º {}".format(self.temperatura, self.unidadM)
    
    def unidadMedida(self, uniM=None):
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == "F" or uniM == "C":
                self.__unidadM  = uniM
                
    def temp(self, temperatura=None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
            
    def mide(sefl, uniM=None):
        if uniM == None or uniM == self.unidadM:
            return self.__str__()
        else:
            if uniM == "F" or uniM =="C":
                return self.conversor(self.__temperatura, self.__unidadM)
            else:
                return self.__str__()
        

        

        