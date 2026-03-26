# Lenguajes MOC

## General
```dataview
TABLE tags AS Tags FROM "Lenguajes" and #lenguajes/general  
```


## Python

### Básico
```dataview
TABLE tags AS Tags FROM "Lenguajes"
WHERE contains(file.tags, "#lenguajes/python")
AND !any(file.tags, (t) => startswith(t, "#lenguajes/python/"))
```

### Literales
```dataview
TABLE tags AS Tags FROM "Lenguajes" AND #lenguajes/python/literales     
```

### Funciones
```dataview
TABLE tags as Tags FROM "Lenguajes"
WHERE contains(file.tags, "#lenguajes/python/funciones/ejemplos") 
AND !any(file.tags, (t) => startswith(t, "#lenguajes/python/funciones/ejemplos/"))  
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