[[Lenguajes MOC]]
# Invocación de Funciones (Python)

**Tags**:: #lenguajes/python #lenguajes/python/funciones 
**Links**:: [[Python]], [[Funciones]]

Para *invocar una función* basta con escribir su nombre y sus argumentos encerrados en paréntesis. Por ejemplo,

```python
print("Hola")
```

¿Qué sucede cuando Python encuentra una invocación como la de abajo?

```python
nombre_funcion(argumento)
```

Vamos por pasos:
1. Python revisa que el nombre de la función sea *legal* (busca en sus datos internos para encontrar una función existente con ese nombre, si no lo encuentra se aborta el código).
2. Se revisa si se cumple con el requerimiento del número de argumentos de la función para *permitirte invocar la función*.
>[!example] Por Ejemplo
>Si la función necesita dos argumentos, cualquier invocación donde sólo se le pase uno será considerada errónea y el código se abortará.

3. Python deja el código principal por un momento y salta dentro de la función invocada; por supuesto, se lleve los argumentos que se le pasaron y se los lleva a la función.
4. La función ejecuta su código, causa el efecto deseado (si acaso), evalúa los resultados deseados (si los hay) y termina su tarea.
5. Finalmente, Python regresa al código principal justo después de la invocación y continúa su ejecución