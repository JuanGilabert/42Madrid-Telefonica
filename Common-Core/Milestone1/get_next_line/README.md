*Este proyecto ha sido creado como parte del currículo de 42 por `jgilaber`.*

# Get Next Line

## 📖 Descripción

**Get Next Line (GNL)** es un proyecto del currículo de 42 cuyo objetivo consiste en desarrollar una función capaz de leer un archivo o flujo de entrada línea a línea.

La función principal, `get_next_line()`, devuelve una línea completa cada vez que es llamada, manteniendo internamente el estado de lectura para continuar desde el punto exacto donde terminó la llamada anterior.

Este proyecto permite profundizar en conceptos fundamentales del lenguaje C, como la gestión dinámica de memoria, el manejo de descriptores de archivo (*file descriptors*), el uso de variables estáticas y el tratamiento eficiente de buffers de lectura.

Además, constituye una base importante para proyectos posteriores donde sea necesario procesar archivos o entradas de datos de manera incremental.

---

## ✨ Características

### Funcionalidad principal

* Lectura de archivos línea a línea.
* Soporte para cualquier descriptor de archivo válido.
* Conservación del estado entre llamadas mediante variables estáticas.
* Compatible con diferentes tamaños de `BUFFER_SIZE`.
* Gestión adecuada de memoria para evitar fugas.

---

### Bonus

La versión bonus permite gestionar múltiples descriptores de archivo simultáneamente, manteniendo un estado independiente para cada uno de ellos.

Esto posibilita alternar llamadas entre distintos archivos sin perder la posición de lectura de ninguno.

---

## 🛠️ Instrucciones

### Requisitos

* Sistema operativo Linux o macOS.
* Compilador compatible con C (`gcc` o `clang`).
* `make`.

### Compilación

Para compilar los archivos del proyecto:

```bash
make
```

Si el proyecto se utiliza junto con otro programa, basta con incluir los archivos fuente correspondientes durante la compilación.

Ejemplo:

```bash
gcc main.c get_next_line.c get_next_line_utils.c -D BUFFER_SIZE=42 -o programa
```

### Compilar la versión bonus

```bash
gcc main.c get_next_line_bonus.c get_next_line_utils_bonus.c -D BUFFER_SIZE=42 -o programa
```

---

## 🚀 Ejemplo de uso

Incluye el archivo de cabecera en tu proyecto:

```c
#include "get_next_line.h"
```

Ejemplo sencillo:

```c
#include "get_next_line.h"
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int     fd;
    char    *line;

    fd = open("texto.txt", O_RDONLY);
    while ((line = get_next_line(fd)))
    {
        printf("%s", line);
        free(line);
    }
    close(fd);
    return (0);
}
```

---

## 🏗️ Decisiones técnicas

* El proyecto sigue la **Norminette** de 42.
* Se utilizan exclusivamente las funciones permitidas por el subject (`read`, `malloc` y `free`).
* La persistencia de datos entre llamadas se implementa mediante una variable estática.
* Se minimizan las llamadas al sistema leyendo bloques de tamaño `BUFFER_SIZE`.
* Toda la memoria reservada dinámicamente es liberada cuando deja de ser necesaria.

---

## ⚙️ Algoritmo utilizado

La implementación se basa en una estrategia de **buffer persistente**.

Cada vez que se invoca `get_next_line()`, la función realiza los siguientes pasos:

1. Comprueba si existe información almacenada de llamadas anteriores.
2. Lee nuevos bloques de tamaño `BUFFER_SIZE` mediante `read()`.
3. Concatena los datos recién leídos con el contenido previamente almacenado.
4. Busca el carácter de salto de línea (`'\n'`).
5. Si encuentra una línea completa:

   * Reserva memoria para devolverla.
   * Guarda el contenido restante para futuras llamadas.
6. Si se alcanza el final del archivo:

   * Devuelve el contenido restante, aunque no termine en `'\n'`.
   * Libera la memoria utilizada por el buffer estático.

### Justificación del algoritmo

La utilización de un buffer estático permite conservar la información que aún no ha sido devuelta al usuario sin necesidad de reposicionar el descriptor de archivo ni volver a leer datos ya procesados.

Este enfoque resulta eficiente porque:

* Reduce el número de llamadas a `read()`.
* Evita procesar varias veces la misma información.
* Permite trabajar correctamente con cualquier valor de `BUFFER_SIZE`.
* Facilita la ampliación a múltiples descriptores de archivo en la parte bonus mediante un array o estructura indexada por el `file descriptor`.

La complejidad temporal depende del tamaño de las líneas leídas, siendo aproximadamente lineal respecto a la cantidad de caracteres procesados.

---

## 📚 Descripción detallada del proyecto

`get_next_line()` es una función diseñada para proporcionar una interfaz sencilla para la lectura secuencial de archivos.

A diferencia de funciones tradicionales como `read()`, que operan sobre bloques arbitrarios de bytes, `get_next_line()` abstrae este comportamiento y devuelve directamente una línea completa en cada llamada.

Internamente, la función administra un área de almacenamiento temporal donde conserva los datos pendientes de procesar, garantizando que ninguna información se pierda entre llamadas consecutivas.

La versión bonus amplía este comportamiento permitiendo mantener un buffer independiente para cada descriptor de archivo abierto.

---

## 📚 Recursos

### Documentación y referencias

* The C Programming Language — Brian W. Kernighan & Dennis M. Ritchie.
* Advanced Programming in the UNIX Environment — W. Richard Stevens.
* The Linux Manual Pages Project (`man read`, `man open`, `man close`).
* POSIX Programmer's Manual.
* Documentación oficial del currículo de 42.

### Uso de Inteligencia Artificial

Durante el desarrollo de este proyecto se ha utilizado IA únicamente como herramienta de apoyo para:

* Revisión y mejora de la documentación.
* Generación y corrección del archivo `README.md`.
* Consulta de explicaciones teóricas sobre la gestión de memoria, variables estáticas y descriptores de archivo.

La implementación, diseño y codificación de la función `get_next_line()` han sido realizados manualmente siguiendo los requisitos del proyecto y las normas académicas de 42.

---

## 👤 Autor

**Login 42:** `jgilaber`

Proyecto realizado como parte del programa de formación de **42 Madrid**.
