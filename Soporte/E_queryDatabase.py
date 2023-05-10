# Consultas a base de datos
# Solo usada para realizar pruebas en la base de datos
import Soporte.D_ConnectDB as db

# RETORNO de los resultados de una consulta personalizada
def getWords(query, word):
    connection = db.conectarBD()
    with connection.cursor() as cursor:
        cursor.execute(query, word)
        result = cursor.fetchall()
        return result

# RETORNO de las relaciones que dos palabras puedan tener (Pueden ser una o varias)
def getRelationFrom2Words(words):
    connection = db.conectarBD()
    with connection.cursor() as cursor:
        query = "SELECT `Relationship` FROM `words_relations` WHERE `Word 1`=%s AND `Word 2`=%s"
        cursor.execute(query, words)
        result = cursor.fetchall()
        return result

"""palabra = ("train", "transport")
query1Word = "SELECT `Word 1`,`Word 2`,`Relationship` FROM `words_relations` WHERE `Word 1`=%s"
query2Word = "SELECT `Word 1`,`Word 2`,`Relationship` FROM `words_relations` WHERE `Word 1`=%s AND `Word 2`=%s"
print(getRelationFrom2Words(palabra))"""