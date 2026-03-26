[[Lenguajes MOC]]
# Argumento de Funciones (Python)

**Tags**:: #lenguajes/python #lenguajes/python/funciones #basic
**Links**:: [[Python]], [[Funciones]]

Las funciones pueden tener *un efecto* y *un resultado*. También hay un tercer, y no menos importante elemento, su **argumento**.

Las funciones matemáticas básicas sólo aceptan un argumento. Por ejemplo, la función $\sin(x)$ toma un valor $x$. Por otro lado, las funciones en Python son más versátiles: aceptan cualquier cantidad de argumentos dependiendo de nuestras necesidades.

>[!note] Nota
>Cuando decimos que las funciones pueden aceptar *cualquier* número de argumentos es porque es en serio, incluyendo cero argumentos. Algunas funciones de Python no necesitan argumentos.

Sin importar la cantidad de argumentos, las funciones demandan fuertemente la presencia de un par de paréntesis, **()** (uno que abre y otro que cierra). Por ejemplo, la función `print`.


```python
print("Hola")
```

Todos los argumentos que se quieran pasar a una función deben de ir dentro de los paréntesis.

>[!note] Nota
>Para distinguir palabras ordinarias con el nombre de una función, se debe colocar un par de paréntesis vacíos después del nombre. Por ejemplo, `print()`.

### Un string como argumento de la función `print`
Un `string` o cadena de caracteres se delimita con unas comillas simples, **" "**. Estas comillas cortan el código e indican que lo que está dentro de ellas tiene un significado específico, el de ser datos (data).