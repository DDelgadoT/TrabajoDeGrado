# Estandarización de una lista de palabras
import nltk.stem as stem

# INSTALACION PAQUETES
#nltk.download('omw-1.4')
#nltk.download("stopwords")

# SOPORTE
# RETORNO de la limpieza de stopwords
def cleanListOfWordsFromStepWords(listaPalabras):
    from nltk.corpus import stopwords
    step_words_en = stopwords.words("english")
    for i in listaPalabras:
        if i in step_words_en:
            listaPalabras.remove(i)
    return listaPalabras

# SOPORTE
# RETORNO de la singularización de todas las palabras de una lista
def singularizeList(listaPalabras):
    singularize = stem.WordNetLemmatizer()
    listaPalabras = [singularize.lemmatize(word) for word in listaPalabras]
    return listaPalabras

def cleaning(lista):
    return singularizeList(cleanListOfWordsFromStepWords(lista))