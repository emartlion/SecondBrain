[[Lenguajes MOC]]
# NumPy Arrays

**Tags**:: #lenguajes/python/numpy #lenguajes/python/numpy 
**Links**:: [[Qué es NumPy|Numpy]], [[indexing]]

Los *arrays* de NumPy, o `ndarray`, son una estructura de datos especializada en guardar y manipular ==datos homogéneos== de manera eficiente y hasta en múltiples dimensiones. Permite realizar operaciones sobre grandes volúmenes de datos de manera rápida.

Este tipo de estructura permite la aritmética de vectores, por lo que también se conocen como *vectores* en Python.

>[!caution] Cuidado
>Si intentas crear un `ndarray` con diferentes tipos de datos, NumPy va a convertir todas las entradas a un tipo de dato común.


NumPy hace operaciones *entrada-a-entrada* sobre sus arrays.


### Creación
Los `ndarray` pueden crearse a partir de un objeto homogéneo (e.g. una lista con el mismo tipo de dato en sus entradas):

```python
np.array(lista)
```

Los parámetros de este método se pueden consultar en su [documentación](https://numpy.org/doc/stable/reference/generated/numpy.array.html).


### Subsetting
Para acceder a los elementos de un *array* usamos [[indexing]] al igual que en una lista.

```python
array = np.array([1, 2, 3])
print(array)
array[1]
```
---
```
array([1, 2, 3])
2
```

Para extraer los elementos de la lista mayores a 2 vemos que
```python
array > 2
```
---
```
array([False, False, True])
```

Entonces usamos subsetting:
```python
array[array > 2]
```
---
```
array([3])
```


### N-Dimensiones
Los arrays son estructuras que soportan diferentes dimensionalidades, de ahí que su tipo de dato sea `ndarray` (n-dimensional array).

- Para n = 2
```python
np_2d = np.array([[1, 2, 3],
				  [4, 5, 6]])
np_2d
```
---
```
array([[1, 2, 3],
	   [4, 5, 6]])
```

  El atributo `shape` nos permite ver explícitamente el tamaño del array.

```python
np_2d.shape
```
---
```
(2, 3) # 2 rows, 3 columns
```
