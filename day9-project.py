# import shutil
# Getting the instructions
# shutil.unpack_archive('Proyecto+Dia+9.zip', 'day9-exercise', 'zip')

# A los fines de este ejercicio, estas son las condiciones de formato que deben cumplir los hallazgos:
# - [N] + [tres carateres de texto] + [-] + [5 números]

# Por ejemplo: Nryu-12365

# La presentación en pantalla de los hallazgos debe ser un listado en formato de tabla, que respete el
# siguiente formato de ejemplo:

# ----------------------------------------------------
# Fecha de búsqueda: [fecha de hoy]

# ARCHIVO		NRO. SERIE
# -------		----------
# texto1.txt	Nter-15496
# texto25.txt	Ngba-85235

# Números encontrados: 2
# Duración de la búsqueda: 1 segundos
# ----------------------------------------------------

import re
import os
import time
import math

from datetime import datetime, date

# create and match the pattern
pattern = r'N\w{3}-\d{5}'

# read the tree structure
current_path = ('C:\\Users\\simon\\PycharmProjects\\python-total\\dia-9-buscador-num-serie\\day9-exercise'
                '\\Mi_Gran_Directorio')

search_results = []

for carpeta, subcarpeta, archivo in os.walk(current_path):
    for arch in archivo:
        if arch.endswith('.txt'):
            file_path = os.path.join(carpeta, arch)
            with open(file_path, 'r') as current_file:
                current_text = current_file.read()
                search = re.search(pattern, current_text)
                if search:
                    search_results.append({'file': arch, 'code': search.group()})


print('Fecha de búsqueda:', date.today())
print('ARCHIVO		NRO. SERIE:')
print('-------		-----------')

startTime = time.time()

for result in search_results:
    print(result['file'], result['code'])

endTime = time.time()

print('-----------------------')
print('Archivos encontrados:', len(search_results))
print(f'Duracion de la busqueda: {math.ceil(endTime - startTime)}')
