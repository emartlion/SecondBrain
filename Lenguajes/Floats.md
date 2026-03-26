[[Lenguajes MOC]]
# Floats (Valores de Punto Flotante)

**Tags**:: #lenguajes/python/literales  
**Links**:: [[Python]], [[Valores Literales]]

Este tipo de dato está diseñado para representar y guardar números cuya parte fraccionaria es distinta de cero.

Cuando hablamos de *dos y medio*, *menos cero punto cuatro* estamos pensando en números que la computadora considera de punto flotante:

```
2.5
-0.4
```

Una parte crucial de estos números viene en su nombre: de **punto** flotante. Para separar su parte entera de su parte decimal *debemos* usar un punto. Python no permite las comas como separador.

Por otra parte, podemos omitir escribir el cero cuando es el único dígito antes o después de un punto decimal.

```
0.4 = .4
4.0 = 4.
```

Aquí puede surgir una confusión muy común: el `4.0` representa cuatro enteros, `4`. Pero Python los ve y almacena de una forma completamente diferente.

- `4.0` es un `float`, aunque represente cuatro enteros, tiene las virtudes y características de un número de punto flotante.
- `4` es un `int`, de tipo distinto a `float`.

### Notación Científica
Otra forma de escribir números de tipo flotante es con la letra `e`, es decir, utilizando notación científica.

Si queremos escribir un número muy pequeño o muy grande, como la velocidad de la luz expresada en metros sobre segundo $\text{m}/\text{s}$. Escrita explícitamente se ve como `300000000`. Para evitar escribir tantos ceros, usamos las notación científica para escribir `3x10^8`, es decir, tres por diez a la octava potencia.

En Python, podemos usar la notación científica reemplazando el `x10^` por una `E` o `e`. Así, la velocidad de la luz escrita en Python usando esta notación se ve como `3E8` o `3e8`. La letra `e` viene de *exponente*.

>[!note] Nota
>- El exponente (el valor después de `E` debe ser un `int`).
>- La base (el valor antes de `E`) puede ser `int` o `float`.

Si ahora quisiéramos codificar un número muy pequeño, como la constante de Planck, $h = 6.62607\times10^{-34}$, la escribiríamos de la siguiente manera:

```
6.62607E-34
```

>[!note] Note
>El hecho de que hayamos escogido una convención de escritura no significa que Python vaya a escoger la misma. Si le pasamos el número `0.0000000000000000000001` a un `print()` Python lo va a imprimir como `1e-22`.
