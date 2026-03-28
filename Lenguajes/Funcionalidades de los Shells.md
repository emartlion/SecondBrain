[[Lenguajes MOC]]
# Funcionalidades de los Shells

**Tags**:: #lenguajes/shells 
**Links**:: [[Qué es un Shell]], [[Sustituciones de Wildcards]]

Los shells son tan populares debido a lo concisos que son. Aunque esto no significa que son "simples", ya que ofrecen muchas funcionalidades.

### Procesamiento en Segundo Plano
Dependiendo del comando, los scripts de shell son pueden correr en primer o segundo plano. Los procesos en primer plano son visibles en pantalla y sólo pueden ejecutarse de forma secuencial.

Los procesos en segundo plano no aparecen en pantalla y pueden correr de forma no secuencial. Para ejecutar un script de shell en segundo plano basta con agregar un ampersand (&) al final del script.

### [[Sustituciones de Wildcards]]
Estas sustituciones permiten a los sistemas procesar más de un comando a la vez o encontrar fragmentos de un texto o frases en archivos de texto. Por ejemplo, `*` le dice al sistema que busque coincidencias con cualquier string, incluso strings vacíos. El wildcard `?` busca coincide un caracter, etc.

### Alias de Comandos
Los aliases de shell son atajos a comandos, pueden una sola palabra o una sola letra. Para ver la lista de aliases basta con ingresar el comando `alias`.

###  Historial de Comandos
Hay muchas maneras en las que los shells ahorran tiempo y esfuerzo, una de ellas es el historial de comandos. En vez de volver a escribir un comando que se haya usado anteriormente en una sesión, el historial de comandos muestra rápidamente los comandos usados para acceder a ellos rápidamente.

### Redirección de Entradas/Salidas
La redirección de entradas/salidas, input/output (i/o), permite al usuario permiten cambiar la entrada y salida estándares (`stdin` y `stdout` respectivamente) para asociarlos con la pantalla, el teclado o algún archivo.

### Pipping
El término hace alusión a una *tubería* (pipe) que conecta la salida de un comando/proceso/programa  con la entrada de otro. Esto les permite operar simultáneamente y permite la transferencia continua de datos sin tener que usar la pantalla o un archivo temporal como intermediario.

### Sustitución de Variables de Shell
Cuando el shell se encuentra con una expresión que contiene caracteres especiales, traduce el código a algo que es más legible para los usuarios. A este proceso se le conoce como sustitución de variables o simplemente *variables*.

Las variables también se pueden usar como un *placeholder* para valores aún desconocidos al momento de escribir el código y antes de que esté listo para ejecutarse.