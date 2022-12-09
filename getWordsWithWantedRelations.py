# Conseguir palabras que solo tengan las relaciones que se desean

import csv, time, datetime

#tiempoInicio = time.time()

# Crea un nuevo .csv donde solo se encuentren las relaciones que se deseen
def conseguirPalabrasRelaciones(datasetOriginal, datasetNuevo, relations):
    # Se obtienen la cabecera
    with open(datasetOriginal, encoding = 'cp850') as originalFile:
        readerHeader = csv.reader(originalFile)
        for row in readerHeader:
            fieldnames = row
            break

    with open(datasetOriginal, encoding = 'cp850') as file:
        # Parametros de evaluación
        lineCount = 0
        wantedLines = 0

        # Se abre el archivo a escribir
        csvWantedRelations = open(datasetNuevo, 'w', encoding = 'cp850', newline="")
        writer = csv.DictWriter(csvWantedRelations, fieldnames=fieldnames)
        writer.writeheader()

        # Lector para el archivo original
        readerCSV = csv.DictReader(file)

        # Se itera en cada línea que tenga el archivo original
        for row in readerCSV:
            if any(elem in row['Relationship'] for elem in relations):
                wantedLines += 1
                writer.writerow(row)
            lineCount += 1
        
        # Se cierra el archivo a escribir
        csvWantedRelations.close()
    
    # Impresiones de métricas
    # Cantidad de lineas
    lineasProcesadas = "{:,}".format(lineCount)
    lineasLimpias = "{:,}".format(wantedLines)
    print(f"Cantidad de lineas procesadas: {lineasProcesadas}")
    print(f"Cantidad de lineas con las relaciones deseadas procesadas: {lineasLimpias}")
                
datasetOriginal = "CSVs/WordsEnglishOnlyClean.csv"
datasetNuevo = "CSVs/WordsEnglishWantedRelations.csv"
relations = ("Antonym", "FormA", "HasContext", "IsA", "MadeOf", "PartOf", "RelatedTo", "SimilarTo", "SymbolOf", "Synonym", "UsedFor") # Relaciones deseadas
conseguirPalabrasRelaciones(datasetOriginal, datasetNuevo, relations)

# ------------- METRICAS ------------- 
"""
tiempoEjecuccion = time.time() - tiempoInicio
print()
print()
print(f"Tiempo de procesamiento: {str(datetime.timedelta(seconds=tiempoEjecuccion))}")
"""