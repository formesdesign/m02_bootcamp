#FUNCIONS LAMBDA: son funcions anonimes
# serveis per les funciones de 1r nivell
#el return no se fica en lambda

# opció 1
# from funciones1nivel import sumaTodos
# print(sumaTodos(3, lambda x: x**3))

# opció 2

from funciones1nivel import sumaTodos

doble  = lambda x : x*2
triple = lambda x : x*3

print(sumaTodos(3, doble))
print(sumaTodos(100, triple))


