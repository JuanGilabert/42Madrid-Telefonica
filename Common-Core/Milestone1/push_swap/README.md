# *Este proyecto ha sido creado como parte del currículo de 42 por `<jgilaber>` y `<aliao-tr>`.*

# push_swap

## 📖 Descripción

**push_swap** es un proyecto del currículo de 42 cuyo objetivo consiste en ordenar una secuencia de números enteros utilizando únicamente un conjunto limitado de operaciones sobre dos pilas.

El programa recibe una lista de números como argumentos, los almacena en dos pilas denominadas **A** y **B**, y debe generar la secuencia de instrucciones necesaria para ordenar los elementos en orden ascendente utilizando el menor número posible de movimientos.

Este proyecto permite profundizar en conceptos fundamentales de la programación en C, como la implementación de estructuras de datos dinámicas, el diseño y análisis de algoritmos, la optimización de operaciones y el tratamiento eficiente de la memoria.

Además, constituye una primera aproximación al estudio de la complejidad algorítmica y al desarrollo de soluciones orientadas al rendimiento.

---

## ✨ Características

### Funcionalidad principal

* Recepción de números enteros mediante argumentos de línea de comandos.
* Validación de la entrada y detección de errores.
* Gestión de números negativos y positivos.
* Detección de valores duplicados.
* Ordenación utilizando exclusivamente las operaciones permitidas.
* Generación de una secuencia optimizada de instrucciones.

---

### Operaciones permitidas

#### Intercambio

* `sa` → Intercambia los dos primeros elementos del stack a.
    No hace nada si hay solo uno o ningún elemento.
* `sb` → Intercambia los dos primeros elementos del stack b.
    No hace nada si hay solo uno o ningún elemento.
* `ss` → Ejecuta `sa` y `sb` simultáneamente.

#### Inserción

* `pa` → Toma el primer elemento del stack b y lo coloca el primero en el stack a.
    No hace nada si b está vacío.
* `pb` → Toma el primer elemento del stack a y lo coloca el primero en el stack b.
    No hace nada si a está vacío.

#### Rotación

* `ra` → Desplaza hacia arriba todos los elementos del stack a una posición, convirtiendo el primer elemento en el último.
* `rb` → Desplaza hacia arriba todos los elementos del stack b una posición, convirtiendo el primer elemento en el último.
* `rr` → Ejecuta `ra` y `rb` simultáneamente.

#### Rotación inversa

* `rra` → Desplaza hacia abajo todos los elementos del stack a una posición, convirtiendo el último elemento en el primero.
* `rrb` → Desplaza hacia abajo todos los elementos del stack b una posición, convirtiendo el último elemento en el primero
* `rrr` → Ejecuta `rra` y `rrb` simultáneamente.

---

# Casos de ejecucion especificos

* `push_swap --bench` → No muestra nada al no haber ningun numero como argumento. Se da por hecho que bench estara al completo a 0.
* `push_swap --simple 3 2 1 --simple` → Muestra las operaciones realizadas para ordenar la secuencia `3 2 1`, aceptando como estrategia la indicada aunque la misma este duplicada.

---

## 🛠️ Instrucciones

### Requisitos

* Sistema operativo Linux o macOS.
* Compilador compatible con C (`cc` o `clang`).
* `make`.

### Compilación

Para generar el ejecutable:

```bash
make
```

Esto creará el archivo:

