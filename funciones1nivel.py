#les funciones retornen funcions

def normal(x):
    return x

def cuadrado (y):
    return y*y

def cubo(z):
    return z**3

def sumaTodos(limitTo, f): #f es de la funció (crida a les dos definides primer)
    resultado = 0
    for i in range(0, limitTo+1):
        resultado += f(i)
        
    return resultado

if __name__ == "__main__":
    print (sumaTodos (100, normal))
    print (sumaTodos (3, cuadrado))
