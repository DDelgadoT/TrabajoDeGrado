import Soporte.D_ConnectDB as D, time, datetime

tiempoInicio = time.time()

def getWords(query, word):
    connection = D.conectarBD()
    with connection.cursor() as cursor:
        cursor.execute(query, word)
        result = cursor.fetchall()
        print(result)

def getRelationFrom2Words(words):
    connection = D.conectarBD()
    with connection.cursor() as cursor:
        query = "SELECT `Relationship` FROM `words_relations` WHERE `Word 1`=%s AND `Word 2`=%s"
        cursor.execute(query, words)
        result = cursor.fetchall()
        return result

palabra = ("house", "dog")
query1Word = "SELECT `Word 1`,`Word 2`,`Relationship` FROM `words_relations` WHERE `Word 1`=%s"
query2Word = "SELECT `Word 1`,`Word 2`,`Relationship` FROM `words_relations` WHERE `Word 1`=%s AND `Word 2`=%s"
getWords(query2Word, palabra)