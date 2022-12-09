# Limpieza de un conjunto de palabras

import nltk
from nltk.stem import WordNetLemmatizer

#nltk.download('omw-1.4')
#nltk.download("stopwords")

# Limpieza de stopwords
def cleanListOfWordsFromStepWords(listaPalabras):
    from nltk.corpus import stopwords
    step_words_en = stopwords.words("english")
    for i in listaPalabras:
        if i in step_words_en:
            listaPalabras.remove(i)
    return listaPalabras

# Singulariza todas las palabras de una lista
def singularizeList(listaPalabras):
    singularize = WordNetLemmatizer()
    listaPalabras = [singularize.lemmatize(word) for word in listaPalabras]
    return listaPalabras

def cleaning(lista):
    return singularizeList(cleanListOfWordsFromStepWords(lista))