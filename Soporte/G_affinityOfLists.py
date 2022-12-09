# Devuelve la afinidad de una lista según la relación entre todas tus palabras

import time, datetime
from itertools import permutations
from Soporte.E_queryDatabase import getRelationFrom2Words

tiempoInicio = time.time()

# Crea las permutaciones de una lista y retorna la afinidad total de lista hallando la afinidad entre todos los pares posibles de palabras
# La afinidad se define como que la relación dos palabras sea "RelatedTo"
def getAffinity(lista):
    afinidad = 0
    perm = permutations(lista, 2)
    for i in list(perm):
        relacion = getRelationFrom2Words(i)
        for i in relacion:
            if i[0] == "RelatedTo":
                afinidad += 1
    return afinidad

# Imprime la afinidad de una lista de listas de palabras
def printAffinities(lista):
    for i in lista:
        print(getAffinity(i))

# ------------- METRICAS ------------- 
tiempoEjecuccion = time.time() - tiempoInicio
print()
print()
print(f"Tiempo de procesamiento: {str(datetime.timedelta(seconds=tiempoEjecuccion))}")