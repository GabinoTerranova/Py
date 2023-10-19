'''Métodos de las listas

Las listas tienen una serie de métodos que se pueden usar para manipularlas. Algunos de los métodos más comunes son:

* append(): Agrega un elemento a la lista al final.
* clear(): Elimina todos los elementos de la lista.
* copy(): Devuelve una copia de la lista.
* count(): Cuenta el número de veces que aparece un elemento en la lista.
* extend(): Agrega los elementos de una lista a otra lista.
* index(): Devuelve el índice del primer elemento que coincide con un valor dado.
* insert(): Inserta un elemento en la lista en un índice dado.
* pop(): Elimina el elemento de la lista en un índice dado.
* remove(): Elimina el primer elemento que coincide con un valor dado.
* reverse(): Invierte el orden de los elementos de la lista.
* sort(): Ordena los elementos de la lista.

```
# Agregar un elemento al final de una lista
lista = ["a", "b", "c"]
lista.append("d")
print(lista)
# ["a", "b", "c", "d"]

# Eliminar el primer elemento de una lista
lista = ["a", "b", "c"]
lista.pop(0)
print(lista)
# ["b", "c"]

# Contar el número de veces que aparece un elemento en una lista
lista = ["a", "b", "c", "a", "b"]
print(lista.count("a"))
# 2

# Obtener el índice de un elemento en una lista
lista = ["a", "b", "c", "d"]
print(lista.index("c"))
# 2

# Insertar un elemento en una lista en un índice dado
lista = ["a", "b", "c"]
lista.insert(1, "x")
print(lista)
# ["a", "x", "b", "c"]

# Eliminar el primer elemento que coincide con un valor dado
lista = ["a", "b", "c", "d"]
lista.remove("a")
print(lista)
# ["b", "c", "d"]

# Invertir el orden de los elementos de una lista
lista = ["a", "b", "c", "d"]
lista.reverse()
print(lista)
# ["d", "c", "b", "a"]

# Ordenar los elementos de una lista
lista = ["c", "a", "b", "d"]
lista.sort()
print(lista)
# ["a", "b", c", "d"]
```


Métodos de los diccionarios

Los diccionarios tienen una serie de métodos que se pueden usar para manipularlos. Algunos de los métodos más comunes son:

* clear(): Elimina todos los elementos del diccionario.
* copy(): Devuelve una copia del diccionario.
* get(): Devuelve el valor asociado a una clave, o un valor por defecto si la clave no existe.
* items(): Devuelve una lista de pares (clave, valor).
* keys(): Devuelve una lista de claves.
* pop(): Elimina el elemento asociado a una clave, y devuelve el valor.
* update(): Agrega o actualiza los elementos de un diccionario.
* values(): Devuelve una lista de valores.

```
# Eliminar todos los elementos de un diccionario
diccionario = {"nombre": "Juan", "edad": 20}
diccionario.clear()
print(diccionario)
# {}

# Devolver una copia de un diccionario
diccionario = {"nombre": "Juan", "edad": 20}
copia = diccionario.copy()
print(copia)
# {"nombre": "Juan", "edad": 20}

# Devolver el valor asociado a una clave
diccionario = {"nombre": "Juan", "edad": 20}
valor = diccionario.get("nombre")
print(valor)
# Juan

# Devolver una lista de pares (clave, valor)
diccionario = {"nombre": "Juan", "edad": 20}
pares = diccionario.items()
print(pares)
# [("nombre", "Juan"), ("edad", 20)]

# Devolver una lista de claves
diccionario = {"nombre": "Juan", "edad": 20}
claves = diccionario.keys()
print(claves)
# ["nombre", "edad"]

# Eliminar el elemento asociado a una clave
diccionario = {"nombre": "Juan", "edad": 20}
valor = diccionario.pop("nombre")
print(valor)
# Juan
print(diccionario)
# {"edad": 20}

# Agregar o actualizar los elementos de un diccionario
diccionario = {"nombre": "Juan", "edad": 20}
diccionario.update({"pais": "Argentina"})
print(diccionario)
# {"nombre": "Juan", "edad": 20, "pais": "Argentina"}

# Devolver una lista de valores
diccionario = {"nombre": "Juan", "edad": 20}
valores = diccionario.values()
print(valores)
# [Juan, 20]
```
## Ejercicios
1. Crea un diccionario que contenga la información de una persona, como su nombre, edad, dirección y teléfono. Luego, utiliza los métodos get(), update() y pop() para modificar la información del diccionario.

2. Crea un diccionario que contenga el precio de una lista de productos. Luego, utiliza los métodos keys(), values() e items() para recorrer el diccionario y mostrar la información de cada producto.

3. Crea un diccionario que contenga la temperatura de una lista de ciudades. Luego calcule la media,max y minima de las temperaturas.

4. Crea un diccionario que contenga el nombre de un país y su capital. Luego, utiliza el método update() para agregar un nuevo elemento al diccionario.
5. Crea una lista que contenga una lista de números. Luego, utiliza el método count() para contar el número de veces que aparece un elemento en la lista.
6. Crea una lista que contenga una lista de números. Luego, utiliza el método index() para obtener el índice de un elemento en la lista.
## Algoritmo de ordenamiento
Buscar información'''