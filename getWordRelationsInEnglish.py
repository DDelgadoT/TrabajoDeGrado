# Retorno de un .csv en el idioma que se desee

import csv, time, datetime

#tiempoInicio = time.time()

# Crea un nuevo .csv donde las filas sean del mismo idioma
def obtenerIdioma(datasetOriginal, datasetNuevo, language):
    # Se obtienen la cabecera
    with open(datasetOriginal, encoding = 'cp850') as originalFile:
        readerHeader = csv.reader(originalFile)
        for row in readerHeader:
            fieldnames = row
            break

    fieldnames.pop(0)
    fieldnames.remove('Language 1')
    fieldnames.remove('Language 2')
    
    with open(datasetOriginal, encoding = 'cp850') as originalFile:
        # Parametros de evaluación
        lineCount = 0
        languageLines = 0

        # Se abre el archivo a escribir
        csv_english = open(datasetNuevo, 'w', encoding = 'cp850', newline="")
        writer = csv.DictWriter(csv_english, fieldnames=fieldnames)
        writer.writeheader()

        # Lector para el archivo original
        readerCSV = csv.DictReader(originalFile)

        # Se itera en cada línea que tenga el archivo original
        for row in readerCSV:
            if row['Language 1'] == language and row['Language 2'] == language:
                languageLines += 1
                row.pop('')
                row.pop('Language 1')
                row.pop('Language 2')
                writer.writerow(row)
            lineCount += 1

        # Se cierra el archivo a escribir
        csv_english.close()

    # Impresiones de métricas
    # Cantidad de lineas
    lineasProcesadas = "{:,}".format(lineCount)
    lineasIdioma = "{:,}".format(languageLines)
    print(f"Cantidad de lineas procesadas: {lineasProcesadas}")
    print(f"Cantidad de lineas {language} a {language} procesadas: {lineasIdioma}")

datasetOriginal = "CSVs/WordRelationshipsInConceptNet.csv"
datasetNuevo = "CSVs/WordsEnglishOnly.csv"
language = "English"
obtenerIdioma(datasetOriginal, datasetNuevo, language)

# ------------- METRICAS ------------- 
"""
tiempoEjecuccion = time.time() - tiempoInicio
print()
print()
print(f"Tiempo de procesamiento: {str(datetime.timedelta(seconds=tiempoEjecuccion))}")
"""