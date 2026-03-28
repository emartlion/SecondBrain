[[Lenguajes MOC]]
# Tipos de Shells

**Tags**:: #lenguajes/shells  
**Links**:: [[Qué es un Shell]]

Al igual que los lenguajes de programación, también hay una variedad de shells con enfoques diferentes y compatibles con sistemas diferentes.


## Bourne Shell

El shell Bourne fue creado en 1979 por [Stephen Bourne](https://en.wikipedia.org/wiki/Stephen_R._Bourne) en los Laboratorios Bell. Al igual que su predecesor, el shell Thompson, la extensión de archivo de Bourne es `.sh`.

Este shell es el segundo más usado en sistemas tipo Unix, siendo el shell por defecto del sistema operativo [SolarisOS](https://www.oracle.com/solaris). A pesar de su edad, Bourne sigue siento tan popular gracias a que es compacto y rápido. Sin embargo, no es muy interactivo y no tiene historial de comandos. También carece de expresiones lógicas y matemáticas.

Algunos commandos del shell Bourne incluyen:

- Ruta completa: `/bin/sh` y `/sbin/sh`
- Usuario no root por defecto: `$`
- Usuario root por defecto: `#`


## Línea de Comandos (command-line)

El shell de C, extensión `.csh`, y su extensión anterior `.tcsh`, es otro shell tipo Unix desarrollado a finales de los 70s. Fue desarrollado por [Bill Joy](https://en.wikipedia.org/wiki/Bill_Joy).

A diferencia del shell de Bourne, el shell C sí es interactivo, tiene un historial de comandos y alias. También tienen expresiones con sintaxis de tipo [[C]] y aritmética incluida.

Algunos commandos del shell C incluyen:

- Ruta completa: `/bin/csh`
- Usuario no root por defecto: `%`
- Usuario root por defecto: `#`


## KornShell

El KornShell, extensión `.ksh`, fue desarrollado a principios de los 80s por [David Korn](https://en.wikipedia.org/wiki/David_Korn_(computer_scientist)) en los laboratorios Bell. KornShell incorpora mucha de las funcionalidades del shell C, y es un superconjunto de,  y por lo tanto es retrocompatible con, el shell Bourne.

KornShell corre más rápido que el shell C, corre scripts de Bourne y presenta arreglos, funciones y facilidades para manipular strings, todas similares a las de C. Además, incluye aritmética.

Algunos commandos de KornShell incluyen:

- Ruta completa: `/bin/ksh`
- Usuario no root por defecto: `$`
- Usuario root por defecto: `#`


## Shell Bourne Again de GNU ([[bash]])

El shell Bourne Again de [GNU](https://en.wikipedia.org/wiki/GNU), mejor conocido commo Bash, es una alternativa de software libre al shell Bourne. Fue diseñado por Brian Fox para el [proyecto GNU](https://en.wikipedia.org/wiki/GNU_Project) y fue lanzado en 1989. No solo es completamente compatible con el shell Bourne, también toma las las mejores funcionalidades de KornShell y el shell C. Bash tiene ya tiene mapeadas las teclas de dirección para editar y recordar comandos.

Algunos commandos de KornShell incluyen:

- Ruta completa: `/bin/bash`
- Usuario no root por defecto: `bash-x.xx$`
- Usuario root por defecto: `bash-x.xx#`
