import pymysql.cursors

def conectarBD():
    connection = pymysql.connect(host='localhost',
                user='root',
                password='admin1234',
                database='trabajo_grado')
    return connection