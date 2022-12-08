# Conseguir palabras que solo tengan las relaciones que se desean
import csv, time, datetime, math, random
def conseguirCantidadPalabras(datasetOriginal, datasetNuevo, cantidad):
    row_count = 0
    with open(datasetOriginal, encoding = 'cp850') as originalFile:
        readerHeader = csv.reader(originalFile)
        for row in readerHeader:
            fieldnames = row
            break
        row_count = sum(1 for _ in originalFile)
    
    probabilidad = math.ceil(row_count / cantidad)

    with open(datasetOriginal, encoding = 'cp850') as file:
        tiempoInicio = time.time()
        lineCount = 0
        wantedLines = 0
        readerCSV = csv.DictReader(file)
        csvWantedRelations = open(datasetNuevo, 'w', encoding = 'cp850', newline="")
        writer = csv.DictWriter(csvWantedRelations, fieldnames=fieldnames)
        writer.writeheader()
        for row in readerCSV:
            if random.randint(1,probabilidad) == 11:
                wantedLines += 1
                writer.writerow(row)
            lineCount += 1
        csvWantedRelations.close()
    lineasProcesadas = "{:,}".format(lineCount)
    lineasLimpias = "{:,}".format(wantedLines)
    print(f"Cantidad de lineas procesadas: {lineasProcesadas}")
    print(f"Cantidad de lineas con las relaciones deseadas procesadas: {lineasLimpias}")
    tiempoEjecuccion = time.time() - tiempoInicio
    print(f"Tiempo de procesamiento: {str(datetime.timedelta(seconds=tiempoEjecuccion))}")
                
datasetOriginal = "WordsEnglishWantedRelations.csv"
datasetNuevo = "AmountOfWordsGiven.csv"
cantidadDePalabrasDeseadas = 25000
conseguirCantidadPalabras(datasetOriginal, datasetNuevo, cantidadDePalabrasDeseadas)