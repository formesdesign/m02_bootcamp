lista = [1, 3, -1, 9, 15]

# map es un Operador, treballar sobre els parametres d'entrada i map fa la transformació
listaDobles = map(lambda x: x*2, lista)

# filtres es un Operador, només flitra la condició que li marques
listaPares = filter (lambda x: x % 2 == 0, lista)