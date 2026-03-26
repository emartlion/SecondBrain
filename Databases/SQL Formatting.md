[[Databases MOC]]
# SQL Formatting

**Tags**:: #databases/sql 
**Links**:: [[SQL]]

La sintaxis o el formateado de SQL es muy flexible. Pero, por temas de legibilidad y de una mejor colaboración, es buena idea seguir las buenas prácticas del lenguaje.

El siguiente código es válido, pero no es bien visto:

```sql
select title, release_year, country from films limit 3
```

La forma correcta y legible es:

```sql
SELECT title, release_year, country
FROM films
LIMIT 3;
```

Hay que:

- Capitalizar las keywords.
- Escribir los nombres de los campos (fields, columnas) con `_` en lugar de espacios.
- Separar los comandos en líneas nuevas.
- Terminar el código con un `;`, ya que algunos [[SQL|sabores]] de SQL lo requieren e indica el fin del query.

>[!warning] Cuidado
>Es posible llamar a un campo `release year` en vez de `release_year`, pero al momento de llamarlo en un query, tenemos que escribir el nombre entre comillas para indicar que es un string, de lo contrario SQL nos devolverá un error.

Sin embargo, cada usuario puede construir sobre estas convenciones generales. Así, es recomendado seguir una *guía de estilos* de SQL, como la [guía de estilo de Holywells](https://www.sqlstyle.guide/).