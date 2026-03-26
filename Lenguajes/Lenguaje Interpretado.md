[[Lenguajes MOC]]
# Lenguaje Interpretado

**Tags**:: #lenguajes #lenguajes/general 
**Links**:: [[Python]], [[R]], [[Lenguaje Compilado]], [[Qué Hace a un Lenguaje]]

Los lenguajes de programación interpretados son aquellos que no necesitan de un compilador para ejecutar su código. En cambio, el código se ejecuta línea por línea directamente por un programa llamado *intérprete*.

```
Código Fuente -> Intérprete -> Ejecución
```

Algunos lenguajes interpretados son [[Python]], [[R]], JavaScript, PHP, Ruby, MATLAB, etc.

El intérprete lee el source code de arriba a abajo, de izquierda a derecha, aunque hay algunas excepciones.

1. Primero, el intérprete checa si todas las líneas subsecuentes son correctas (usando los criterios [[Qué Hace a un Lenguaje|que hacen a un lenguaje]]).
2. Si el intérprete detecta un error, termina su tarea inmediatamente. En este caso, el único resultado es un **Mensaje de Error**: te informará dónde se localiza el error y qué lo causó. Sin embargo, el intérprete no puede leer tus intenciones exactas, y podría detectar errores en situaciones alejadas de su causa real.
>[!example] Por ejemplo
>Si quieres usar una entidad de nombre desconocido, esto causará un error, pero el error será detectado en el lugar donde se intente usar la entidad, no donde el nombre de la entidad fue (mal) introducido. Así, el origen del error viene de antes en el código de donde advierte el intérprete.

3. Si la línea se ve bien, el intérprete intenta ejecutarla.
>[!note] Nota
>Usualmente, cada línea de código se ejecuta por separado, por lo que el trío *lee-checa-ejecuta* puede repetirse muchas veces, más veces que el número real de líneas del código, ya que algunas partes pueden ejecutarse más de una vez.

Es posible que una parte importante del código se logre ejecutar antes de que se encuentre un error. Esto es normal en este modelo de ejecución.

Debido a razones históricas, los lenguajes con el enfoque de interpretación son llamados *scripting languages*, cuyos programas son *scripts*.