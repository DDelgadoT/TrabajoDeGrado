# Obtener un dataset que contenga un número definido de filas de un dataset más grande
# Solo es usada para dividir un dataset para ser subido por partes
import csv, math, random

# Creación de una porción de un dataset
def conseguirCantidadPalabras(datasetOriginal, datasetNuevo, cantidad):
    row_count = 0
    with open(datasetOriginal, encoding = 'cp850') as originalFile:
        readerHeader = csv.reader(originalFile)
        for row in readerHeader:
            fieldnames = row
            break
        row_count = sum(1 for _ in originalFile)
    
    probabilidad = math.ceil(row_count / cantidad) # Genera el número, que si se obtiene, acepta la fila y la agrega al nuevo .csv

    with open(datasetOriginal, encoding = 'cp850') as file:
        lineCount = 0
        wantedLines = 0
        readerCSV = csv.DictReader(file)
        csvWantedRelations = open(datasetNuevo, 'w', encoding = 'cp850', newline="")
        writer = csv.DictWriter(csvWantedRelations, fieldnames=fieldnames)
        writer.writeheader()
        for row in readerCSV:
            if random.randint(1, probabilidad) == probabilidad: # Uso de la variable "probabilidad" Nota: Se usa el último número para aceptar la fila
                wantedLines += 1
                writer.writerow(row)
            lineCount += 1
        csvWantedRelations.close()
    lineasProcesadas = "{:,}".format(lineCount)
    lineasLimpias = "{:,}".format(wantedLines)
    print(f"Cantidad de lineas procesadas: {lineasProcesadas}")
    print(f"Cantidad de lineas con las relaciones deseadas procesadas: {lineasLimpias}")
                
datasetOriginal = "../CSVs/3_WordsEnglishWantedRelations.csv"
datasetNuevo = "AmountOfWordsGiven.csv"
cantidadDePalabrasDeseadas = 25000
conseguirCantidadPalabras(datasetOriginal, datasetNuevo, cantidadDePalabrasDeseadas)