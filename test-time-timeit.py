# import time
import timeit

def test_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista



def test_while(numero):
    lista = []
    contador = 1

    while contador <= numero:
        lista.append(contador)
        contador += 1

    return lista


# inicio = time.time()
# test_while(1500000)
# fin = time.time()
# print(f'while time: {fin - inicio}')

# inicio = time.time()
# test_for(1500000)
# fin = time.time()
# print(f'For time: {fin - inicio}')


declaracion = '''
test_for(10)
'''

mi_setup = '''
def test_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

duracion = timeit.timeit(declaracion, setup=mi_setup, number=100000)
print(duracion)