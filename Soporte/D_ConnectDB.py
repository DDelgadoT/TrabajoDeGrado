# Creación de la conexión para la base de datos y diversas funciones más para verificaciones

import pymysql.cursors

# Retorna la conexión para la base de datos
def conectarBD():
    connection = pymysql.connect(host='localhost',
                user='root',
                password='admin1234',
                database='trabajo_grado')
    return connection

"""def conectarBD():
    connection = pymysql.connect(host='trabajogradounivalle.cnci5bmkxmhz.us-east-1.rds.amazonaws.com',
                user='admin',
                password='admin1234',
                database="words_relations")
    return connection"""

def crearBD():
    connection = conectarBD()
    cursor = connection.cursor()
    sql = '''create database words_relations'''
    cursor.execute(sql)
    cursor.connection.commit()

def createTable():
    connection = conectarBD()
    cursor = connection.cursor()
    sql = '''
    create table words_relations ( id int NOT NULL AUTO_INCREMENT, Word1 varchar(255), Word2 varchar(255), Relationship varchar(255), PRIMARY KEY (id))'''
    print("Table created")
    print("Model: id int NOT NULL AUTO_INCREMENT, Word1 varchar(255), Word2 varchar(255), Relationship varchar(255), PRIMARY KEY (id))")
    cursor.execute(sql)

def checkTables():
    connection = conectarBD()
    cursor = connection.cursor()
    sql = '''show tables'''
    cursor.execute(sql)
    print("Tables:")
    print(cursor.fetchall())

def checkContentTable():
    connection = conectarBD()
    cursor = connection.cursor()
    sql = "SELECT * FROM words_relations LIMIT 25"
    cursor.execute(sql)
    for i in range(0, 25):
        print(cursor.fetchone())
    
def deleteContentTable():
    connection = conectarBD()
    cursor = connection.cursor()
    sql = "DELETE FROM words_relations"
    cursor.execute(sql)
    connection.commit()
    print(cursor.fetchall())