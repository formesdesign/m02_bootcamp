from functools import reduce



lista = [1, 3, -1, 9, 15]

sumatorio = reduce(lambda x,y: x+y, lista)
# creem una cópia de la llista [:]
l = lista[:]
# afegim el 0 xq la llista comence des de la posició 0
l.insert(0,0)
sumatorioDobles = reduce(lambda x,y: x+y*2, lista)

print(sumatorio)
print(sumatorioDobles)


