# Subida de un csv a una base de datos

import csv, pymysql.cursors, time, datetime, Soporte.D_ConnectDB as BD

#tiempoInicio = time.time()

# Creación de la conexión a la base de datos
connection = BD.conectarBD()

with open("3_WordsEnglishWantedRelations.csv", encoding = 'cp850') as originalFile:
    csv_data = csv.DictReader(originalFile)
    with connection:
        with connection.cursor() as cursor:
            for row in csv_data:
                sql = "INSERT INTO `words_relations`(`Word 1`, `Word 2`, `Relationship`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (row['Word 1'], row['Word 2'], row['Relationship']))
        connection.commit()

# ------------- METRICAS -------------
"""
tiempoEjecuccion = time.time() - tiempoInicio
print()
print()
print(f"Tiempo de procesamiento: {str(datetime.timedelta(seconds=tiempoEjecuccion))}")
"""