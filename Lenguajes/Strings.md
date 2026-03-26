[[Lenguajes MOC]]
# Strings (Cadenas de Caracteres)

**Tags**:: #lenguajes/python/literales  
**Links**:: [[Python]], [[print()]], [[Valores Literales]]

Las cadenas de caracteres, *strings* o `str` son un tipo de dato que se usa cuando queremos procesar texto.

[[Python]] los identifica con las comillas `" "` o apóstrofes `' '`. Todo lo que ve adentro de ellas se les considera un `str`.

Ahora, ¿cómo podríamos citar alguna frase si para eso necesitamos las comillas? Bueno, hay dos posibles soluciones.

1. Usando el [[Caracteres de Escape y Nueva Línea|caracter de escape]] `\`. Podemos "escapar" a las comillas para que Python no se confunda.

```python
print("\"Matanga\", dijo la changa.")
```
---
```
"Matanga", dijo la changa.
```

2. Podemos aprovechar que Python también acepta apóstrofes y usar, ya sea `" "` o `' '` para delimitar el `str` y usar la opción que sobre para delimitar la cita.

```python
print('"Matanga", dijo la changa.')
```
---
```
"Matanga", dijo la changa.
```


La opción más general es la del caracter de escape. Si ahora lo que quisiéramos insertar es un apóstrofe cuando también lo estamos usando como el delimitador del `str` es tan simple como

```python
print('I\'m Bond, James Bond.')
```
---
```
I'm bond. James Bond.
```


Finalmente, un `str` puede estar vacío, `""` o `''`.