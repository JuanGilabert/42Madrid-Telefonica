# 🚀 A-Maze-ing

## 🚀 A-Maze-Ing Project

**Este es el camino**

**Resumen:** ¡Crea tu propio generador de laberintos y muestra su resultado!

**Versión:** 2.2

## Índice

- I Prólogo
- II Instrucciones sobre IA
- III Instrucciones comunes
  - III.1 Reglas generales
  - III.2 Makefile
  - III.3 Directrices adicionales
- IV Parte obligatoria
  - IV.1 Resumen
  - IV.2 Uso
  - IV.3 Formato del archivo de configuración
  - IV.4 Requisitos del laberinto
  - IV.5 Formato del archivo de salida
- V Representación visual
- VI Requisitos de reutilización del código
- VII Requisitos del README
- VIII Bonificaciones
- IX Entrega y evaluación entre pares

### Capítulo I — Prólogo

Los laberintos han fascinado a los seres humanos durante miles de años. Desde el legendario Laberinto de Cnosos de la mitología griega, construido por Dédalo para encerrar al Minotauro, hasta los modernos libros de acertijos y videojuegos, los laberintos siempre han simbolizado misterio, desafío y diseño ingenioso.

En informática, la generación de laberintos es algo más que diversión: es una aplicación práctica de algoritmos, aleatoriedad y teoría de grafos. Algunos algoritmos famosos utilizados para generar laberintos, como los de Prim, Kruskal o el backtracking recursivo, también se emplean en problemas del mundo real, como el diseño de redes o la generación procedural de contenido.

Curiosamente, los laberintos perfectos (con un único camino entre dos puntos cualesquiera) están directamente relacionados con los árboles abarcadores de la teoría de grafos. Construir un laberinto, especialmente uno que puedas visualizar y compartir, es una excelente forma de explorar cómo los ordenadores pueden crear estructura a partir del caos y, al mismo tiempo, divertirse un poco.

> «Un laberinto no es un lugar donde perderse, sino un camino que encontrar.»  
> — Anónimo

### Capítulo II — Instrucciones sobre IA

#### Contexto

Durante tu proceso de aprendizaje, la IA puede ayudarte con muchas tareas diferentes. Tómate el tiempo necesario para explorar las distintas capacidades de las herramientas de IA y cómo pueden ayudarte en tu trabajo. Sin embargo, acércate siempre a ellas con cautela y evalúa críticamente los resultados.

Ya se trate de código, documentación, ideas o explicaciones técnicas, nunca puedes estar completamente seguro de que tu pregunta estaba bien formulada o de que el contenido generado sea correcto. Tus compañeros son un recurso valioso para ayudarte a evitar errores y puntos ciegos.

#### Mensaje principal

- ☛ Usa la IA para reducir las tareas repetitivas o tediosas.
- ☛ Desarrolla habilidades para crear prompts —tanto de programación como de otros tipos— que serán útiles en tu futura carrera.
- ☛ Aprende cómo funcionan los sistemas de IA para anticiparte mejor y evitar riesgos, sesgos y problemas éticos habituales.
- ☛ Continúa desarrollando tanto tus habilidades técnicas como tus habilidades interpersonales trabajando con tus compañeros.
- ☛ Utiliza únicamente contenido generado por IA que comprendas completamente y del que puedas responsabilizarte.

#### Reglas para el estudiante

- Tómate el tiempo necesario para explorar las herramientas de IA y comprender cómo funcionan, de modo que puedas utilizarlas de forma ética y reducir posibles sesgos.
- Reflexiona sobre el problema antes de escribir el prompt. Esto te ayuda a redactar prompts más claros, detallados y pertinentes utilizando un vocabulario preciso.
- Desarrolla el hábito de comprobar, revisar, cuestionar y probar sistemáticamente todo lo generado por IA.
- Busca siempre la revisión de tus compañeros; no dependas únicamente de tu propia validación.

#### Resultados de la fase

- Desarrollar habilidades generales y específicas de dominio para crear prompts.
- Aumentar tu productividad mediante un uso eficaz de las herramientas de IA.
- Seguir reforzando el pensamiento computacional, la resolución de problemas, la adaptabilidad y la colaboración.

#### Comentarios y ejemplos

- Te encontrarás habitualmente con situaciones —exámenes, evaluaciones y otras— en las que tendrás que demostrar que realmente comprendes lo que haces. Prepárate y continúa desarrollando tus habilidades técnicas e interpersonales.
- Explicar tu razonamiento y debatir con tus compañeros suele revelar lagunas en tu comprensión. Haz del aprendizaje entre compañeros una prioridad.
- Las herramientas de IA a menudo carecen de tu contexto específico y tienden a proporcionar respuestas genéricas. Tus compañeros, que comparten tu entorno, pueden ofrecerte conocimientos más relevantes y precisos.
- Mientras que la IA tiende a generar la respuesta más probable, tus compañeros pueden aportar perspectivas alternativas y matices valiosos. Confía en ellos como punto de control de calidad.

