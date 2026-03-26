[[Lenguajes MOC]]
# Instrucciones en Python

**Tags**:: #lenguajes/python
**Links**:: [[Python]], [[Invocación de Funciones]]

La invocación de una función es una de los muchos tipos de instrucciones en Python.

Por supuesto, un programa complejo usualmente contiene más de una instrucción. ¿Cómo se acopla más de una instrucción?

La [[Qué Hace a un Lenguaje|sintaxis]] de Python es muy específica en este aspecto. A diferencia de otros lenguajes, Python necesita que *no pueda haber más de una instrucción en una línea de código*. Una línea puede estar vacía (no tiene ninguna instrucción), pero no puede tener dos, tres o cuatro instrucciones.

>[!note] Nota
>Python tiene una excepción a esta regla - **SÍ** permite que una instrucción abarque más de una línea, lo que es útil para instrucciones complejas.

Así, dos instrucciones se ven así:

```python
print("Soy un cacahuate.")
print("Todos somos cacahuates.")
```

Y el output debería verse así:

```
Soy un cacahuate.
Todos somos cacahuates.
```

Ahora, si metemos una invocación "vacía" de `print()` 

```python
print("Soy un cacahuate.")
print()
print("Todos somos cacahuates.")
```

Obtenemos

```
Soy un cacahuate.

Todos somos cacahuates.
```

La invocación no es tan vacía como parece, arroja una línea vacía como salida.