```text
push_swap
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

Ordenar una pequeña secuencia:

```bash
./push_swap 2 1 3
```

Salida:

```text
sa
```

Otro ejemplo:

```bash
./push_swap 3 2 5 1 4
```

Salida posible:

```text
rra
rra
pb
ra
ra
pb
sa
rra
pa
pa
```

Comprobar el resultado utilizando el programa `checker`:

```bash
ARG="3 2 5 1 4"; ./push_swap $ARG | ./checker_linux $ARG
```

Salida:

```text
OK
```

---

## 🏗️ Decisiones técnicas

* Todas las funciones siguen la **Norminette** de 42.
* La memoria dinámica se gestiona mediante `malloc` y `free`, evitando fugas de memoria.
* La entrada se valida completamente antes de iniciar el proceso de ordenación.
* Los números se almacenan en estructuras dinámicas para facilitar las operaciones de inserción y rotación.
* Se emplean algoritmos diferentes según el tamaño del conjunto de datos.

---

## ⚙️ Algoritmos seleccionados

La estrategia de ordenación se divide en dos partes.

### Ordenación para pocos elementos

Para secuencias reducidas (entre 2 y 5 elementos) se utilizan algoritmos específicos construidos manualmente.

Estos algoritmos:

* Analizan la posición relativa de cada elemento.
* Seleccionan directamente la combinación mínima o casi mínima de operaciones.
* Reducen considerablemente el número de movimientos.

Por ejemplo:

* 2 elementos → máximo 1 operación.
* 3 elementos → máximo 2 operaciones.
* 4 elementos → máximo 7 operaciones y con uso de la pila B para simplificar la ordenación.
* 5 elementos → máximo 10 operaciones y con uso de la pila B para simplificar la ordenación.

---

### Ordenación simple: Selection Sort mediante extracción de mínimos

### Estrategia Simple

La **estrategia simple** se basa en un enfoque similar al **Selection Sort**, adaptado a las restricciones de `push_swap`.

* Buscar el **elemento más pequeño** de la pila `A`.
* Comprobar su posición y elegir la rotación más corta:

  * `ra` si está más cerca del inicio.
  * `rra` si está más cerca del final.
* Llevar el mínimo al `top` y enviarlo a la pila `B` mediante `pb`.
* Repetir el proceso hasta vaciar `A`.
* Finalmente, devolver todos los elementos de `B` a `A` mediante `pa`.

De esta forma, los elementos se extraen en orden creciente y la pila `A` queda ordenada.

---

### Ordenación media: Chunk Sort

La estrategia media divide los elementos del stack A en chunks según su índice.

### Medium Strategy

* Divide los elementos de la pila `A` en **chunks** según su `index`.
* Recorre la pila `A` buscando elementos que pertenezcan al chunk actual.
* Si el elemento pertenece al chunk:

  * Hace `pb` para moverlo a la pila `B`.
  * Hace `rb` si pertenece a la mitad inferior del chunk.
* Si el elemento no pertenece al chunk:
  * Hace `ra` para seguir buscando.
* Cuando todos los elementos están en la pila `B`, comienza la reconstrucción.
* Se busca la posición del elemento con mayor `index` en la pila `B`.
* Según la posición del máximo:
  * Usa `rb` si está en la primera mitad.
  * Usa `rrb` si está en la segunda mitad.
* Cuando el máximo está en el `top`, hace `pa` para pasarlo a la pila `A`.
* Repite el proceso hasta vaciar `B`.
* Finalmente la pila `A` queda ordenada de menor a mayor.


### Ordenación compleja: Radix Sort sobre índices normalizados

Para conjuntos de mayor tamaño se utiliza una variante de **Radix Sort binario**.

Antes de comenzar la ordenación:

1. Los números se copian y se ordenan.
2. Cada valor recibe un índice correspondiente a su posición en el conjunto ordenado.
3. Los valores originales se sustituyen por dichos índices.

Por ejemplo:

Entrada:

```text
40 10 -2 100
```

Índices:

```text
2 1 0 3
```

Una vez normalizados los datos:

1. Se procesa cada bit del índice comenzando por el menos significativo.
2. Si el bit actual es `0`, el elemento se envía a la pila B mediante `pb`.
3. Si el bit actual es `1`, se realiza una rotación de la pila A mediante `ra`.
4. Cuando todos los elementos han sido examinados, los elementos almacenados en B se devuelven a A mediante `pa`.
5. El proceso se repite para todos los bits necesarios.

Al finalizar el último recorrido, la pila A queda completamente ordenada.

---

## 📈 Justificación del algoritmo

La elección de **Radix Sort binario** está motivada por varias razones.

### Rendimiento predecible

El número de operaciones crece de manera aproximadamente lineal respecto al número de elementos:

```text
O(n · k)
```

donde:

* `n` es el número de elementos.
* `k` es el número de bits necesarios para representar el índice máximo.

Dado que `k` es pequeño incluso para conjuntos grandes, el rendimiento resulta muy estable.

### Adaptación a las operaciones permitidas

Las operaciones de `push_swap` encajan de forma natural con el funcionamiento de Radix Sort:

* `pb` permite separar los elementos cuyo bit es `0`.
* `ra` conserva el orden relativo de los elementos cuyo bit es `1`.
* `pa` reconstruye la pila principal para la siguiente iteración.

Por este motivo, el algoritmo puede implementarse utilizando exclusivamente las operaciones autorizadas por el subject.

### Simplicidad y robustez

La normalización de índices elimina problemas asociados a:

* Números negativos.
* Valores extremadamente grandes.
* Comparaciones complejas entre enteros.

El algoritmo trabaja únicamente con índices consecutivos:

```text
0 ... n - 1
```

lo que simplifica notablemente la implementación y reduce la posibilidad de errores.

---

## 🗂️ Estructura de datos

Las pilas se implementan mediante listas enlazadas.

Cada nodo almacena:

* El valor original.
* El índice normalizado.
* Un puntero al siguiente elemento.
* Un puntero al anterior elemento.

La utilización de listas enlazadas ofrece varias ventajas:

* Inserción y extracción en tiempo constante.
* Rotaciones eficientes.
* Gestión dinámica de la memoria.
* Ausencia de límites fijos de capacidad.

Estas características hacen que las listas enlazadas sean especialmente adecuadas para representar las pilas de `push_swap`.

---

## 📚 Descripción detallada del proyecto

`push_swap` es un programa orientado al estudio de la eficiencia algorítmica bajo restricciones operacionales.

A diferencia de los algoritmos de ordenación tradicionales, el objetivo no consiste únicamente en obtener una secuencia ordenada, sino en minimizar el número de operaciones disponibles sobre dos pilas.

La combinación de estructuras dinámicas, algoritmos especializados para conjuntos pequeños y Radix Sort para conjuntos grandes permite obtener soluciones eficientes y escalables respetando todas las limitaciones impuestas por el proyecto.

---

## 📚 Recursos

### Documentación y referencias

* The C Programming Language — Brian W. Kernighan & Dennis M. Ritchie.
* Introduction to Algorithms — Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest & Clifford Stein.
* Algorithms — Robert Sedgewick & Kevin Wayne.
* The Linux Manual Pages Project (`man atoi`, `man malloc`, `man free`).
* Documentación oficial del currículo de 42.
* Documentación sobre algoritmos de ordenación y análisis de complejidad algorítmica.

### Uso de Inteligencia Artificial

Durante el desarrollo de este proyecto se ha utilizado IA únicamente como herramienta de apoyo para:

* Revisión y mejora de la documentación.
* Generación y corrección del archivo `README.md`.
* Consulta de explicaciones teóricas sobre estructuras de datos, análisis de complejidad y funcionamiento de los algoritmos de ordenación.
* Corrección de errores e.g memory leaks, SIGSEGV, SIGINT, etc...

La implementación, diseño y codificación del programa `push_swap` han sido realizados manualmente siguiendo los requisitos del proyecto y las normas académicas de 42.

---

## 📊 Rendimiento

* 100 números aleatorios: entre 600 y 1100 operaciones.
* 500 números aleatorios: entre 6400 y 6800 operaciones.

---

## 👤 Autor

**Login 42:** `jgilaber` y `aliao-tr`

Proyecto realizado como parte del programa de formación de **42 Madrid**.