##### ✓ Buena práctica

Le pregunto a la IA: «¿Cómo pruebo una función de ordenación?». Me da algunas ideas. Las pruebo y reviso los resultados con un compañero. Juntos perfeccionamos el enfoque.

##### ✗ Mala práctica

Le pido a la IA que escriba una función completa, la copio y pego en mi proyecto. Durante la evaluación entre pares, no puedo explicar qué hace ni por qué. Pierdo credibilidad y suspendo el proyecto.

##### ✓ Buena práctica 2

Utilizo la IA para ayudarme a diseñar un parser. Después repaso la lógica con un compañero. Detectamos dos errores y lo reescribimos juntos: mejor, más limpio y completamente comprendido.

##### ✗ Mala práctica 2

Dejo que Copilot genere el código de una parte clave de mi proyecto. Compila, pero no puedo explicar cómo gestiona las tuberías (`pipes`). Durante la evaluación, no puedo justificarlo y suspendo el proyecto.

### Capítulo III — Instrucciones comunes

#### III.1 Reglas generales

- El proyecto debe estar escrito en Python 3.10 o posterior.
- El proyecto debe cumplir el estándar de codificación `flake8`.
- Tus funciones deben gestionar las excepciones correctamente para evitar fallos. Utiliza bloques `try-except` para gestionar posibles errores. Prefiere gestores de contexto para recursos como archivos o conexiones, de modo que la limpieza se realice automáticamente. Si tu programa se bloquea por excepciones no gestionadas durante la evaluación, se considerará que no funciona.
- Todos los recursos (por ejemplo, identificadores de archivos o conexiones de red) deben gestionarse correctamente para evitar fugas. Utiliza gestores de contexto siempre que sea posible para gestionar estos recursos automáticamente.
- El código debe incluir anotaciones de tipos para los parámetros de las funciones, los valores de retorno y las variables cuando corresponda (utilizando el módulo `typing`). Usa `mypy` para la comprobación estática de tipos. Todas las funciones deben superar `mypy` sin errores.
- Incluye docstrings en funciones y clases siguiendo PEP 257 (por ejemplo, con estilo Google o NumPy) para documentar su propósito, parámetros y valores de retorno.

#### III.2 Makefile

Incluye un `Makefile` en tu proyecto para automatizar tareas habituales. Debe contener las siguientes reglas (el `lint` obligatorio implica las opciones especificadas; se recomienda encarecidamente probar `--strict` para realizar una comprobación más exhaustiva):

- `install`: instalar las dependencias del proyecto utilizando `pip`, `uv`, `pipx` o cualquier otro gestor de paquetes que elijas.
- `run`: ejecutar el script principal del proyecto (por ejemplo, mediante el intérprete de Python).
- `debug`: ejecutar el script principal en modo depuración utilizando el depurador integrado de Python (por ejemplo, `pdb`).
- `clean`: eliminar archivos temporales o cachés (por ejemplo, `__pycache__`, `.mypy_cache`) para mantener limpio el entorno del proyecto.
- `lint`: ejecutar los comandos `flake8 .` y `mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs`.
- `lint-strict` (opcional): ejecutar los comandos `flake8 .` y `mypy . --strict`.

#### III.3 Directrices adicionales

- Crea programas de prueba para verificar la funcionalidad del proyecto (no se entregan ni se califican). Utiliza frameworks como `pytest` o `unittest` para realizar pruebas unitarias que cubran casos límite.
- Incluye un archivo `.gitignore` para excluir artefactos de Python.
- Se recomienda utilizar entornos virtuales (por ejemplo, `venv` o `conda`) para aislar las dependencias durante el desarrollo.

Si se aplican requisitos adicionales específicos del proyecto, se indicarán inmediatamente debajo de esta sección.

### Capítulo IV — Parte obligatoria

#### IV.1 Resumen

Debes implementar un generador de laberintos en Python que reciba un archivo de configuración, genere un laberinto —posiblemente perfecto (con un único camino entre la entrada y la salida)— y lo escriba en un archivo utilizando una representación hexadecimal de las paredes.

También deberás proporcionar una representación visual del laberinto y organizar el código de forma que la lógica de generación pueda reutilizarse posteriormente.

#### IV.2 Uso

Tu programa debe ejecutarse con el siguiente comando:

```bash
python3 a_maze_ing.py config.txt
```

- `a_maze_ing.py` es el archivo principal de tu programa. Debes utilizar exactamente este nombre.
- `config.txt` es el único argumento. Es un archivo de texto plano que define las opciones de generación del laberinto. Puedes utilizar un nombre de archivo diferente.

