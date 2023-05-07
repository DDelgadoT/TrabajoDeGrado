# Creación de la conexión para la base de datos y diversas funciones para verificaciones
import pymysql.cursors

# RETORNO la conexión para la base de datos local
def conectarBD():
    connection = pymysql.connect(host='localhost',
                user='root',
                password='admin1234',
                database='trabajo_grado')
    return connection

# Retorna la conexión para la base de datos remota
"""def conectarBD():
    connection = pymysql.connect(host='trabajogradounivalle.cnci5bmkxmhz.us-east-1.rds.amazonaws.com',
                user='admin',
                password='admin1234',
                database="words_relations")
    return connection"""
# SOPORTE
# Creación base de datos
def crearBD():
    connection = conectarBD()
    cursor = connection.cursor()
    sql = '''create database words_relations'''
    cursor.execute(sql)
    cursor.connection.commit()

# SOPORTE
# Creación de una tabla en la BD
def createTable():
    connection = conectarBD()
    cursor = connection.cursor()
    sql = '''
    create table words_relations ( id int NOT NULL AUTO_INCREMENT, Word1 varchar(255), Word2 varchar(255), Relationship varchar(255), PRIMARY KEY (id))'''
    print("Table created")
    print("Model: id int NOT NULL AUTO_INCREMENT, Word1 varchar(255), Word2 varchar(255), Relationship varchar(255), PRIMARY KEY (id))")
    cursor.execute(sql)

# SOPORTE
# Verificar las tablas en la BD
def checkTables():
    connection = conectarBD()
    cursor = connection.cursor()
    sql = '''show tables'''
    cursor.execute(sql)
    print("Tables:")
    print(cursor.fetchall())

# SOPORTE
# Revisar contenidos de una tabla
def checkContentTable():
    connection = conectarBD()
    cursor = connection.cursor()
    sql = "SELECT * FROM words_relations LIMIT 25"
    cursor.execute(sql)
    for i in range(0, 25):
        print(cursor.fetchone())

# SOPORTE
# Eliminar el contenido de una tabla
def deleteContentTable():
    connection = conectarBD()
    cursor = connection.cursor()
    sql = "DELETE FROM words_relations"
    cursor.execute(sql)
    connection.commit()
    print(cursor.fetchall())