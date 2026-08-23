*Este proyecto ha sido creado como parte del currículo de 42 por jgilaber.*

# Libft

## 📖 Descripción

**Libft** es el primer proyecto del currículo de 42 y consiste en desarrollar una biblioteca propia en lenguaje C que reimplementa funciones estándar de la biblioteca libc, además de incorporar funciones adicionales de utilidad para futuros proyectos.

El objetivo principal es profundizar en los fundamentos del lenguaje C, la gestión de memoria, el manejo de cadenas y estructuras de datos básicas, así como adquirir buenas prácticas de programación y organización de código.

Esta librería servirá como base para numerosos proyectos posteriores del programa de 42, proporcionando un conjunto de herramientas reutilizables y bien documentadas.

---

## ✨ Características

La biblioteca incluye varias categorías de funciones:

### Funciones de la libc

Reimplementación de funciones estándar, entre ellas:

* `ft_isalpha`
* `ft_isdigit`
* `ft_isalnum`
* `ft_isascii`
* `ft_isprint`
* `ft_strlen`
* `ft_memset`
* `ft_bzero`
* `ft_memcpy`
* `ft_memmove`
* `ft_strlcpy`
* `ft_strlcat`
* `ft_toupper`
* `ft_tolower`
* `ft_strchr`
* `ft_strrchr`
* `ft_strncmp`
* `ft_memchr`
* `ft_memcmp`
* `ft_strnstr`
* `ft_atoi`
* `ft_calloc`
* `ft_strdup`

---

### Funciones adicionales

Funciones de manipulación de cadenas y memoria:

* `ft_substr`
* `ft_strjoin`
* `ft_strtrim`
* `ft_split`
* `ft_itoa`
* `ft_strmapi`
* `ft_striteri`
* `ft_putchar_fd`
* `ft_putstr_fd`
* `ft_putendl_fd`
* `ft_putnbr_fd`

---

### Listas enlazadas

Implementación de una estructura de lista simplemente enlazada (`t_list`) junto con las funciones:

* `ft_lstnew`
* `ft_lstadd_front`
* `ft_lstsize`
* `ft_lstlast`
* `ft_lstadd_back`
* `ft_lstdelone`
* `ft_lstclear`
* `ft_lstiter`
* `ft_lstmap`

---

## 🛠️ Instrucciones

### Requisitos

* Sistema operativo Linux o macOS.
* Compilador compatible con C (`gcc` o `clang`).
* `make`.

### Compilación

Para generar la librería:

```bash
make
```

Esto creará el archivo:

```text
libft.a
```

### Limpiar archivos objeto

```bash
make clean
```

### Eliminar todos los archivos generados

```bash
make fclean
```

### Recompilar completamente

```bash
make re
```

---

## 🚀 Ejemplo de uso

Incluye el archivo de cabecera en tu proyecto:

```c
#include "libft.h"
```

Compila enlazando la librería:

```bash
gcc main.c libft.a -I. -o programa
```

Ejemplo sencillo:

```c
#include "libft.h"
#include <stdio.h>

int main(void)
{
    printf("%zu\n", ft_strlen("42 Madrid"));
    return (0);
}
```

---

## 🏗️ Decisiones técnicas

* Todas las funciones siguen la **Norminette** de 42.
* Se evita el uso de funciones prohibidas por el subject.
* La gestión de memoria dinámica se realiza mediante `malloc` y `free`, procurando evitar fugas de memoria.
* La biblioteca está diseñada para ser modular y fácilmente reutilizable en proyectos futuros.

---

## 📚 Descripción detallada de la librería

`libft.a` es una biblioteca estática que agrupa un conjunto de funciones de propósito general escritas íntegramente en C.

Su finalidad es proporcionar implementaciones propias de operaciones frecuentes sobre:

* Caracteres.
* Cadenas de texto.
* Bloques de memoria.
* Conversión entre tipos de datos.
* Salida por descriptores de archivo.
* Manipulación de listas enlazadas.

Cada función ha sido desarrollada desde cero, respetando el comportamiento esperado de sus equivalentes en la libc cuando existen, y siguiendo las restricciones establecidas por el proyecto.

La librería se compila en un único archivo estático (`libft.a`), facilitando su inclusión en otros proyectos mediante enlazado.

---

## 📚 Recursos

### Documentación y referencias

* The C Programming Language — Brian W. Kernighan & Dennis M. Ritchie.
* Advanced Programming in the UNIX Environment — W. Richard Stevens.
* The Linux Manual Pages Project (`man`).
* ISO C Standard Library Documentation.
* Documentación oficial del currículo de 42.

### Uso de Inteligencia Artificial

Durante el desarrollo de este proyecto se ha utilizado IA únicamente como herramienta de apoyo para:

* Revisión y mejora de la documentación.
* Generación y corrección del archivo `README.md`.
* Consulta de explicaciones teóricas sobre conceptos del lenguaje C.

La implementación, diseño y codificación de las funciones de la librería han sido realizadas manualmente siguiendo los requisitos del proyecto y las normas académicas de 42.

---

## 👤 Autor

**Login 42:** `<jgilaber>`

Proyecto realizado como parte del programa de formación de **42 Madrid**.