Tu programa debe gestionar todos los errores correctamente: configuración no válida, archivo no encontrado, sintaxis incorrecta, parámetros de laberinto imposibles, etc. Nunca debe bloquearse inesperadamente y siempre debe proporcionar al usuario un mensaje de error claro.

#### IV.3 Formato del archivo de configuración

El archivo de configuración debe contener un par `CLAVE=VALOR` por línea.

Las líneas que comiencen por `#` son comentarios y deben ignorarse.

Las siguientes claves son obligatorias:

| Clave | Descripción | Ejemplo |
|---|---|---|
| `WIDTH` | Anchura del laberinto (número de celdas) | `WIDTH=20` |
| `HEIGHT` | Altura del laberinto | `HEIGHT=15` |
| `ENTRY` | Coordenadas de entrada (x,y) | `ENTRY=0,0` |
| `EXIT` | Coordenadas de salida (x,y) | `EXIT=19,14` |
| `OUTPUT_FILE` | Nombre del archivo de salida | `OUTPUT_FILE=maze.txt` |
| `PERFECT` | ¿Es el laberinto perfecto? | `PERFECT=True` |

Puedes añadir claves adicionales (por ejemplo, `seed`, `algorithm`, `display mode`) si resultan útiles.

Debe haber un archivo de configuración predeterminado disponible en tu repositorio Git.

#### IV.4 Requisitos del laberinto

- El laberinto debe generarse aleatoriamente, pero se requiere reproducibilidad mediante una semilla (`seed`).
- Cada celda del laberinto tiene entre 0 y 4 paredes, una en cada dirección cardinal (Norte, Este, Sur y Oeste).
- El laberinto debe ser válido, lo que significa:
  - La entrada y la salida existen, son diferentes y están dentro de los límites del laberinto.
  - La estructura garantiza conectividad completa y no existen celdas aisladas (excepto el patrón «42», véase más abajo).
  - Como la entrada y la salida son celdas específicas, debe haber paredes en los bordes exteriores.
  - Los datos generados deben ser coherentes: cada celda vecina debe tener la misma pared, si existe. Por ejemplo, está prohibido que una primera celda tenga una pared en su lado este y que la segunda celda, situada detrás de esa pared, no tenga una pared en su lado oeste.
- El laberinto no puede tener grandes zonas abiertas. Los pasillos no pueden tener más de 2 celdas de anchura. Por ejemplo, puede existir una zona abierta de `2x3` o `3x2`, pero nunca una zona abierta de `3x3`.
- Cuando se represente visualmente (véase más abajo), el laberinto debe contener un «42» visible dibujado mediante varias celdas completamente cerradas.
- Si la opción `PERFECT` está activada, el laberinto debe contener exactamente un camino entre la entrada y la salida (es decir, debe ser un laberinto perfecto: sin bucles).
- Si la opción `PERFECT` no está activada (valor predeterminado), el laberinto debe ser un tablero directamente utilizable para un juego similar a Pac-Man. En concreto:
  - todos los pasillos deben ser alcanzables (conectividad completa), de modo que todo el tablero pueda llenarse de puntos de comida y siga siendo posible ganar;
  - las cuatro esquinas y el centro deben ser pasillos abiertos (los fantasmas y los superpuntos se sitúan en las esquinas y el jugador comienza en el centro);
  - debe ofrecer al menos dos rutas independientes (bucles), de modo que un jugador perseguido siempre tenga una alternativa. Por tanto, un laberinto perfecto, o un laberinto perfecto con una única pared eliminada (un solo bucle), no es aceptable en este modo;
  - los callejones sin salida deben ser poco frecuentes (se toleran un par); un tablero sin ningún callejón sin salida es lo ideal y recibe una bonificación (véase el capítulo de Bonificaciones).
- El patrón «42» puede omitirse si el tamaño del laberinto no permite incluirlo (es decir, si es demasiado pequeño). En ese caso, imprime un mensaje de error en la consola.

> Los dos modos de generación sobre la misma cuadrícula: `PERFECT=True` obliga a crear un único camino sinuoso (cada otro pasillo es un callejón sin salida), mientras que el valor predeterminado `PERFECT=False` mantiene abiertas al menos dos rutas independientes para que un jugador perseguido siempre tenga una alternativa. El camino más corto aparece resaltado en ambos casos.

#### IV.5 Formato del archivo de salida

El laberinto debe escribirse en el archivo de salida utilizando un dígito hexadecimal por celda, donde cada dígito codifica qué paredes están cerradas:

| Bit | Dirección |
|---|---|
| 0 (LSB) | Norte |
| 1 | Este |
| 2 | Sur |
| 3 | Oeste |

