# *Este proyecto ha sido creado como parte del currículo de 42 por <jgilaber>.*

# ft_printf

## Descripción

**ft_printf** consiste en desarrollar una implementación propia de la función `printf()` de la biblioteca estándar de C.

El objetivo del proyecto es comprender cómo funcionan las funciones con un número variable de argumentos (*variadic functions*), aprender a procesar cadenas de formato y mejorar el manejo de la salida estándar mediante llamadas de bajo nivel.

Esta implementación reproduce el comportamiento de `printf` para un conjunto concreto de especificadores de formato definidos en el enunciado del proyecto:

* `%c` - Carácter
* `%s` - Cadena de caracteres
* `%p` - Dirección de memoria de un puntero
* `%d` - Entero con signo
* `%i` - Entero decimal
* `%u` - Entero sin signo
* `%x` - Número hexadecimal en minúsculas
* `%X` - Número hexadecimal en mayúsculas
* `%%` - Carácter `%`

La función devuelve el número total de caracteres escritos, igual que la implementación original de la biblioteca estándar.

---

## Características

* Implementación propia de `printf()`.
* Uso de funciones variádicas mediante `<stdarg.h>`.
* Conversión de números en distintas bases.
* Impresión de direcciones de memoria.
* Gestión del contador de caracteres impresos.
* Código dividido en funciones pequeñas y reutilizables.

---

## Estructura del proyecto

```text
.
├── includes
│ └── ft_printf.h
├── printf_utils
│ └── ft_printf_utils.c
├── ft_printf.c
├── Makefile
└── README.md
```

> Los nombres de los archivos pueden variar ligeramente dependiendo de la organización elegida.

---

## Instrucciones

### Compilar

```bash
make
```

Se generará la biblioteca:

```text
libftprintf.a
```

### Limpiar archivos objeto

```bash
make clean
```

### Limpiar completamente

```bash
make fclean
```

### Recompilar

```bash
make re
```

### Uso

Incluye el archivo de cabecera:

```c
#include "ft_printf.h"
```

Compila enlazando la biblioteca:

```bash
cc main.c libftprintf.a
```

Ejemplo:

```c
#include "ft_printf.h"

int main(void)
{
    ft_printf("Hola %s\n", "42");
    ft_printf("Número: %d\n", 42);
    ft_printf("Hexadecimal: %x\n", 255);
    return (0);
}
```

---

## Algoritmo y estructura de datos

La implementación sigue un algoritmo secuencial que recorre la cadena de formato carácter por carácter.

1. Se lee cada carácter de la cadena.
2. Si el carácter no es `%`, se escribe directamente en la salida estándar.
3. Cuando aparece `%`, se analiza el carácter siguiente para identificar el especificador.
4. Dependiendo del especificador, se obtiene el siguiente argumento mediante `va_arg()` y se llama a la función correspondiente para imprimirlo.
5. Cada función devuelve el número de caracteres escritos, que se acumula hasta obtener el resultado final.

Este diseño presenta varias ventajas:

* Cada conversión está desacoplada del resto.
* El código es más fácil de mantener y ampliar.
* Se evita repetir lógica entre distintos tipos de conversión.

### Estructura de datos

Este proyecto no requiere estructuras de datos complejas.

Únicamente se utilizan:

* La lista de argumentos variádicos (`va_list`) proporcionada por `<stdarg.h>`.
* Variables escalares para almacenar el contador de caracteres y valores temporales durante las conversiones.

Para las conversiones numéricas se emplea un algoritmo recursivo (o iterativo, dependiendo de la implementación) que descompone el número en la base correspondiente (10 o 16), imprimiendo cada dígito en el orden correcto.

No se realiza almacenamiento dinámico de memoria, ya que todos los datos pueden procesarse directamente antes de enviarlos a la salida estándar.

---

## Decisiones de implementación

Durante el desarrollo se tomaron las siguientes decisiones:

* Dividir cada tipo de conversión en una función independiente.
* Reutilizar funciones para minimizar código duplicado.
* Escribir directamente sobre la salida estándar mediante `write()`.
* Mantener el mismo comportamiento que `printf()` siempre que fuera posible dentro de las restricciones del proyecto.
* Priorizar la claridad del código sobre optimizaciones prematuras.

---

## Recursos

### Documentación

* Manual de `printf`

  * https://man7.org/linux/man-pages/man3/printf.3.html

* Manual de `stdarg`

  * https://man7.org/linux/man-pages/man3/stdarg.3.html

* cppreference

  * https://en.cppreference.com/w/c/variadic

* The GNU C Library

  * https://www.gnu.org/software/libc/manual/

### Uso de Inteligencia Artificial

Durante el desarrollo de este proyecto se utilizó IA únicamente como herramienta de apoyo.

Su uso se limitó a:

* Resolver dudas conceptuales sobre funciones variádicas.
* Revisar explicaciones sobre conversiones numéricas.
* Corregir y mejorar la documentación del proyecto (README).

La implementación, el diseño del algoritmo, la arquitectura del código, la depuración y las decisiones técnicas fueron desarrollados manualmente.

---

## Autor

Proyecto desarrollado como parte del currículo de 42 Madrid.
