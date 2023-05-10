# Retorno de un .csv sin caracteres especiales como el "@"
import csv, time, datetime

# Creación de un nuevo .csv donde ninguna de las dos palabras contenga caracteres especiales
def limpiezaDeCaracteres(datasetOriginal, datasetNuevo, chars):
    # Se obtienen la cabecera
    with open(datasetOriginal, encoding = 'cp850') as originalFile:
        readerHeader = csv.reader(originalFile)
        for row in readerHeader:
            fieldnames = row
            break

    with open(datasetOriginal, encoding = 'cp850') as originalFile:
        # Parametros de evaluación
        lineCount = 0
        wantedLines = 0

        # Se abre el archivo a escribir
        csv_english = open(datasetNuevo, 'w', encoding = 'cp850', newline="")
        writer = csv.DictWriter(csv_english, fieldnames=fieldnames)
        writer.writeheader()

        # Lector para el archivo original
        readerCSV = csv.DictReader(originalFile)

        # Se itera en cada línea que tenga el archivo original
        for row in readerCSV:
            if not(any(elem in row['Word 1'] for elem in chars)) and not(any(elem in row['Word 2'] for elem in chars)):
                wantedLines += 1
                writer.writerow(row)
            lineCount += 1

        # Se cierra el archivo a escribir
        csv_english.close()

    # Impresiones de métricas
    # Cantidad de lineas
    lineasProcesadas = "{:,}".format(lineCount)
    lineasLimpias = "{:,}".format(wantedLines)
    print(f"Cantidad de lineas procesadas: {lineasProcesadas}")
    print(f"Cantidad de lineas limpias sin {chars} procesadas: {lineasLimpias}")

datasetOriginal = "-----/WordsEnglishOnly.csv"
datasetNuevo = "-----/WordsEnglishOnlyClean.csv"
chars = frozenset(r'_.@')
limpiezaDeCaracteres(datasetOriginal, datasetNuevo, chars)