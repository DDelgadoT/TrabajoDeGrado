#  Generación de oraciones

import random, math
import extractTagsWithAzure as cvazure

wordsSegmentation = []

# Almacenamiento de las etiquetas para evitar realizar llamados constantes al recurso de Computer Vision
def getTags(image_url):
    global wordsSegmentation
    wordsSegmentation = cvazure.tagImage(image_url)
    tags = ""
    tags = ', '.join(wordsSegmentation)
    return tags

# RETORNO de una muestra de una lista de palabras limpias de stopwords y singularizadas
def getCombinationOfWords(originalWords, listOfWords, numberOfWordsPerSample, numberOfSentences):
    import Soporte.F_cleaningOfListOfWords as cleaning
    import Soporte.G_affinityOfLists as aff
    sampleSelectedWords = list() # Lista de palabras que se van a usar para hacer oraciones
    listOfWords = cleaning.cleaning(listOfWords)
    while numberOfSentences > 0:
        auxSample = random.sample(originalWords, math.floor(1 + (numberOfWordsPerSample / 3))) + random.sample(listOfWords, math.floor(1 + (numberOfWordsPerSample / 2)))
        auxSample.sort()
        if auxSample not in sampleSelectedWords:
            if aff.getAffinity(auxSample) > 0:
                random.shuffle(auxSample)
                sampleSelectedWords.append(auxSample)
                numberOfSentences = numberOfSentences - 1
    return sampleSelectedWords

# GENERACIÓN de oraciones con una lista de palabras desorganizadas alfabéticamente
def getSentenceWithRandomOrder(words):
    from keytotext import pipeline
    nlp = pipeline("k2t-base")
    generatedSenteces = ""
    for i in words:
        generatedSenteces = generatedSenteces + "\n" + "[" + ', '.join(i) + "]"
        generatedSenteces = generatedSenteces + "\n" + nlp(i) + "\n"
        generatedSenteces = generatedSenteces + "----------------------------------------------------------------"
    return generatedSenteces

# GENERACIÓN de oraciones
def generarOraciones(wordsPerSentence, sentences):
    import gettingRelationsFromDB as getDB
    listOfWords = getDB.returnSelectedWords(wordsSegmentation) # Lista de palabras elegidas por heurística
    sampleSelectedWords = getCombinationOfWords(wordsSegmentation, listOfWords, wordsPerSentence, sentences) # Se eligen X oraciones de Y palabras cada una
    allSenteces = getSentenceWithRandomOrder(sampleSelectedWords)
    return allSenteces