- Una pared cerrada pone el bit a `1`; una pared abierta pone el bit a `0`.
- Ejemplo: `3` (binario `0011`) significa que las paredes Sur y Oeste están abiertas. O `A` (binario `1010`) significa que las paredes Este y Oeste están cerradas.
- Las celdas se almacenan fila por fila, una fila por línea.
- Después de una línea vacía, se insertan en el archivo de salida los siguientes 3 elementos, en 3 líneas:
  - las coordenadas de entrada;
  - las coordenadas de salida;
  - el camino válido más corto desde la entrada hasta la salida, utilizando las cuatro letras `N`, `E`, `S`, `W`.
- Todas las líneas terminan con `\n`.

Junto con su archivo de configuración específico, este archivo de salida puede ser probado automáticamente por una *Moulinette*. También se proporciona un script de análisis (`maze_analyzer.py`) con este enunciado.

Dado un archivo de salida, comprueba que la codificación de las paredes es coherente (cada pared compartida está codificada de la misma manera por las dos celdas vecinas) e informa de si el laberinto es perfecto (un único camino, como se exige con `PERFECT=True`) o un tablero jugable (sin callejones sin salida salvo los del patrón «42» y con varias rutas independientes, como se exige por defecto).

Puedes utilizarlo para comprobar que tu generador produce el modo solicitado por el archivo de configuración.

**Ejemplo de archivo de salida**

### Capítulo V — Representación visual

Tu programa debe proporcionar una forma de mostrar visualmente el laberinto, utilizando una de estas opciones:

- representación ASCII en el terminal; o
- una representación gráfica mediante la biblioteca MiniLibX (MLX).

La representación visual debe mostrar claramente las paredes, la entrada, la salida y el camino de solución.

Debe haber interacciones de usuario disponibles, al menos para las siguientes tareas:

- Regenerar un laberinto nuevo y mostrarlo.
- Mostrar/ocultar un camino válido más corto desde la entrada hasta la salida.
- Cambiar los colores de las paredes del laberinto.
- Opcional: establecer colores específicos para mostrar el patrón «42».

Puedes añadir interacciones adicionales.

**Representación predeterminada del laberinto en el terminal**

**Otro laberinto, camino más corto y colores de las paredes**

**Representación del laberinto utilizando MLX**

### Capítulo VI — Requisitos de reutilización del código

Debes implementar la generación del laberinto como una clase única (por ejemplo, `MazeGenerator`) dentro de un módulo independiente que pueda importarse en un proyecto futuro.

Debes proporcionar una breve documentación que describa cómo:

- Instanciar y utilizar tu generador, incluyendo al menos un ejemplo básico.
- Pasar parámetros personalizados (por ejemplo, tamaño, semilla).
- Acceder a la estructura generada y acceder al menos a una solución.

El módulo generador del laberinto debe proporcionar acceso a la estructura del laberinto, pero no tiene por qué utilizar necesariamente el mismo formato que el archivo de salida.

Este módulo reutilizable completo (código y documentación) debe estar disponible en un único archivo adecuado para su posterior instalación mediante `pip`.

Este paquete debe llamarse `mazegen-*` y el archivo debe encontrarse en la raíz de tu repositorio Git.

Se permiten las extensiones `.tar.gz` y `.whl`, generadas mediante la compilación estándar de un paquete de Python.

Ejemplo de nombre de archivo completo:

```text
mazegen-1.0.0-py3-none-any.whl
```

Debes proporcionar en tu repositorio Git todos los elementos necesarios para compilar el paquete. Esto se solicitará durante la evaluación: en un `virtualenv` o equivalente, se instalarán las herramientas necesarias y se volverá a construir el paquete a partir de sus fuentes.

Como este generador de laberintos está pensado para reutilizarse en un proyecto posterior, debes incluir un archivo `LICENSE.md` en la raíz de tu repositorio, indicando la licencia bajo la cual puede reutilizarse tu código.

La elección y redacción de esta licencia forma parte de la tarea: es tu primer contacto con las licencias de software y la propiedad intelectual. La licencia que elijas debe permitir explícitamente la reutilización y distribución de tu generador de laberintos por parte de los proyectos posteriores que se basen en él.

El archivo principal `README.md` (que no forma parte del módulo reutilizable) también debe contener esta breve documentación.

### Capítulo VII — Requisitos del README

Debe proporcionarse un archivo `README.md` en la raíz de tu repositorio Git. Su objetivo es permitir que cualquier persona que no conozca el proyecto (compañeros, personal, reclutadores, etc.) entienda rápidamente en qué consiste, cómo ejecutarlo y dónde encontrar más información sobre el tema.

El `README.md` debe incluir como mínimo:

- La primera línea debe estar en cursiva y decir:

  > This project has been created as part of the 42 curriculum by <login1>[, <login2>[, <login3>[...]]].

