[[Lenguajes MOC]]
# Argumentos de Palabras Clave

**Tags**:: #lenguajes/python/funciones 
**Links**:: [[Python]], [[Funciones]], [[print()]]

Python ofrece una forma de pasar argumentos. Este mecanismo se conoce como argumentos de palabras clave (*keyword arguments*). El nombre viene del hecho de que el significado de estos argumentos no vienen de su posición, sino de la palabra especial (*keyword*) usada para identificarlos.

### End
La función `print()` tiene dos argumentos *keyword*. La primera se llama `end`.

```python
print("Me llamo", "Emilio.", end=" ")
print("Mucho gusto.")
```

Imprime

```
Me llamo Emilio. Mucho gusto.
```

Para poder usar estos argumentos hay que tener en cuenta dos aspectos importantes:
1. Un argumento keyword consiste de tres partes: la palabra clave (*keyword*) que identifica el argumento (`end` en este caso); un *signo igual* ` =`; y el *valor* que se le asignará al argumento.
2.  Cualesquiera argumentos keyword deben ir después del último argumento posicional.

En este ejemplo, el argumento `end` le dice a la función `print()` qué caracter mandar a su salida cuando se llegue al final de sus argumentos posicionales.

Por defecto, `print()` actúa como si el argumento `end` se ejecutara de la siguiente manera `end="\n"`.

El `string` asignado a `end` puede ser de la longitud que sea.

### Sep
El argumento keyword que cambia cómo `print()` separa diferentes argumentos posicionales se llama `sep` (como separador).

```python
print("Hola", "a", "todos", sep="-")
```

Da como resultado

```
Hola-a-todos
```

Ahora se usa un guión `-` para separar las salidas de cada argumento.

Ambos argumentos keyword pueden invocarse al mismo tiempo.

```python
print("Hola", "a", "todos", sep="_", end="*")
print("Qué", "tal", sep="*", end="\n")
```

Y obtenemos

```
Hola_a_todos*Qué*tal
```
