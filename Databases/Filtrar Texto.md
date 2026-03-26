[[Databases MOC]]
# Filtrar Datos de Texto

**Tags**:: #databases/sql/filtrar 
**Links**:: [[SQL]]


## Filtrar Texto

En la sección anterior ya filtramos campos cuyas entradas son `strings`. Ahora queremos filtrar un *patrón* más que un texto específico. Para esto usamos las palabras clave:

- `LIKE`
- `NOT LIKE`
- `IN`

### LIKE
Se usa para buscar un patrón dentro de un campo.

Usamos wildcards como un placeholder de algún valor para aislar el patrón que queremos filtrar. El operador `LIKE` tiene dos wild cards:

- `%`, relaciona (*match*) cero, uno o más caracteres.
- `_`, relaciona sólo un caracter.

Por ejemplo:

```sql
SELECT name
FROM people
WHERE name LIKE 'Ade%';
```
---
```
|name         |
|-------------|
|Adel Karam   |
|Adelaide Kane|
|Aden Young   |
```

El filtro nos regresó todas las entradas de `name` que comienzan con `'Ade'`, sin importar qué o cuántos caracteres haya después.

Por otro lado:

```sql
SELECT name
FROM people
WHERE name LIKE 'Ev_';
```
---
```
|name      |
|----------|
|Eve       |
```

La wildcards `_` sólo nos regresa las entradas que empiecen con `'Ev'` y tengan un sólo caracter posteriormente.

>[!info] Nota
>Si quisiéramos buscar el nombre "Eva Méndez" con la wild card `_`, tendríamos que escribir el apellido: `WHERE name LIKE 'Ev_ Méndez`.

### NOT LIKE
Este operador se usa cuando queremos obtener valores que no incluyen el patrón especificado.

Por ejemlpo:

```sql
SELECT name
FROM people;
```
---
```
|name              |
|------------------|
|50 Cent           |
|A. Michael Baldwin|
|A. Raven Cruz     |
|Aaliyah           |
|Aaron Ashmore     |
```

Para dejar afuera a las entradas que comienzan con `A.` escribimos:

```sql
SELECT people
FROM name
WHERE name NOT LIKE 'A.%';
```
---
```
|name              |
|------------------|
|50 Cent           |
|Aaliyah           |
|Aaron Ashmore     |
```

### Posición de las wildcards
Las wildcards pueden ir en el lugar que sea dentro de un texto, y también pueden combinarse y repetirse al gusto.

Por ejemplo:

```sql
SELECT name
FROM people
WHERE name LIKE '%r';
```
---
```
|name           |
|---------------|
|A.J. Langer    |
|Aaron Schneider|
|Aaron Seltzer  |
```

Regresa las entradas que comiencen con cualquier combinación de caracteres y luego lleven una `'r'`. Es decir, todas las entradas que terminen en la letra r. Además:

```sql
SELECT name
FROM people
WHERE name LIKE '__t%';
```
---
```
|name                   |
|-----------------------|
|Aitana Sánchez-Gijón   |
|Anthony 'Critic' Campos|
|Anthony Bell           |
```

