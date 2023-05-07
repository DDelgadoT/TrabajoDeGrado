# Devuelve la afinidad de una lista según la relación entre todas tus palabras

import itertools as itools
import Soporte.E_queryDatabase as queryDB

# RETORNO de la afinidad total de lista
# Para verificar la afinidad se crean las permutaciones de una lista y se realiza la verifiación
# La afinidad se define como que la relación dos palabras sea "RelatedTo", "Synonym" o "UsedFor"
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

# SOPORTE
# Imprime la afinidad de una lista de listas de palabras
def printAffinities(lista):
    for i in lista:
        print(getAffinity(lista))