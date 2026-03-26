# Databases MOC

## General
```dataview
TABLE tags AS Tags FROM "Databases" and #databases/general
```


## SQL

### Básico
```dataview
TABLE tags AS Tags FROM "Databases"
WHERE contains(file.tags, "#databases/sql")
AND !any(file.tags, (t) => startswith(t, "#databases/sql/"))
```

### Filtros
```dataview
TABLE tags as Tags
FROM "Databases"
WHERE contains(file.tags, "#databases/sql/filtrar") 
	AND !any(file.tags, (t) => startswith(t, "#databases/sql/filtrar/"))
```

### Literales
```dataview
TABLE tags AS Tags FROM "Lenguajes" AND #lenguajes/python/literales     
```

### NumPy
```dataview
TABLE tags AS Tags FROM "Lenguajes" and #lenguajes/python/numpy 
```


## R
```dataview
TABLE tags as Tags from "Lenguajes" and #lenguajes/r 
```


### SQL
```dataview
TABLE tags as Tags from "ML"
```