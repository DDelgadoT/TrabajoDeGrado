#  Generación de oraciones

import time, datetime, random
from gettingRelationsFromDB import returnSelectedWords
from Soporte.G_affinityOfLists import getAffinity
import Soporte.F_cleaningOfListOfWords as F

tiempoInicio = time.time()

# RETORNO de una muestra de una lista de palabras limpias de stopwords y singularizadas
def getCombinationOfWords(listOfWords, numberOfWordsPerSample, numberOfSentences):
    sampleSelectedWords = list() # Lista de palabras que se van a usar para hacer oraciones
    listOfWords = F.cleaning(listOfWords)
    while numberOfSentences > 0:
        auxSample = random.sample(listOfWords, numberOfWordsPerSample)
        auxSample.sort()
        if auxSample not in sampleSelectedWords:
            sampleSelectedWords.append(auxSample)
            numberOfSentences = numberOfSentences - 1
    return sampleSelectedWords

# GENERACIÓN de oraciones con una lista de palabras organizadas alfabéticamente
def getSentenceWithSortedOrder(words):
    from keytotext import pipeline # Se coloca aquí para evitar aumentar el tiempo de ejecucción
    nlp = pipeline("k2t-base")
    print("----------------------------------------------------------------")
    print("Oraciones con las palabras organizadas")
    for i in words:
        print(i)
        print("Oración: ", end="")
        print(nlp(i))

# GENERACIÓN de oraciones con una lista de palabras desorganizadas alfabéticamente
def getSentenceWithRandomOrder(words):
    from keytotext import pipeline # Se coloca aquí para evitar aumentar el tiempo de ejecucción
    nlp = pipeline("k2t-base")
    print("----------------------------------------------------------------")
    print("Oraciones con las palabras desorganizadas")
    for i in range(len(words)):
        words[i] = random.sample(words[i], len(words[i]))
    for i in words:
        print(i)
        print("Oración: ", end="")
        print(nlp(i))

# GENERACIÓN de oraciones
def generarOraciones():
    listOfWords = returnSelectedWords() # Palabras elegidas por heurística
    sampleSelectedWords = getCombinationOfWords(listOfWords, 5, 5) # Se eligen 5 oraciones de 5 palabras cada una
    print(sampleSelectedWords) # Lista de la muestra de palabras
    return
    getSentenceWithSortedOrder(sampleSelectedWords)
    getSentenceWithRandomOrder(sampleSelectedWords)

generarOraciones()

# ------------- METRICAS ------------- 
tiempoEjecuccion = time.time() - tiempoInicio
print()
print()
print(f"Tiempo de procesamiento: {str(datetime.timedelta(seconds=tiempoEjecuccion))}")