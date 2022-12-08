# Conseguir las relaciones
import csv
def conseguirTipoRelaciones(dataset):
    with open(dataset, encoding = 'cp850') as file:
        readerCSV = csv.DictReader(file)
        relaciones = list()
        for row in readerCSV:
            if not(any(elem in row['Relationship'] for elem in relaciones)):
                relaciones.append(row['Relationship'])
        print(relaciones)
dataset = "WordsEnglishOnlyClean.csv"
conseguirTipoRelaciones(dataset)