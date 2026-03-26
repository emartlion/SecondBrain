[[Lenguajes MOC]]
# Caracteres de Escape y Nueva Línea

**Tags**:: #lenguajes/python 
**Links**:: [[Python]], [[print()]]

La diagonal invertida `\` tiene un significado especial en Python cuando se usa dentro de un `string`. Se conoce como *caracter de escape*.

La palabra *escape* significa eso - la serie de caracteres en el `string` escapa por un momento muy corto para hacer una inclusión especial. En otras palabras, `\` no significa nada por sí mismo, más bien anuncia que el caracter inmediatamente después de `\` también tiene un significado especial.

Veamos un ejemplo.

```python
print("¡Eso es!, dice Jaime\nNo soy un poeta, soy un peatón.")
```

Da como resultado

```
¡Eso es!, dice Jaime

no soy un poeta, soy un peatón.
```

Si usamos `\n` dentro de un `print()` se imprime una nueva línea en consola. La `n` viene de la palabra "newline". El par de `\` con `n` forman un símbolo especial conocido como caracter de línea nueva (*newline character*).

Esta convención tiene dos consecuencias importantes:

1. Si queremos poner un \ dentro de un `string` no podemos olvidarnos de su naturaleza de escape: debemos ponerlo doble. De lo contrario obtendremos un error.

>[!example] Por Ejemplo
>El código
>```python
>print("\")
>```
>devolverá un error. Mientras que
>```python
>print("\\")
>```
>no lo hará.

2. No todos los pares de escape significan algo, `\c` no significa nada y se imprimirá tal cual.