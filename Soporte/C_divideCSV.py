# Divide un .csv en varios de tamaños más pequeños
# NOTA IMPORTANTE: ESTE CÓDIGO NO FUE HECHO POR MI. CREDITOS A Jordi Rivero (https://gist.github.com/jrivero)
# LINK DEL REPOSITORIO: https://gist.github.com/jrivero/1085501
import os, time, datetime

def split(filehandler, delimiter=',', row_limit=55000, 
    output_name_template='output_%s.csv', output_path='./csvs dividido/', keep_headers=False):
    """
    Splits a CSV file into multiple pieces.
    
    A quick bastardization of the Python CSV library.
    Arguments:
        `row_limit`: The number of rows you want in each output file. 10,000 by default.
        `output_name_template`: A %s-style template for the numbered output files.
        `output_path`: Where to stick the output files.
        `keep_headers`: Whether or not to print the headers in each output file.;
    """
    import csv
    tiempoInicio = time.time()
    reader = csv.reader(filehandler, delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(
         output_path,
         output_name_template  % current_piece
    )
    current_out_writer = csv.writer(open(current_out_path, 'w', encoding = 'cp850', newline=""), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = reader.next()
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
               output_path,
               output_name_template  % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w', encoding = 'cp850', newline=""), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)
    tiempoEjecuccion = time.time() - tiempoInicio
    print(f"Tiempo de procesamiento: {str(datetime.timedelta(seconds=tiempoEjecuccion))}")

dataset = "WordsEnglishWantedRelations.csv"
split(open(dataset, 'r', encoding = 'cp850'))