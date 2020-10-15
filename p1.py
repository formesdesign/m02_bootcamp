def sumaTodos(limitTo):
    resultado = 0
    for i in range(0, limitTo+1):
        resultado += i
        
    return resultado

def sumaTodosLosQuadrados(limitTo):
    resultado = 0
    for i in range(limitTo+1):
        resultado += i*i
    
    return resultado

    
print (sumaTodos (100))
print (sumaTodosLosQuadrados (5))
