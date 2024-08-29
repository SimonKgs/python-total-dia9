import random
from collections import Counter, defaultdict, namedtuple

numeros = [random.randint(0, 10) for _ in range(100)]

print(numeros)

# Know of much times a number is in the array
# Counter creates a collection with each character and how many times it is repeated
print(Counter(numeros))
print(Counter('mississippi'))

counter_numeros = Counter(random.randint(0, 10) for _ in range(100))
# it also let me use some useful methods like
# Most common will show the most repeated numbers ordered if we pass a number will show the x most repeated
print(counter_numeros.most_common(1))
# Total will show the total of the elements that it counts
print(counter_numeros.total())
# keys will show the elements and values how many times an element is on the array
print(counter_numeros.keys())
print(max(counter_numeros.values()))



# DEFAULT DICT
mi_normal_dict = {'uno': 'verde', 'dos': 'azul', 'tres': 'rojo'}
print(mi_normal_dict['uno'])

# using default I can prevent key errors by answering with the default value
mi_default_dict = defaultdict(lambda: 'nada')
mi_default_dict['uno'] = 'Hola'
print(mi_default_dict['dos'])


# namedTupled
my_tuple = (500, 18, 65)
print(my_tuple[1])

# this will let me access to an element of an array by a number given
# this eg has the
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.66, 79)
print(ariel.nombre)
print(ariel[0])