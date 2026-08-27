# Instrucciones Generales
- El proyecto deberá estar escrito en C.

## Consideraciones Tecnicas
- Declarar variables globales está prohibido.
- Si necesitas crear funciones auxiliares para descomponer una función más compleja,
    debes definirlas como static para restringir su alcance al archivo correspondiente.
- Todos los archivos deben colocarse en la raíz de tu repositorio.
- Se prohíbe entregar archivos no utilizados.
- Todos los archivos .c deben compilarse con las opciones (flags) -Wall -Werror -Wextra.
- Debes utilizar el comando ar para generar la librería. El uso de libtool queda prohibido.
- Tu libft.a debe ser creado en la raíz de tu repositorio.

## Funciones de GNL
- Para empezar, deberás rehacer algunas funciones de la GNL. Tus funciones tendrán
    los mismos prototipos y comportamientos que las funciones originales, siguiendo fielmente
    las definiciones indicadas en la página del man de cada función. La única diferencia será el
    nombre: todas deberán comenzar con el prefijo “ft_”. Por ejemplo, strlen se convertirá en ft_strlen.

# Parte obligatoria de GNL
## Ejercicio principal: get_next_line
### Indicaciones
- **`Directorio entrega`**: GNL
- **`Archivos a entregrar`**: get_next_line.c, get_next_line_utils.c y get_next_line.h
- **`Funciones autorizadas`**: read, malloc, free
### Descripcion
- **`get_next_line`**: Escribe una función que devuelva la línea desde un descriptor de archivo.
### Prototipo
- **`char *get_next_line(int fd);`**:
    El prototipo de la función deberá ser el siguiente: `char *get_next_line(int fd)`.
### Valor de retorno
- Devuelve si es posible la linea leida.
- Devuelve `NULL` en caso de error/fallo o si la lectura termina.
### Consideraciones
- Llamar a la función `get_next_line` de manera repetida (por ejemplo, usando un bucle)
    permitirá leer el contenido del archivo hacia el que apunta el descriptor de archivo, línea a línea, hasta el final.
- La función deberá devolver:
    la línea que se acaba de leer
    `NULL` si no hay nada más que leer o si ha ocurrido un error.
- Hay que asegurarse de que la función se comporta adecuadamente cuando lea de un `archivo` y cuando lea de `stdin`.
- Importante: La línea devuelta debe terminar con el `\n`, excepto si se ha llegado al final del archivo y éste no termina con un `\n`.
- Informacion: Un buen comienzo sería saber qué es una variable estática.
- Se considera que `get_next_line()` tiene un comportamiento indeterminado si el
    archivo al que apunta el descriptor de archivo ha cambiado desde la última vez que
    se llamó, siempre que read() no haya llegado al final del archivo.
- Se considera que `get_next_line()` tiene un comportamiento indeterminado cuando lo que se lee es un archivo binario.
    Sin embargo, es posible implementar alguna manera lógica de sortear este problema, si se desea.
- Informacion: Se debería leer lo menos posible cada vez que se llame a `get_next_line()`.
    Si hay un salto de línea, se debería devolver la línea actual.
    No hay que leer el archivo entero y luego procesar cada línea.
- Se pueden añadir todas las funciones de ayuda que se necesiten en el archivo `get_next_line_utils.c`.
- En el archivo de cabecera `get_next_line.h` se deberá incluir tener como mínimo el prototipo de la función `get_next_line`.
- El programa debe compilar con el indicador (flag) `get_next_line()=n`.
    Este indicador se utilizará para determinar el tamaño del buffer de las lecturas de la función read() en el `get_next_line()`.
    Este parámetro será modificado por las personas que hagan la evaluación y por Moulinette para probar tu programa.
- Atencion: Se debería poder compilar este proyecto con y sin el indicador `get_next_line()`, junto a los indicadores habituales.
    Se puede elegir el valor por defecto que se prefiera.
- El programa se compilará de la siguiente forma (se utiliza como ejemplo un tamaño de buffer de 42):
    cc -Wall -Werror -Wextra get_next_line()=42 <archivos>.c -> `cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 *.c`.
- Importante: ¿Funciona correctamente get_next_line si el BUFFER_SIZE es 9999? ¿Y si es 1? ¿Qué tal con 10000000? ¿Sabes por qué?
- Prohibido:
    el uso de libft en este proyecto.
    el uso de lseek.
    el uso de variables globales.

# Parte bonus de GNL
- En esta segunda parte, deberás desarrollar un conjunto de funciones que, o no son de la librería GNL, o lo son pero de una forma distinta.

## Ejercicio: ft_substr