- Una sección «Description» que presente claramente el proyecto, incluyendo su objetivo y una breve descripción general.
- Una sección «Instructions» que contenga toda la información relevante sobre compilación, instalación y/o ejecución.
- Una sección «Resources» que enumere referencias clásicas relacionadas con el tema (documentación, artículos, tutoriales, etc.), así como una descripción de cómo se utilizó la IA, especificando para qué tareas y qué partes del proyecto.
- Pueden ser necesarias secciones adicionales dependiendo del proyecto (por ejemplo, ejemplos de uso, lista de funcionalidades, decisiones técnicas, etc.).
- Cualquier adición requerida se indicará explícitamente a continuación.
- La estructura completa y el formato de tu archivo de configuración.
- El algoritmo de generación de laberintos que hayas elegido.
- Por qué elegiste ese algoritmo.
- Qué parte de tu código es reutilizable y cómo.
- Tu equipo y la gestión del proyecto, incluyendo:
  - los roles de cada miembro del equipo;
  - la planificación prevista y cómo evolucionó hasta el final;
  - qué funcionó bien y qué podría mejorarse;
  - si has utilizado herramientas específicas y cuáles.

Si implementas funcionalidades avanzadas (varios algoritmos, opciones de visualización), descríbelas en este archivo `README.md`.

Se recomienda utilizar el inglés; como alternativa, puedes utilizar el idioma principal de tu campus.

### Capítulo VIII — Bonificaciones

Puedes añadir varias bonificaciones a tu proyecto. Estos son algunos ejemplos posibles:

- Un laberinto predeterminado (no perfecto) sin ningún callejón sin salida: un tablero perfectamente «trenzado», de modo que un jugador perseguido nunca quede atrapado en ningún lugar (el script de análisis proporcionado lo confirma con `--max-dead-ends 0`).
- Compatibilidad con varios algoritmos de generación de laberintos.
- Añadir una animación durante la generación del laberinto.

### Capítulo IX — Entrega y evaluación entre pares

Entrega tu tarea en tu repositorio Git como de costumbre. Durante la defensa solo se evaluará el trabajo que se encuentre dentro de tu repositorio. No dudes en comprobar dos veces los nombres de tus archivos para asegurarte de que son correctos.

Durante la evaluación, ocasionalmente se puede solicitar una breve modificación del proyecto. Esto puede consistir en un pequeño cambio de comportamiento, unas pocas líneas de código que escribir o reescribir, o una funcionalidad sencilla de añadir.

Aunque este paso no se aplica necesariamente a todos los proyectos, debes estar preparado para realizarlo si aparece indicado en las directrices de evaluación.

Este paso tiene como objetivo comprobar que realmente comprendes una parte concreta del proyecto.

La modificación puede realizarse en cualquier entorno de desarrollo que elijas (por ejemplo, tu entorno habitual) y debería poder completarse en unos pocos minutos, salvo que se establezca un plazo específico como parte de la evaluación.

Por ejemplo, pueden pedirte que hagas una pequeña actualización en una función o script, modifiques una visualización o ajustes una estructura de datos para almacenar nueva información.

Los detalles (alcance, objetivo, etc.) se especificarán en las directrices de evaluación y pueden variar de una evaluación a otra para el mismo proyecto.

## 🚀 A-Maze-Ing Tests

## 📌 0. Guidelines

### ⚠️ Rules

- La evaluación debe realizarse de forma respetuosa, constructiva y seria.
- La revisión se realiza únicamente sobre el contenido existente en el **repositorio Git del alumno o del grupo**.
- Verifica que el repositorio pertenece al alumno/grupo y que corresponde al proyecto evaluado.
- Comprueba que `git clone` se realiza en una carpeta vacía.
- Comprueba que no se han utilizado aliases maliciosos para mostrar contenido diferente al repositorio oficial.
- El evaluador y el evaluado deben revisar los posibles scripts utilizados para facilitar la evaluación.
- Si el evaluador no ha realizado todavía el proyecto, debe leer previamente el subject completo.
- No se modifica ningún archivo salvo que sea estrictamente necesario y, en ese caso, se explica previamente al evaluado y ambos deben estar de acuerdo.
- Durante la defensa no se permite una terminación inesperada, prematura o no controlada del programa.
- Si se detecta una condición que obliga a finalizar la evaluación, debe utilizarse la flag correspondiente.
- Si el trabajo está vacío, incompleto, no funciona, contiene un error de norma o se detecta cheating, la evaluación puede finalizar con la nota correspondiente según la escala.

### 📁 Expected repository contents

Comprueba que están presentes:

- `README.md`
- `LICENSE.md`
- `a_maze_ing.py`
- `mazegen-*.tar.gz` y/o fichero `.whl`
- Fichero de configuración
- Todos los elementos necesarios para volver a construir el paquete del generador de laberintos
- Los ficheros Python deben pasar `flake8`.
- El código debe pasar `mypy`.

Si falta alguno de los elementos obligatorios, la evaluación obtiene **0**.

### 🚩 Stop conditions

