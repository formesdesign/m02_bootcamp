from functools import reduce

def doble(x):
    return x+x

def esPar(x):
    return x % 2 ==0

lista = [1, 3, -1, 9, 15]

# map es un Operador, treballar sobre els parametres d'entrada i map fa la transformació
listaDobles = map(lambda x: x*2, lista)
listaDobles1 = map(doble, lista)


# filtres es un Operador, només flitra la condició que li marques
listaPares = filter (lambda x: x % 2 == 0, lista)
listaPares1 = filter (esPar, lista)


# REduce, va a procesat el valors de la llista pero els va a transformar en un unic valor
# per utilitzar reduce tenim que fer un import from functools import reduce

sumatorio = reduce(lambda x,y: x+y, lista)
sumatorioDobles = reduce(lambda x,y: x+y*2, lista)

suma100 = reduce(lambda x,y: x+y, range(101))

print(list(listaPares))
print(list(listaPares1))

print(sumatorio)
print(sumatorioDobles)

print(suma100)






