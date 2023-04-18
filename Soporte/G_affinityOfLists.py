# Devuelve la afinidad de una lista según la relación entre todas tus palabras

import itertools as itools
import Soporte.E_queryDatabase as queryDB

# Crea las permutaciones de una lista y retorna la afinidad total de lista hallando la afinidad entre todos los pares posibles de palabras
# La afinidad se define como que la relación dos palabras sea "RelatedTo"
def getAffinity(lista, ):
    afinidad = 0
    wantedRelations = ["RelatedTo", "Synonym", "UsedFor"]
    perm = itools.permutations(lista, 2)
    #comb = itools.combinations(lista, 2)
    for i in list(perm):
        relacion = queryDB.getRelationFrom2Words(i)
        for i in relacion:
            if i[0] in wantedRelations:
                afinidad += 1
    return afinidad

# Imprime la afinidad de una lista de listas de palabras
def printAffinities(lista):
    for i in lista:
        print(getAffinity(lista))