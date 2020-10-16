#Funcio RECURSIVIDAD, es un funció que per ejecutar-se se invoca a si mateixa
# hem de tindre en compte que l'hem de parar

def retrocontador(e):
    print("{},".format(e), end="")
    
    if e>0:
        retrocontador(e-1)

retrocontador(10)

