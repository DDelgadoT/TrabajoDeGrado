# Obtener las posibles relaciones que hay entre las palabras
import csv

# Retorna todos los valores posibles en la columna "Relationship" del dataset
def conseguirTipoRelaciones(dataset):
    with open(dataset, encoding = 'cp850') as file:
        readerCSV = csv.DictReader(file)
        relaciones = list()
        for row in readerCSV:
            if not(any(elem in row['Relationship'] for elem in relaciones)):
                relaciones.append(row['Relationship'])
        print(relaciones)

dataset = "-----/WordsEnglishOnlyClean.csv"
conseguirTipoRelaciones(dataset)