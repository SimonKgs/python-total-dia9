# expresiones regulares     ejemplos
# \d digito numerico        v\d.\d\d        -> v2.00
# \w caracter alfanumerico  \w\w\w-\w\w     -> sol-do | Abc-23
# \s espacio en blanco      numero\s\d\d    -> numero 12

# mayus indica lo contrario
# \D No numerico            \D\D\D\D        -> asCs | XXXX
# \W No alfanumerico        \W\W\W          -> +=- | ???
# \S No espacio blanco      \S\S\S          -> abcD | 1234

# cuantificadores
# + una o más veces         codigo_\d-\d+   -> codigo_5-5 | codigo_5-23425
# {n} se repite n veces     num-\d{3}       -> num-333  | num-555
# {n, m} entre n a m veces  \d{2, 5}        -> 12   | 123   | 12345
# {n, } desde sin limite    -\w{3, }-       -> -asw-    | -aweqrfasdasz-
# * 0 o mas veces           \w\s*\w         -> h h  | J     J
# ? 1 o 0 veces             casas*          -> puede ser singular sin la s o plural

import re

regular_expresion = r'\d\d\d-\d{3}'

texto = 'este es un texto corto para comprender el funcionamiento de las expresiones regulares '
palabra = 'comprender' in texto

print(palabra)

patron = r'\w\w\w\s\w{3}'
busqueda = re.search(patron, texto)
buscaTodas = re.findall(patron, texto)
print(busqueda)
print(buscaTodas)

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())


texto_nuevo = "llama al 545-123-5664 ya mismo"
patron = r'\d{3}-\d{3}-\d{4}'

busca_numero = re.findall(patron, texto_nuevo)
print(busca_numero)

# podemos compilar la cadena
# con ello podremos hacer busquedas por grupos
patron_dos = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
busca_numero_compilado = re.search(patron_dos, texto_nuevo)
print(busca_numero_compilado.group(2))


# podemos utilizarlos para claves
# clave = input("Clave: \n")
patron_clave = r'\D{1}\w{7}'
# chequear = re.search(patron_clave, clave)
# print(chequear)

texto_condicional = "No atendemos los martes por la tarde"
buscar_condicion = re.search(r'lunes|martes', texto_condicional)

buscar_comodin = re.search(r'...demos..', texto_condicional)
print(buscar_comodin)

# patron al comienzo, que no sea un digito
buscar_patron_comienzo = re.search(r'^\D', texto_condicional)
print(buscar_patron_comienzo)

buscar_patron_final = re.search(r'\D$', texto_condicional)
print(buscar_patron_final)

# excluir, en este caso excluimos todos los espacios, con el mas en lugar de caracteres tenemos las palabras en la lista
# aclarando, devolverá todos los caracteres en una lista excepto los espacios,
# los agrupara por cada espacio que encuentre, formando palabras completas
excluir_patron = re.findall(r'[^\s]+', texto_condicional)
print(excluir_patron)