[[Lenguajes MOC]]
# Implementaciones de Python

**Tags**:: #lenguajes/python 
**Links**:: [[Python]]

La [Wiki de Python](https://wiki.python.org/moin/PythonImplementations) define una *implementación de Python* como:

>[!quote]
>Un programa o ambiente, que provee soporte para la ejecución de programas escritos en el lenguaje de Python, siguiendo los lineamientos de la referencia de implementación de CPython.

**CPython** es la implementación tradicional de Python, creada por el mismo Guido van Rossum como su versión de referencia del lenguaje de cómputo Python. Debido a esto, a esta implementación simplemente se le conoce como Python.

Hay otro grupo de implementaciones de Python mantenidos por personas miembros de la Python Software Foundation (*PSF*), con Guido van Rossum como su presidente. Es por esto que a estas versiones se les conocer como **canónicas**. También se les considera como Pythons de referencia, ya que cualquier otra versión debe seguir todos los estándares establecidos por la PSF.

Guido van Rossum utilizó el lenguaje de programación *C* para implementar la primera versión de Python, esta decisión sigue vigente. Todos los Pythons producidos por la PSF están escritos en C. Una de las razones más importantes de esta decisión es que Python puede ser puede ser fácilmente porteado y migrado a distintas plataformas con la habilidad de compilar y ejecutar programas de C (básicamente todas las plataformas existentes).

Es por esto que a la implementación de la PSF se le conoce como *C*Python.

Otras versiones de Python son:
### Cython
Esta variante tiene como objetivo solucionar uno de los grandes problemas de Python: su *falta de eficiencia*. C es un lenguaje mucho más eficiente para realizar cálculos matemáticos grandes y complejos, pero producir el código para ello es mucho más fácil en Python.

Estas desventajas se reconcilian en Cython, donde el código se escribe en Python, y una vez que nos aseguramos de que el código funciona y produce resultados correctos, se traduce a C para correrlo. Así, ambas etapas de desarrollo son tan eficientes como pueden serlo.

### Jython
Esta versión de Python está escrita en Java en vez de C. Esto es útil cuando desarrollas sistemas grandes y complejos en Java, pero te gustaría añadir algo de las flexibilidades de Python.

El tradicional CPython puede resultar difícil de integrar en estos ambientes, ya que la filosofía e ideas de C y Java son muy diferentes. Jython se puede comunicar con infraestructura existente de Java de una manera más eficiente.

>[!note] Nota
>A 6 de febrero del 2026, la implementación actual de Jython se basa en estándares de Python 2.0. No hay una versión de Jython para Python 3.0 hasta ahora.

### PyPy
La serpiente que se come así misma, el ciclo sin fin, ni comienzo. PyPy es una versión de Python escrita en un lenguaje llamado RPython (*Restricted Python*), que de hecho es un subconjunto del mismo Python.

El source code de PyPy no se corre con el método de interpretación. En cambio, es traducido a C y entonces es ejecutado por separado. Esto resulta muy útil si quieres probar una nueva funcionalidad que podría, pero no necesariamente, ser introducida a la implementación mainstream de Python, es más fácil con PyPy que con CPython.

Así, PyPy es más una herramienta para desarrollar Python que para un uso general.

### MicroPython
Esta es una implementación open source optimizada para correr en microcontroladores. Incluye un pequeño subconjunto de la Python Standard Library (*PSL*), pero incluye un gran número de funcionalidades como prompt interactivo o enteros de precisión arbitraria, así como módulos que le dan al programador acceso al hardware de bajo nivel.