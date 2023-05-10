# Obtener las palabras que estén relacionadas con una lista de palabras
import Soporte.D_ConnectDB as connectDB

wordsRelated, wordsWithRelationships = list(), list()
# wordsRelated = (word, word, word, ...)
# wordsWithRelationships = ((word, word, relation),(word, word, relation),(word, word, relation),...)

# SETEO de lista donde se obtienen todas las posibles relaciones que existan con las palabras obtenidas de la segmentación
def getWords(wordsFromSeg):
    indexWord = 0
    connection = connectDB.conectarBD()
    with connection.cursor() as cursor:
        sql = "SELECT `Word 1`,`Word 2`,`Relationship` FROM `words_relations` WHERE `Word 1`=%s"
        for i in wordsFromSeg:
            cursor.execute(sql, i)
            for tuple in cursor:
                wordsRelated.append(tuple[1])
                wordsWithRelationships.append((tuple[1], tuple[2], indexWord))
            indexWord += 1
        #print(type(result)) RESULT = TUPLA

# SETEO de una lista donde se cuentan la cantidad de veces que una palabra relacionada aparezca
def contadorRelaciones():
    global relationCounter
    relationCounter = dict()
    for word in wordsRelated:
        if word in relationCounter:
            relationCounter[word] += 1
        else:
            relationCounter[word] = 1

# SOPORTE
# RETORNO un diccionario ordenado por los valores
def sortCounter(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

# RETORNO de un diccionario donde aparece el porcentaje que una palabra relacionada aparezca con una relación de "RelatedTo"
# Aunque se obtienen las tuplas con cualquier relación, no se puede omitir las otras relaciones porque siguen siendo importantes
def getWordsFromTuplesWithWantedRelation(dictionary, relation):
    listOfWords = list(dictionary.keys())
    listWithWordsAndPercentajes = dict()
    countOfWord, countOfRelation = 0, 0
    for word in listOfWords:
        for item in wordsWithRelationships:
            if item[0] == word:
                countOfWord += 1
                if item[1] in relation:
                    countOfRelation += 1
        listWithWordsAndPercentajes[word] = round(countOfRelation/countOfWord, 3)
        countOfWord, countOfRelation = 0, 0
    return sortCounter(listWithWordsAndPercentajes)

# RETORNO de una lista de palabras que tengan un porcentaje de aparición con la relación "RelatedTo"
def getWordsWithCount(dictionary, number):
    wordsAppearMore = list()
    for word, count in dictionary.items():
        if count >= number:
            wordsAppearMore.append(word)
    return wordsAppearMore

# SOPORTE
# IMPRESIÓN de todas las tuplas donde una palabra deseada aparezca
def searchForTupleWithWord(listOfTuples, word):
    print("----------------------------------------------------------------")
    print(f"Tuplas que tengan la palabra \"{word}\"")
    for tuple in listOfTuples:
        if tuple[0] == word:
            print(tuple)

# RETORNO de una lista de palabras relacionadas que tengan una probabilidad mayor de aparición con relación de "RelatedTo" a un umbral deseado
def returnSelectedWords(segmentacionImagenes):
    getWords(segmentacionImagenes)
    contadorRelaciones()
    return getWordsWithCount(getWordsFromTuplesWithWantedRelation(relationCounter, ["RelatedTo"]), 0.75)