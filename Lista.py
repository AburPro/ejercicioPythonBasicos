import random
listaAleatoria = random.sample(range(1, 11), 10)
print("Lista: ", listaAleatoria)
print("")
listaAscendente = sorted(listaAleatoria)
print("Lista en orden ascendente: ", listaAscendente)
print("")
listaDescendente = sorted(listaAleatoria, reverse=True)
print("Lista en orden descendente: ",listaDescendente)