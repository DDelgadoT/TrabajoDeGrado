# Crea la conexión para la base de datos

import pymysql.cursors

# Retorna la conexión para la base de datos
def conectarBD():
    connection = pymysql.connect(host='localhost',
                user='root',
                password='admin1234',
                database='trabajo_grado')
    return connection