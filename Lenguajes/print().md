[[Lenguajes MOC]]
# print() en Python

**Tags**:: #lenguajes/python/funciones/ejemplos 
**Links**:: [[Python]], [[Funciones]]

Esta función:
- Toma sus argumentos (pude ser más o menos de uno).
- Las convierte en un formato leíble por humanos si es necesario (los `strings` no necesitan convertirse).
- Y envía los datos resultantes al dispositivo de salida, usualmente la consola.

### ¿Qué tipo de argumentos espera `print()`?
Esta función puede operar con básicamente todo tipo de datos en Python: strings, números, caracteres, valores lógicos, objetos.

### ¿Qué valor regresa `print()`?
Ninguno. Su efecto es suficiente.


---
Veamos cómo responde esta función cuando le pasamos un número distinto de argumentos.

1. Con *cero* argumentos:

```python
print()
```

Da como salida una línea en blanco.

```

```
 
 
2. Con *un* argumento:

```python
print("Hola")
```

Da como salida el texto Hola.

```
Hola
```

3. Con *más de un* argumento:

```python
print("Perú", "es", "clave")
```

```
Perú es clave
```
