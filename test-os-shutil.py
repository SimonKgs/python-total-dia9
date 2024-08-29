import os
import shutil

import send2trash

print(os.getcwd())

# with open('curso.txt', 'w') as cursotxt:
#    cursotxt.write('texto de prueba')


# print(os.listdir())

# shutil.move('curso.txt', "C:\\Users\\simon\\desktop")
# send2trash.send2trash('C:\\Users\\simon\\desktop\\curso.txt')


# print(os.walk('C:\\Users\\simon\\PycharmProjects\\python-total'))

ruta = 'C:\\Users\\simon\\PycharmProjects\\python-total'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'Carpeta: {carpeta}')
    print(f'las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')

    print('Los archivos son:')
    for arch in archivo:
        if arch.startswith('2015'):
            print('This will print only the files which starts with that string')
        if arch.endswith('.txt'):
            print('This will print only .txt files')
            print(f'text file: {arch} \n')
        # print(f'\t {arch}')
    print('\n')
