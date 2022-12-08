# Devuelve la afinidad de una lista según la relación entre todas tus palabras

import time, datetime
from itertools import permutations
from Soporte.E_queryDatabase import getRelationFrom2Words

tiempoInicio = time.time()

def getAffinity(lista):
    afinidad = 0
    print(lista)
    perm = permutations(lista, 2)
    for i in list(perm):
        relacion = getRelationFrom2Words(i)
        print(i, end=" ")
        for i in relacion:
            print(i, end=", ")
            if i[0] == "RelatedTo":
                afinidad += 1
        print()
    return afinidad

def printAffinities(lista):
    for i in lista:
        print(getAffinity(i))

# ------------- METRICAS ------------- 
tiempoEjecuccion = time.time() - tiempoInicio
print()
print()
print(f"Tiempo de procesamiento: {str(datetime.timedelta(seconds=tiempoEjecuccion))}")