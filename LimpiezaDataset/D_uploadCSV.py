# Subida de un csv a una base de datos

import csv, Soporte.D_ConnectDB as BD

# Creación de la conexión a la base de datos
connection = BD.conectarBD()

with open("csvs dividido/output_1.csv", encoding = 'cp850') as originalFile:
    csv_data = csv.DictReader(originalFile)
    with connection:
        with connection.cursor() as cursor:
            for row in csv_data:
                sql = "INSERT INTO `words_relations`(`Word1`, `Word2`, `Relationship`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (row['Word 1'], row['Word 2'], row['Relationship']))
                break
        connection.commit()