# Requisitos del Readme(ESTO VIENE DE LIBFT, ACTUALIZAR PARA QUE SE CORRESPONDA CON GNL)
- Debe incluirse un archivo README.md en la raíz del repositorio Git.
    Su propósito es permitir que cualquier persona que no esté familiarizada con el proyecto (pares, personal,
    responsables de selección, etc.) pueda entender rápidamente de qué trata el proyecto,
    cómo ejecutarlo y dónde encontrar más información sobre el tema.

- El README.md debe incluir, como mínimo:
    • La primera línea debe estar en cursiva y decir: Este proyecto ha sido creado como parte del currículo de 42 por <login1>[, <login2>[, <login3>[...]]].
    • Una sección de "Descripción"que presente claramente el proyecto, incluyendo su objetivo y una breve visión general.
    • Una sección de "Instrucciones"que contenga cualquier información relevante sobre compilación, instalación y/o ejecución.
    • Una sección de "Recursos"que enumere referencias clásicas relacionadas con el tema (documentación, artículos, tutoriales, etc.),
        así como una descripción del uso de IA, especificando para qué tareas y en qué partes del proyecto se ha utilizado.
- ➠ Podrían requerirse secciones adicionales dependiendo del proyecto (por ejemplo, ejemplos de uso, lista de características, decisiones técnicas, etc.).
- También debe incluirse una descripción detallada de la librería creada para este proyecto.
    La elección del idioma queda a tu criterio. Se recomienda escribir en inglés, pero no es obligatorio.




# Get Next Line

## Instrucciones Generales

* El proyecto deberá estar escrito en **C**.
* Declarar variables globales está prohibido.
* Si necesitas crear funciones auxiliares para descomponer una función más compleja, debes definirlas como `static` para restringir su alcance al archivo correspondiente.
* Todos los archivos deben colocarse en la **raíz de tu repositorio**.
* Se prohíbe entregar archivos no utilizados.
* Todos los archivos `.c` deben compilarse con las opciones:

```text
-Wall -Wextra -Werror
```

* Debes utilizar el comando `ar` para generar la librería. El uso de `libtool` queda prohibido.
* Tu `libft.a` debe ser creado en la raíz de tu repositorio.

---

# Funciones de GNL

Para empezar, deberás rehacer algunas funciones de la GNL.

Tus funciones tendrán los mismos **prototipos y comportamientos que las funciones originales**, siguiendo fielmente las definiciones indicadas en la página del `man` de cada función.

La única diferencia será el nombre: todas deberán comenzar con el prefijo `ft_`.

Por ejemplo:

```c
strlen
```

se convertirá en:

```c
ft_strlen
```

---

# Parte Obligatoria de GNL

## Ejercicio Principal: `get_next_line`

### Información del ejercicio

| Campo                     | Información                                                   |
| ------------------------- | ------------------------------------------------------------- |
| **Directorio de entrega** | `GNL`                                                         |
| **Archivos a entregar**   | `get_next_line.c`, `get_next_line_utils.c`, `get_next_line.h` |
| **Funciones autorizadas** | `read`, `malloc`, `free`                                      |

---

## Descripción

Escribe una función que devuelva la línea desde un descriptor de archivo.

### Prototipo

El prototipo de la función deberá ser:

```c
char *get_next_line(int fd);
```

---

## Valor de retorno

La función:

* Devuelve la línea que se acaba de leer si es posible.
* Devuelve `NULL` en caso de error/fallo.
* Devuelve `NULL` cuando la lectura termina y no hay nada más que leer.

---

## Comportamiento

Llamar a la función `get_next_line` de manera repetida, por ejemplo usando un bucle, permitirá leer el contenido del archivo hacia el que apunta el descriptor de archivo, línea a línea, hasta el final.

La función deberá devolver:

* La línea que se acaba de leer.
* `NULL` si no hay nada más que leer o si ha ocurrido un error.

Hay que asegurarse de que la función se comporta adecuadamente cuando lea de un **archivo** y cuando lo haga de **stdin**.

### Terminación de las líneas

La línea devuelta debe terminar con `\n`, excepto si se ha llegado al final del archivo y éste no termina con un `\n`.

---

## Variables estáticas

> **Información:** Un buen comienzo sería saber qué es una variable estática.

La implementación de `get_next_line()` requiere conservar información entre llamadas consecutivas a la función.

---

## Comportamientos indeterminados

Se considera que `get_next_line()` tiene un comportamiento indeterminado en los siguientes casos:

* El archivo al que apunta el descriptor ha cambiado desde la última vez que se llamó a `get_next_line()`, siempre que `read()` no haya llegado al final del archivo.
* Lo que se lee es un archivo binario.