Si se detecta una condición que obliga a finalizar la evaluación, utiliza la flag correspondiente:

- **Empty work → El repositorio está vacío**
- **Incomplete work → Falta trabajo obligatorio**
- **Norme → Error de norma / `flake8`**
- **Cheat → Uso de cheating o contenido no autorizado**
- **Crash → Terminación inesperada o programa no funcional**
- **Incomplete group → El grupo no está completo**
- **Concerning situation → Situación preocupante**
- **Can't support / explain code → El alumno no puede explicar o defender el código**

---

# 📄 1. README.md

**Archivo:** `README.md`

### 🔍 Required content

- El archivo existe en la raíz del repositorio.
- La primera línea está en cursiva y tiene exactamente el formato:
  `This project has been created as part of the 42 curriculum by <login>, <login>.`
- Existe una sección **Description** que explica el propósito y ofrece una visión general del proyecto.
- Existe una sección **Instructions** con información relevante sobre compilación, instalación y/o ejecución.
- Existe una sección **Resources** con referencias externas y explicación del uso de IA, indicando para qué tareas y partes del proyecto se utilizó.
- Se documenta completamente el fichero de configuración.
- Se indica el algoritmo utilizado para generar el laberinto.
- Se explica por qué se eligió dicho algoritmo.
- Se incluye documentación breve sobre el módulo reutilizable del maze generator.
- Se documenta la gestión del proyecto y del equipo:
  - Roles de cada miembro.
  - Planificación prevista y cómo evolucionó.
  - Qué funcionó bien y qué podría mejorarse.
  - Herramientas específicas utilizadas.
- Se permiten otras secciones relevantes.

### 🧪 README Tests

| Prueba | Esperado |
|---|---|
| `README.md` en la raíz | Presente |
| Primera línea obligatoria | Formato correcto |
| Description | Presente |
| Instructions | Presente |
| Resources | Presente |
| Uso de IA documentado | Presente |
| Configuración documentada | Completa |
| Algoritmo explicado | Presente |
| Motivo de elección del algoritmo | Presente |
| Módulo reutilizable documentado | Presente |
| Roles y planificación | Documentados |
| Herramientas utilizadas | Documentadas |

---

# 🎮 2. Standard Usage

**Archivo principal:** `a_maze_ing.py`

### ▶️ Execution

Ejecuta:

```bash
python3 a_maze_ing.py
```

utilizando el fichero de configuración por defecto.

### 🔍 Functionality

- Se genera un laberinto aleatoriamente.
- El laberinto se muestra en el terminal o mediante una ventana gráfica dedicada.
- El programa permite interactuar con el laberinto.
- Se puede regenerar un nuevo laberinto.
- Existe un control para mostrar/ocultar el camino más corto desde la entrada hasta la salida.
- Existe un botón/control para cambiar los colores de las paredes.
- Se pueden implementar interacciones adicionales, pero las anteriores son las obligatorias.

### 🧪 Interactive Menu Tests

| Prueba | Resultado esperado |
|---|---|
| Ejecutar con configuración por defecto | Se genera y muestra un laberinto |
| Regenerar laberinto | Se genera un nuevo laberinto |
| Mostrar shortest path | El camino aparece correctamente |
| Ocultar shortest path | El camino deja de mostrarse |
| Cambiar color de paredes | El color cambia correctamente |
| Interacción general | El programa continúa funcionando sin terminación inesperada |

---

# ⚙️ 3. Configuration File

### 📌 Format

El fichero de configuración debe respetar:

- Las líneas de comentario empiezan por `#`.
- Cada línea de configuración utiliza el formato `KEY=VALUE`.
- Se permite utilizar minúsculas para las claves.
- Deben estar presentes las claves:
  - `WIDTH`
  - `HEIGHT`
  - `ENTRY`
  - `EXIT`
  - `OUTPUT_FILE`
  - `PERFECT`

### 🧪 Error Management Tests

Edita temporalmente la configuración para comprobar:

| Caso | Resultado esperado |
|---|---|
| Eliminar una clave obligatoria | Error gestionado correctamente |
| Línea sin `=` | Error gestionado correctamente |
| Sustituir números por letras | Error gestionado correctamente |
| Boolean incorrecto para `PERFECT` | Error gestionado correctamente |
| `ENTRY` con formato incorrecto | Error gestionado correctamente |
| `EXIT` con formato incorrecto | Error gestionado correctamente |
| Error de configuración | No debe producir una terminación inesperada |

> ⚠️ Si una prueba provoca una terminación inesperada del programa durante la defensa, la evaluación se detiene y la nota final es 0.

---

# 🧱 4. Output File

### ▶️ Generation

Ejecuta `a_maze_ing.py` y verifica que el primer laberinto generado y mostrado también se guarda en el fichero definido por `OUTPUT_FILE`.

### 🔍 Required format

