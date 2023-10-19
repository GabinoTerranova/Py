'''
Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su
código, se utiliza para desarrollar aplicaciones de todo tipo, por ejemplo: Instagram, Netflix, Spotify. Es orientado a
objetos por tanto todas las variables que veamos en el codigo son objetos y por tanto tienen atributos y metodos.

Python es un lenguaje orientado a objetos
'''

#TIPOS DE DATOS

# Int / Interger
'''
Estos tipos de variables en Python corresponden a los números enteros. Dentro de este tipo de datos existen
subdivisiones. Veamos cada una de ellas en Python
'''

edad=23
print(edad) 

'''
NOTA: Si queremos ver el tipo de dato de nuestra variable podemos usar:
print(type(edad))
'''

# Float
'''
Los números de coma flotante, float o simplemente decimales son números que tienen residuos. Veamos cómo
funcionan estos tipos de variables en Python:
'''
float_test = 1.1 

# Boolean
'''
Los tipos de variables en Python que son boolean pueden tener dos valores: true o false.
'''
type(True)

# String
'''
Estos tipos de variables en Python básicamente son una secuencia inmmutable de caracteres:
'''
txt_1 = 'Soy Amanda'
print (txt_1)

#Listas
'''
Las listas de Python son tipos de contenedores de datos que son mutables y dinámicos, por lo que se pueden añadir y
eliminar elementos de una lista en su lugar, sin tener que crear una copia.
- Indexar en la lista y acceder a un elemento en un índice específico es una operación en tiempo constante.
- Añadir un elemento al final de la lista es una operación de tiempo constante.
- Insertar un elemento en un índice específico es una operación de tiempo lineal.
'''
nombres = ["mariano","colon","lujan","Gabino","Mateo","Santiago"]
numeros = [1,2,3,4,5,6]

for nombre in range(0,len(nombres),2): #recorrer una lista de 2 en 2
    print(nombres[nombre])

for numero in numeros:
    print(numero)

# Tuples
'''
Las tuplas son otra popular estructura de datos incorporada. Son como las listas de Python en el sentido de que puede
indexarlas en tiempo constante y trocearlas. Pero son inmutables, por lo que no puede modificarlas in situ. NOTA: Esto
puede cambiar en las nuevas versiones de python pero tratemos de mantener esa idea en la cabeza como diferencia
clave
'''
num = (1,2,3,4,5)

print(type(num))

# Dictionaries
'''
Un diccionario Python es funcionalmente similar a un mapa hash. Los diccionarios se utilizan para almacenar pares
clave-valor. Las claves del diccionario pueden ser del tipo de dato que yo quiera, yo les recomiendo que sean strings o
int. Los valores no tienen restriccion.
'''
users = {

    "gterranova": "123456",
    "nconil": "contraseña123",
    "mluongo": "contraseña456",

}

print(users["gterranova"])

# Sets
'''
Un set en Python es una colección de elementos únicos que no están ordenados. Esto significa que los elementos de un
set no se pueden repetir y que no tienen un orden específico.

Los sets se pueden usar para varios propósitos, como:
- Almacenar una colección de elementos únicos. Por ejemplo, un set se puede usar para almacenar los nombres
de los usuarios de un sitio web.
- Eliminar elementos duplicados de una lista. Por ejemplo, se puede usar un set para eliminar los elementos
duplicados de una lista de números.
- Realizar operaciones matemáticas con conjuntos. Por ejemplo, se puede usar un set para calcular la intersección
o la unión de dos conjuntos.
'''

set_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Realizar operaciones matemáticas con conjuntos

set_1 = {1, 2, 3}
set_2 = {2, 3, 4}

# Intersección
set_interseccion = set_1 & set_2
print(set_interseccion)