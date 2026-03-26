[[Databases MOC]]
# Filtrar Datos Numéricos

**Tags**:: #databases/sql/filtrar 
**Links**:: [[SQL]]

Cuando le pedimos a una base de datos que nos devuelva información no siempre queremos que nos devuelva todas las entradas de uno o más campos. Así, SQL nos permite filtrar las entradas, de modo que nos devuelva sólo aquellas que cumplan con el o los criterios de nuestra elección.


## Filtrar Datos Numéricos

Para una base de películas, podemos obtener el título de aquellas que se estrenaron después de 1960:

```sql
SELECT titles
FROM films
WHERE release_year > 1960;
```

Usamos la palabra clave `WHERE` y la condición que queremos que cumplan las entradas del campo `titles` de la tabla `films`.

Para este ejemplo, usamos el operador menor que, `>`. Pero podemos usar:

- `<`
- `>=`
- `<=`
- ` = `
- El operador "no igual es a", $\neq$, que en SQL se escribe así: `<>`.

La keyword `WHERE` también puede usarse con `strings`, por ejemplo:

```sql
SELECT titles
FROM films
WHERE country = 'Japan'
LIMIT 5;
```

Y el orden de ejecución sería:

```sql
FROM films
WHERE country = 'Japan'
SELECT titles
LIMIT 5;
```


### Filtrar con Criterios Múltiples
Hay keywords que nos permiten concatenar distintos criterios de para un sólo `WHERE`. Estos son:

- `OR`
- `AND`
- `BETWEEN`

El operador `OR` se usa cuando tenemos multiples criterios y debemos satisfacer al menos uno de ellos. El operador `AND` se utiliza cuando debemos satisfacer simultáneamente dos condiciones.

Por ejemplo:

```sql
SELECT *
FROM coats
WHERE color='yellow' OR lenght='short';
```

Para obtener los abrigos que sean color amarillo *ó* tengan una medida corta.

```sql
SELECT *
FROM coats
WHERE color='yellow' AND lenght='short';
```

Para obtener los abrigos que sean color amarillo *y* tengan una medida corta. También podemos buscar abrigos que tengan entre 1 y 5 botones:

```sql
SELECT *
FROM coats
WHERE buttons BETWEEN 1 AND 5;
```

>[!warning] Cuidado
>SQL necesita que especifiquemos los campos de donde provienen los valores que queremos que se satisfagan. Así, si queremos un abrigo verde o uno amarillo, debemos escribir dos veces el campo color: `color='yellow OR color='green'`.

### Operadores mixtos
Podemos combinar los operadores para formular condiciones más complejas que los datos deben satisfacer. Por ejemplo, para películas estrenadas en 1994 o 1995 y cuya clasificación sea PG o R escribimos:

```sql
SELECT title
FROM films
WHERE (release_year = 1994 OR release_year = 1995)
	AND (certification = 'PG' OR certification = 'R');
```

Cada condición individual debe ir empaquetada en un par de paréntesis `()`.

Otro ejemplo serían las combinaciones de `BETWEEN`, `AND` y `OR`.

```sql
SELECT title
FROM films
WHERE release_year
	BETWEEN 1994 AND 2000 AND country='UK';
```

>[!info] Nota
>El operador `BETWEEN` es **inclusivo**. Es decir, `BETWEEN 1 AND 5` incluye las entradas con 1 y 5.