El fichero de salida debe contener:

1. `HEIGHT` líneas.
2. Cada línea debe contener exactamente `WIDTH` caracteres.
3. Una línea vacía.
4. La tupla `ENTRY`.
5. La tupla `EXIT`.
6. El camino más corto desde entrada hasta salida utilizando únicamente:
   - `N`
   - `E`
   - `S`
   - `W`

### 🧪 Maze Analyzer

Ejecuta:

```bash
python3 maze_analyzer.py <output_file>
```

Comprueba:

- Coherencia de las paredes.
- Que el laberinto coincide con el modo indicado en `PERFECT`.
- Que no existe incoherencia estructural.
- Que el modo **perfect maze** se corresponde con `PERFECT=True`.
- Que el modo **Pac-Man-usable** se corresponde con `PERFECT=False`.
- Que la secuencia del shortest path coincide con su representación visual.

Cualquier incoherencia o mismatch hace que esta cuestión falle.

---

# 🌀 5. Maze Generator Module

## 🔧 Maze Generation

El módulo debe cumplir las expectativas del subject.

### 🔍 Functionality

- El laberinto se genera aleatoriamente.
- Puede utilizarse un módulo estándar de Python como `random`.
- Se gestiona correctamente la entrada cuando los parámetros son inconsistentes:
  - `ENTRY` fuera del laberinto.
  - `EXIT` fuera del laberinto.
  - `WIDTH` negativa.
  - `HEIGHT` negativa.
  - Otros parámetros inconsistentes.
- Todas las celdas son alcanzables, salvo las que eventualmente formen el patrón `42`.
- Existen paredes alrededor de todo el laberinto.
- No existe una zona abierta de `3x3` o mayor sin paredes.
- El patrón `42` está presente cuando el tamaño lo permite.
- Si el tamaño no permite crear el patrón `42`, se muestra un mensaje por terminal.

### 🔢 PERFECT=True

Cuando `PERFECT=True`:

- El laberinto es un **perfect maze**.
- Existe exactamente un camino entre entrada y salida.
- No existen loops.

### 👾 PERFECT=False

Cuando `PERFECT=False`:

- El laberinto funciona como un tablero para un juego tipo Pac-Man.
- Todos los corredores son alcanzables.
- Las cuatro esquinas están abiertas.
- El centro está abierto.
- Existen al menos dos rutas independientes.
- Se toleran algunos dead-ends.

### 🎲 Reproducibility

- Con una seed idéntica debe poder reproducirse el mismo laberinto.
- Comprueba esta propiedad modificando la configuración o el código según corresponda.

### 🧪 Objective Tests

Genera un laberinto con cada modo:

```bash
PERFECT=True
python3 maze_analyzer.py <output_file>
```

Debe informar de un **PERFECT maze**.

Después:

```bash
PERFECT=False
python3 maze_analyzer.py <output_file>
```

Debe informar de un **Pac-Man-USABLE**.

Comprueba también:

- Número de loops.
- Número de dead-ends.
- Umbrales indicados por el analyzer.
- Conectividad.
- Coherencia del patrón `42`.
- Reproducibilidad con seed idéntica.

### 🧠 Questions to ask

- ¿Qué algoritmo utilizaste para generar el laberinto?
- ¿Por qué elegiste ese algoritmo?
- ¿Cómo garantizas que todas las celdas son alcanzables?
- ¿Cómo controlas `PERFECT=True` frente a `PERFECT=False`?
- ¿Cómo evitas zonas abiertas de `3x3` o mayores?
- ¿Cómo implementaste o verificaste el patrón `42`?
- ¿Cómo haces que una misma seed produzca el mismo laberinto?

---

# 📦 6. Reusable Maze Generator Module

### ▶️ Package regeneration

El alumno/equipo debe volver a generar el paquete, preferiblemente dentro de un virtualenv o entorno equivalente.

La operación debe volver a crear:

- `mazegen-*.tar.gz`
- y/o el fichero `.whl`

### 🧪 Installation Test

En un **virtualenv diferente**:

1. Instala el paquete recién generado.
2. Utiliza el paquete instalado desde el nuevo entorno.
3. Ejecuta `a_maze_ing.py`.
4. Utiliza su fichero de configuración.
5. Comprueba que todo sigue funcionando correctamente.

### 🔍 Expected result

- El paquete se genera correctamente.
- El paquete se instala correctamente.
- `a_maze_ing.py` utiliza correctamente el módulo instalado.
- El fichero de configuración sigue funcionando.
- El comportamiento del generador es correcto después de la instalación.

---

# 🧹 7. Code Quality & Best Practices

## 🐍 Python

- El código Python pasa `flake8`.
- El código pasa `mypy`.
- No existen errores de norma relevantes.
- Los tipos están correctamente definidos.
- El código es legible y estructurado.
- La gestión de errores es clara.
- Las salidas del programa son comprensibles.
- La implementación no depende de resultados hardcodeados.

