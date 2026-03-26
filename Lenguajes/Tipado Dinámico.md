[[Lenguajes MOC]]
# Tipado Dinámico

**Tags**:: #lenguajes #lenguajes/general 
**Links**:: [[Python]], [[R]]

Es una característica de algunos lenguajes de programación. Los lenguajes con tipado dinámico no necesitan declarar el tipo de dato de una variable al momento de inicializarla. Además, pueden cambiar dicho tipo de dato sin problemas durante la ejecución.

[[Python]] y [[R]] son ejemplos de lenguajes de tipado dinámico. Por ejemplo, en ``python``:

```python
# La variable x se crea automáticamente como entero
x = 10
print(type(x)) # <class 'int'>

# Ahora la cambiamos a string
x = "Hola"
print(type(x)) # <class 'str'>

# Y ahora a una lista
x = [1, 2, 3]
print(type(x) # <class 'list'>
```