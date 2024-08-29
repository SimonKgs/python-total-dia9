import zipfile

# selecting the mode and the action, write
# my_zip = zipfile.ZipFile('cv_comprimido.zip', 'w')

# adding files/folders to it
# my_zip.write('cv.pdf')
# my_zip.write('cvs.pdf')

# my_zip.close()

# descomprimir
# my_zip = zipfile.ZipFile('mat.zip', 'r')
# my_zip.extractall()

import shutil

# carpeta_origen = 'C:\\Users\\simon\\PycharmProjects\\python-total\\dia-9-buscador-num-serie\\Materiales'
# archivo_destino = 'Materiales_recomprimidos'
# comprimir shutil
# shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

# descomprimir shutil
shutil.unpack_archive('Materiales_recomprimidos.zip', 'Mat Reextraidos', 'zip')