## 🧩 Maze Generator

- La lógica de generación está separada adecuadamente.
- El módulo es reutilizable.
- La generación es realmente aleatoria cuando corresponde.
- La seed se respeta correctamente.
- La lógica de `PERFECT` está implementada de forma real.
- La conectividad se comprueba correctamente.
- El formato del output es coherente con la especificación.

## 📦 Packaging

- El paquete puede reconstruirse.
- El paquete puede instalarse en un entorno limpio.
- El programa funciona utilizando el paquete generado.
- No depende accidentalmente del entorno de desarrollo original.

---

# ⭐ 8. Bonuses

> Los bonuses solo pueden considerarse si todas las cuestiones anteriores han sido superadas correctamente.

Se pueden validar hasta **5 bonuses** diferentes, siempre que cada uno represente una cantidad razonable de trabajo.

### Possible bonuses

#### 🌀 No dead-ends

- El laberinto por defecto no contiene ningún dead-end.
- Ejecuta:

```bash
python3 maze_analyzer.py <output_file> --max-dead-ends 0
```

- El resultado debe seguir siendo **Pac-Man-USABLE**.
- El analyzer debe reportarlo como bonus-grade.

#### 🔀 Multiple algorithms

- Soporte para múltiples algoritmos de generación de laberintos.
- El alumno debe poder explicar las diferencias y demostrar que ambos funcionan.

#### 🎞️ Animation

- Existe animación durante la generación del laberinto.
- La animación debe funcionar realmente y no ser únicamente decorativa o hardcodeada.

### 🧪 Bonus evaluation

| Bonus | Comprobación |
|---|---|
| No dead-ends | Analyzer con `--max-dead-ends 0` |
| Multiple algorithms | Demostrar y explicar varios algoritmos |
| Animation | Ejecutar y observar la generación animada |
| Otros | Deben representar una cantidad razonable de trabajo |

---

# 🚩 9. Defense

## 💬 Questions

1. ¿Qué algoritmo has utilizado para generar el laberinto?

2. ¿Por qué has elegido ese algoritmo?

3. ¿Cómo garantizas que todas las celdas del laberinto son alcanzables?

4. ¿Qué diferencia hay entre `PERFECT=True` y `PERFECT=False`?

5. ¿Cómo garantizas que un `PERFECT` maze no contiene loops?

6. ¿Cómo garantizas que existen al menos dos rutas independientes en el modo Pac-Man?

7. ¿Cómo controlas los valores inválidos de `WIDTH` y `HEIGHT`?

8. ¿Qué ocurre si `ENTRY` o `EXIT` están fuera del laberinto?

9. ¿Cómo validas el formato `KEY=VALUE` del fichero de configuración?

10. ¿Cómo implementaste el patrón `42`?

11. ¿Qué ocurre cuando el tamaño del laberinto no permite crear el patrón `42`?

12. ¿Cómo evitas una zona abierta de `3x3` o mayor?

13. ¿Cómo funciona la reproducibilidad mediante una seed?

14. ¿Cómo se calcula o genera el shortest path?

15. ¿Cómo compruebas que el shortest path del fichero de salida coincide con el camino visual?

16. ¿Qué información contiene el fichero generado por `OUTPUT_FILE`?

17. ¿Cómo has estructurado el módulo reutilizable del maze generator?

18. ¿Cómo reconstruyes el paquete `mazegen-*.tar.gz` o `.whl`?

19. ¿Puedes instalar el paquete en un virtualenv nuevo y ejecutarlo desde allí?

20. ¿Qué herramientas utilizaste durante el desarrollo?

21. ¿Qué parte del proyecto desarrollaste tú y qué parte desarrolló el otro miembro del equipo?

22. ¿Qué dificultades encontraste y cómo las resolviste?

---

# 📝 10. Final Evaluation

### Checklist

- Repositorio no vacío
- Repositorio correcto
- Trabajo completo
- `README.md`
- `LICENSE.md`
- `a_maze_ing.py`
- `PERFECT=True` correcto
- `PERFECT=False` correcto
- `maze_analyzer.py` correcto
- Paquete `mazegen-*.tar.gz` y/o `.whl`
- Configuración correcta
- `mypy` y `flake8` correcto
- Standard usage correcto
- Menú interactivo correcto
- Configuración validada
- Output correcto
- Seed reproducible
- Maze generator funcional
- Paquete regenerable
- Instalación en entorno limpio correcta
- Bonuses, si procede
- Defense completada
- El alumno puede explicar el código

### 📊 Result

**Rating:** `0 → 5`

**Flags:**

- Ok
- Outstanding project
- Empty work
- Incomplete work
- Norme
- Cheat
- Crash
- Incomplete group
- Concerning situation
- Can't support / explain code