Sin embargo, es posible implementar alguna manera lógica de sortear este último problema, si se desea.

---

## Lectura eficiente

> **Información:** Se debería leer lo menos posible cada vez que se llame a `get_next_line()`.

Si hay un salto de línea, se debería devolver la línea actual.

No hay que leer el archivo entero y luego procesar cada línea.

La función debe ir leyendo únicamente los datos necesarios hasta poder devolver la línea solicitada.

---

## Funciones auxiliares

Se pueden añadir todas las funciones de ayuda que se necesiten en el archivo:

```text
get_next_line_utils.c
```

Estas funciones auxiliares deben respetar las restricciones generales del proyecto.

---

## Archivo de cabecera

En el archivo:

```text
get_next_line.h
```

se deberá incluir, como mínimo, el prototipo de la función:

```c
char *get_next_line(int fd);
```

---

# `BUFFER_SIZE`

El programa debe compilar con el indicador:

```text
-D BUFFER_SIZE=n
```

Este indicador se utilizará para determinar el tamaño del buffer utilizado por `read()` en `get_next_line()`.

El valor de `BUFFER_SIZE` será modificado por las personas que hagan la evaluación y por Moulinette para probar el programa.

### Compilación

Se debe poder compilar el proyecto tanto **con** como **sin** el indicador `BUFFER_SIZE`, junto a los indicadores habituales.

Se puede elegir el valor por defecto que se prefiera.

Por ejemplo, para utilizar un tamaño de buffer de `42`:

```bash
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 *.c
```

---

## Diferentes tamaños de `BUFFER_SIZE`

La implementación debe funcionar correctamente independientemente del tamaño utilizado.

Es especialmente importante comprobar su comportamiento con valores como:

```text
BUFFER_SIZE = 1
BUFFER_SIZE = 42
BUFFER_SIZE = 9999
BUFFER_SIZE = 10000000
```

### Preguntas importantes

* ¿Funciona correctamente `get_next_line()` si `BUFFER_SIZE` es `9999`?
* ¿Y si es `1`?
* ¿Qué ocurre con `10000000`?
* ¿Sabes por qué?

La implementación debe ser capaz de manejar correctamente buffers tanto pequeños como grandes.

---

# Prohibiciones

Está prohibido:

* Utilizar `libft` en este proyecto.
* Utilizar `lseek`.
* Utilizar variables globales.

---

# Parte Bonus de GNL

En esta segunda parte, deberás desarrollar un conjunto de funciones que, o no son de la librería GNL, o lo son pero de una forma distinta.

## Ejercicio: `ft_substr`

La parte bonus incluye la implementación de:

```c
ft_substr
```

Esta función forma parte del conjunto de funciones adicionales requeridas para la parte bonus del proyecto.

---

# README

## Requisitos

Debe incluirse un archivo:

```text
README.md
```

en la raíz del repositorio Git.

Su propósito es permitir que cualquier persona que no esté familiarizada con el proyecto —pares, personal, responsables de selección, etc.— pueda entender rápidamente:

* De qué trata el proyecto.
* Cómo ejecutarlo.
* Dónde encontrar más información sobre el tema.

---

## Contenido mínimo

El `README.md` debe incluir, como mínimo, las siguientes secciones.

### 1. Primera línea

La primera línea debe estar en cursiva y decir:

> Este proyecto ha sido creado como parte del currículo de 42 por `<login1>[, <login2>[, <login3>[...]]]`.

---

### 2. Descripción

Debe incluirse una sección de **Descripción** que presente claramente el proyecto, incluyendo:

* Su objetivo.
* Una breve visión general.

---

### 3. Instrucciones

Debe incluirse una sección de **Instrucciones** que contenga cualquier información relevante sobre:

* Compilación.
* Instalación.
* Ejecución.

---

### 4. Recursos

Debe incluirse una sección de **Recursos** que enumere referencias clásicas relacionadas con el tema, por ejemplo:

* Documentación.
* Artículos.
* Tutoriales.
* Otras referencias relevantes.

También debe incluir una descripción del uso de **IA**, especificando:

* Para qué tareas se ha utilizado.
* En qué partes del proyecto se ha utilizado.

---

## Secciones adicionales

Podrían requerirse secciones adicionales dependiendo del proyecto.

Por ejemplo:

* Ejemplos de uso.
* Lista de características.
* Decisiones técnicas.
* Explicaciones adicionales.
* Cualquier otra información que facilite la comprensión del proyecto.

---

## Descripción detallada de la librería

También debe incluirse una descripción detallada de la librería creada para este proyecto.

La elección del idioma queda a tu criterio.

> Se recomienda escribir en **inglés**, pero no es obligatorio.
