# Funciones en python
'''
En programación, una subproceso es un bloque de código que se puede reutilizar en diferentes partes de un programa.
Los subprocesos se utilizan para dividir un programa en tareas más pequeñas y manejables, lo que hace que el código
sea más fácil de entender, depurar y mantener.

def nombre_funcion():
    acciones
'''

# Funciones con retorno y sin retorno

## Funciones sin retorno
'''
Las funciones sin retorno son funciones que no devuelven ningún valor. Las funciones sin retorno se utilizan para
realizar tareas que no requieren la devolución de un valor
'''

def saludo():
    print("Hola")

## Funciones con retorno
'''
Las funciones con retorno son funciones que devuelven un valor. El valor de retorno se puede utilizar por la función que
llamó a la función para obtener los resultados de la función.
'''

def suma():
    return 1+2 

'''NOTA: Noten que esto solo es la definición de las funciones, luego hay que llamarlas para que funcionen.'''

## Funciones con parametros

'''
Las funciones en python pueden tomar parametros
'''

def saludo(nombre):
    print(f"Hola + {nombre}")

## Parametros default

'''
Tambien puede tomar valores por default estos parametros. Entonces si yo corro esto
'''

def fav_lenguaje(lenguaje="Python"):
    print(f"Mi lenguaje favorito de programación es {lenguaje}!")
fav_lenguaje()

'''
Me devolvera "Mi lenguaje favorito de programación es Python" En cambio si lo llamo con un argumento la salida seria
otra. Me devolvera "Mi lenguaje favorito de programación es C++"
'''

## Mas de un parametro

def saludo(primer_nombre,apellido):
    print(f"Hola, {primer_nombre} {apellido}")
saludo("Juan","Perez") 

'''
NOTA: Tener en cuenta que el orden de los argumentos es vital para python, salvo que definamos los argumentos
manualmente en vez de orden.
'''

### Esta salida va a ser diferente a la anterior
saludo("Perez","Juan")
### Mientras que esta no
saludo(apellido="Perez",nombre="Juan")

## Funciones lambda o Funciones anonimas

'''
Las funciones lambda o anonimas de python son funciones que solo existen en una linea de codigo. Estas son muy
utiles cuando queremos aplicar una función relativamente sencilla una sola vez y luego no usarla más.
'''

mi_lista = [1, 2, 3, 4, 5, 6]
lista_nueva = list(map(lambda x: x * 2, mi_lista))
print(lista_nueva) # [2, 4, 6, 8, 10, 12]

'''
Nota: Este tipo de codigo no solo es mas "elegante" sino que ademas es un poco mas eficiente. De todos modos para el
proposito de este curso es mas que suficiente que usen solo los funciones tradicionales. Pero es bueno que sepan que
existe
'''
