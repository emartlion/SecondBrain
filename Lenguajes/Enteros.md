[[Lenguajes MOC]]
# Enteros (Python)

**Tags**:: #lenguajes/python/literales 
**Links**:: [[Python]], [[Valores Literales]], [[print()]]

Los enteros, *integers* o simplemente `int` son valores numéricos que no tienen una parte fraccional. Este tipo de dato es numérico, por lo que la computadora no los ve ni los guarda como lo haría con un `string`.

La característica de un valor numérico que determina su familia, rango y aplicaciones se llama su *tipo*.

Si codificamos un [[Valores Literales|literal]] y lo colocamos dentro de código en [[Python]], la forma del literal determinará la representación (tipo) que se usará **para guardarse en memoria**.

Python reconoce un valor como entero como una cadena compuesta exclusivamente de números, no debe haber ningún otro tipo de caracter.

Si quisiéramos escribir un número grande como once millones ciento once mil ciento once, usualmente escribiríamos algo como `11,111,111` o `1 111 111` para que no sea tan difícil de leer. Pero en Python esto está prohibido, sólo se aceptan caracteres numéricos o guiones bajos[^1]. Así, la forma correcta de escribir nuestro número sería `1111111` o `1_111_111`.

[^1]: Esta excepción fue introducida en Python 3.6 para literales numéricos. No está disponible en versiones anteriores.

Ahora, ¿cómo codificamos números negativos? Simple, con un guion como signo menos: `-1111111` o `-1_111_111`.

Los números positivos no necesitan llevar un signo más frente a ellos, pero Python lo permite: `+1111111`, `+1_111_111`.

## Números Octales y Hexadecimales

Hay otras convenciones que Python utiliza y que no son muy usadas en el mundo de las matemáticas.

### Representación Octal
Si los dígitos de un `int` están precedidos por un `0O` o `0o` (cero-o), dicho entero será tratado como un valor octal. Esto significa que el número **sólo** debe contener caracteres del 0-7.

El número octal `0o123` tiene un valor decimal igual a 83.

La función [[print()]] hace la conversión a decimal automáticamente.

```python
print(0o123)
```

Da como resultado

```
83
```


### Representación Hexadecimal
Los números de esta representación están precedidos por `0X` o `0x`. El número hexadecimal `0x123` tiene un valor decimal de 291.

La función `print()` también hace la conversión automáticamente.

```python
print(0x123)
```
---
```
291
```
