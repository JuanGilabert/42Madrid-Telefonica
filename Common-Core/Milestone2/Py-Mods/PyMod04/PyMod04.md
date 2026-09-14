# 📚 Python Module 04

## 📌 0. Guidelines

### ⚠️ Rules

- La revisión se realiza **en presencia del alumno evaluado**.
- Mantén una actitud educada, respetuosa y constructiva. Comenta con el alumno los problemas encontrados y las posibles diferencias de interpretación del subject.
- Comprueba que el repositorio Git pertenece al alumno y corresponde al proyecto correcto.
- Comprueba que `git clone` se realiza en una carpeta vacía. Se evalúa únicamente el contenido del **repositorio Git del alumno**.
- Si no hay contenido, la evaluación termina aquí: **Empty work**.
- No se han utilizado alias o scripts maliciosos para alterar el contenido evaluado.
- El evaluador y el evaluado han revisado los posibles scripts utilizados durante la evaluación.
- Si el evaluador no ha realizado todavía el proyecto, debe leer previamente el subject completo.
- No debería ser necesario modificar ningún archivo salvo el de configuración, si existe. Cualquier modificación debe explicarse y acordarse previamente con el evaluado.
- La escala solicita expresamente una modificación de código en el ejercicio 3 para comprobar el cierre automático de los archivos.
- Pide ayuda al alumno para ejecutar las pruebas de cada ejercicio si es necesario.
- Ante un programa que no funciona u otra incidencia que obliga a finalizar la evaluación, utiliza la flag correspondiente. La escala establece **0**, o **-42 en caso de trampa**.
- No se permiten terminaciones inesperadas, prematuras o no controladas del programa.
- Salvo en caso de trampa, se anima a continuar la discusión pedagógica después de terminar la calificación, para identificar los problemas y evitar que se repitan.

### 📁 Structure

- Comprueba que la estructura del proyecto coincide con el subject.
- Comprueba que **solo están presentes en el repositorio los archivos solicitados**. La escala indica que, si no se cumple, la revisión se detiene.
- Si falta contenido requerido, utiliza la flag **Incomplete work**.
- Comprueba los archivos correspondientes a los siguientes ejercicios:

| Ejercicio | Programa que debe localizarse |
|---|---|
| 0 | Ancient Text Recovery |
| 1 | Archive Creation |
| 2 | Stream Management |
| 3 | Vault Security |

> **Alcance de la fuente:** esta guía se basa en **PyMod04Eval.pdf**, cuyo margen derecho está recortado. El PDF no muestra los nombres de los archivos de entrega ni la interfaz exacta de ejecución. Localiza esos nombres y argumentos en el subject para aplicar los pasos de ejecución. También está cortado el final de la tarea de recodificación del ejercicio 3; se conserva el requisito visible de verificar el cierre automático y se identifican las pruebas propuestas para comprobarlo.

### 🧰 General concepts to check

- El código está escrito para **Python 3.10 o superior**.
- El código cumple los estándares de `flake8`, sin errores.
- Todas las funciones y métodos tienen **type hints**. Comprueba las anotaciones de parámetros y retorno utilizando `mypy`.
- **No se requieren docstrings para este módulo.**
- El código es legible y está bien estructurado.
- Los nombres de variables son significativos y descriptivos.
- La gestión de errores es apropiada.
- Se utiliza `open()` para abrir archivos y los modos de apertura se corresponden con la operación requerida.
- Se utilizan `read()`, `write()`, `print()` y `close()` donde lo exige cada ejercicio.
- Se distingue entre entrada estándar, salida estándar y salida de errores.
- El ejercicio 3 utiliza `with` para gestionar los archivos y comprobar su cierre automático.

### 🧪 Test preparation

- Crea archivos de prueba con contenido conocido, como solicita la escala.
- Incluye varios contenidos distintos para comprobar que la lectura y la escritura dependen realmente del archivo utilizado.
- Prepara una ruta inexistente y un archivo que el usuario de ejecución no pueda leer para probar los errores de apertura.
- Para probar la sobrescritura, utiliza un archivo de prueba con contenido previo conocido.
- Mantén los archivos de prueba identificados y fuera del contenido versionado que se evalúa, salvo que el subject indique otra cosa.
- Los ejemplos y preguntas de esta guía concretan las comprobaciones de la escala; no fijan mensajes literales ni interfaces que el PDF no especifica.

---
---

# 📜 1. Exercise 0 — Ancient Text Recovery

**Archivo:** el indicado en el subject para **Ancient Text Recovery**.

### ▶️ Execution

Ejecuta el programa con Python 3 y el archivo de prueba, siguiendo la interfaz del subject. Si es necesario, pide al alumno que muestre cómo seleccionar el archivo que se va a leer.

### 🔍 Functionality

- El programa abre el archivo mediante **`open()`**.
- Lee **todo el contenido** utilizando **`read()`**.
- Muestra correctamente el contenido mediante **`print()`**.
- Cierra explícitamente el archivo mediante **`close()`**.
- Funciona con distintos contenidos de archivo.
- Gestiona correctamente los errores al llamar a `open()`.
- Se comprueba la apertura de un archivo inexistente y de un archivo inaccesible.
- Los errores de apertura no provocan una terminación inesperada del programa.
- La salida corresponde al archivo leído; no es un contenido fijo simulado.

### 🧪 Tests

| Prueba | Esperado |
|---|---|
| Leer un archivo con una línea de contenido conocido | Se muestra el contenido correcto |
| Leer un archivo con varias líneas | Se recupera y muestra todo el contenido |
| Repetir con otro contenido | La salida refleja el nuevo archivo |
| Indicar una ruta inexistente | El error de apertura se gestiona correctamente |
| Indicar un archivo sin permisos de lectura para el usuario de ejecución | El error de acceso se gestiona correctamente |
| Inspeccionar el flujo de lectura correcto | Se utilizan `open()`, `read()`, `print()` y `close()` |

### 🧹 Code Quality — Exercise 0

- El modo de apertura es apropiado para leer el archivo.
- La llamada a `read()` recupera el contenido completo solicitado.
- El cierre se realiza correctamente después de utilizar el archivo.
- La gestión de una apertura fallida no intenta utilizar un archivo que no llegó a abrirse.
- El alumno puede explicar por qué es necesario cerrar los archivos.

---
---

# ✍️ 2. Exercise 1 — Archive Creation

**Archivo:** el indicado en el subject para **Archive Creation**.

### ▶️ Execution

Ejecuta el programa proporcionando el archivo de entrada como parámetro, según la interfaz del subject. Cuando solicite un nombre nuevo, indica un archivo de salida de prueba. Repite después con un destino que ya exista.

### 🔍 Functionality

- Abre, lee, muestra y cierra el archivo recibido como parámetro, cumpliendo la tarea del ejercicio anterior.
- Actualiza el contenido añadiendo el carácter **`#` al final de cada línea**.
- Vuelve a mostrar el contenido actualizado.
- Solicita un nombre para el nuevo archivo.
- Abre el archivo de destino para escritura y lo crea si no existe.
- Escribe el contenido actualizado mediante **`write()`**.
- Cierra correctamente el archivo de salida.
- El archivo creado contiene el contenido esperado.
- Si el archivo de destino ya existe, el programa lo sobrescribe.
- El alumno entiende que el modo **`w` puede sobrescribir datos existentes**.

### 🧪 Read, Transform & Write Tests

| Prueba | Esperado |
|---|---|
| Proporcionar un archivo de entrada válido | Se lee y muestra su contenido original |
| Usar una línea con el texto `Ancient record` | La línea actualizada contiene `Ancient record#` |
| Usar varias líneas | Cada línea recibe su propio `#` al final |
| Comprobar la segunda visualización | Muestra el contenido actualizado |
| Elegir un nombre de destino que no exista | Se crea el archivo y se escribe el contenido esperado |
| Abrir el archivo generado tras finalizar el programa | Su contenido coincide con el texto actualizado |
| Elegir un destino existente con contenido previo distinto | Se reemplaza el contenido anterior; no se añade al final |
| Sobrescribir un archivo previo más largo con un resultado más corto | No quedan restos del contenido anterior |

### 🔎 Content & File Mode Validation

- El carácter `#` se añade al final del texto de cada línea, antes de su salto de línea cuando lo haya.
- No se añade únicamente un `#` al final del archivo completo si contiene varias líneas.
- La salida mostrada y el contenido escrito corresponden a la misma transformación.
- Se utiliza realmente `write()` para guardar el resultado.
- La apertura de salida utiliza el modo de escritura requerido.
- El alumno puede explicar la diferencia entre **crear**, **sobrescribir** y **añadir al final** de un archivo.

---
---

# 🔀 3. Exercise 2 — Stream Management

**Archivo:** el indicado en el subject para **Stream Management**.

### ▶️ Execution

Ejecuta el programa siguiendo la interfaz del subject y proporciona el nombre de salida mediante la entrada estándar. Repite un caso que provoque un error y separa la salida estándar de la salida de errores para comprobar dónde aparece el mensaje.

### 🔍 Functionality

- Cumple los requisitos de los ejercicios anteriores: lectura del archivo, actualización del contenido, solicitud del nuevo nombre y escritura en el archivo de destino.
- La transformación añade **`#` al final de cada línea**.
- Los archivos se cierran correctamente.
- Los mensajes de error se escriben en **`stderr`**.
- Los mensajes de error tienen un **prefijo claro**.
- Se comprueba en el código que los mensajes se envían realmente al flujo de errores.
- **No utiliza `input()`**.
- Lee la entrada directamente desde **`stdin`**, utilizando **`read()` o `readline()`**.
- Ambas alternativas de lectura están admitidas por la escala.

### 🧪 Streams Tests

| Caso | Esperado |
|---|---|
| Archivo de entrada válido y nombre de salida recibido por `stdin` | Se completa la lectura, transformación y escritura |
| Inspeccionar la lectura del nombre de salida | Utiliza `stdin.read()` o `stdin.readline()` |
| Revisar el código del ejercicio | No utiliza `input()` |
| Provocar un error de apertura | El mensaje aparece en `stderr` con un prefijo claro |
| Separar `stdout` y `stderr` durante la prueba | El mensaje de error se encuentra en la salida de errores |
| Leer el archivo de salida generado en una ejecución válida | Contiene la transformación esperada, con `#` al final de cada línea |
| Usar un archivo de destino ya existente | Se conserva el comportamiento de sobrescritura del ejercicio anterior |

### 🔎 Stream Validation

- El alumno distingue **`stdin`**, **`stdout`** y **`stderr`**.
- No basta con imprimir un texto que diga «error»: debe enviarse al flujo `stderr`.
- El prefijo permite reconocer claramente los mensajes de error; el PDF no exige un literal concreto.
- El nombre recibido por la entrada estándar se procesa de forma apropiada antes de abrir el destino.
- Si se utiliza `stdin.read()`, el alumno puede explicar cómo finaliza la lectura; si se utiliza `stdin.readline()`, puede explicar qué ocurre con el salto de línea recibido.
- Puede demostrar la separación de flujos mediante redirecciones, adaptando el comando a la interfaz real de su programa.

---
---

# 🔐 4. Exercise 3 — Vault Security

**Archivo:** el indicado en el subject para **Vault Security**.

### ▶️ Execution

Ejecuta las pruebas del programa que llaman a `secure_archive()`, incluyendo casos válidos e inválidos. Después, pide al alumno que realice la modificación de código solicitada para verificar el cierre automático de los archivos.

### 🔍 Functionality

- Existe una función llamada **`secure_archive()`**.
- **Todas las operaciones relacionadas con archivos** se gestionan mediante esa función.
- La función utiliza una sentencia **`with`** para gestionar los archivos.
- El programa llama a `secure_archive()` para probar múltiples casos.
- Las pruebas incluyen casos válidos e inválidos.
- Se muestran los resultados de las pruebas.
- La demostración permite comprobar el cierre automático de los archivos.

### 🧪 Secure Archive Tests

| Caso | Esperado |
|---|---|
| Localizar `secure_archive()` | La función existe y se utiliza |
| Revisar las operaciones de archivos | Están gestionadas por `secure_archive()` |
| Inspeccionar la gestión de los archivos | Se utiliza `with` |
| Ejecutar un caso válido | Se completa la operación y se muestra su resultado |
| Ejecutar un caso inválido adecuado a la operación del programa | El error se gestiona y se muestra el resultado correspondiente |
| Ejecutar varios casos válidos e inválidos | El programa demuestra ambos tipos de funcionamiento |
| Realizar la prueba de recodificación | Se comprueba de forma observable que los archivos se cierran automáticamente |

### ✍️ Recode by the Evaluated Learner

- Pide al alumno que actualice el código para verificar el cierre automático de los archivos, tal como solicita la parte visible de la escala.
- **El final de esa instrucción está recortado en el PDF.** Contrasta la condición exacta con la escala completa antes de utilizarla como criterio adicional de calificación.
- Como comprobación práctica propuesta, observa la propiedad **`closed`** del objeto archivo dentro y después del bloque `with`.
- Dentro del bloque, después de una apertura correcta, se espera `closed == False`.
- Después de salir del bloque, se espera `closed == True`.
- Como comprobación complementaria, puede provocarse una excepción controlada después de abrir el archivo, capturarla fuera del bloque y verificar que el archivo también queda cerrado.
- Un fallo en `open()` no demuestra el cierre de un archivo abierto: para esa comprobación debe haberse abierto correctamente primero.
- Verifica el estado real del objeto archivo; un mensaje fijo que afirme que está cerrado no es una prueba de cierre automático.

### 🧠 Concepts to check

- El alumno puede explicar qué aporta `with` frente a gestionar el cierre manualmente.
- Puede explicar cuándo se abandona el bloque y cómo se produce el cierre.
- Distingue entre una apertura fallida y un error ocurrido después de abrir el archivo.
- Puede mostrar qué operaciones se realizan dentro de `secure_archive()`.
- Puede explicar cómo la prueba de recodificación permite verificar el cierre automático.

---
---

# 🧹 5. Code Quality & Best Practices

## 🐍 Python

- El código está escrito para **Python 3.10 o superior**.
- El código cumple los estándares de **`flake8`**, sin errores.
- Todas las funciones y métodos tienen **type hints** y se revisan con **`mypy`**.
- **No se requieren docstrings para este módulo.**
- El código está bien estructurado y es legible.
- Los nombres de variables son significativos y descriptivos.
- La gestión de errores está implementada apropiadamente.

Desde la raíz de la entrega, comprueba el estilo y las anotaciones de tipo:

```bash
flake8 .
mypy --disallow-untyped-defs .
```

Si los ejercicios se organizan como programas independientes y el análisis conjunto produce conflictos entre módulos, ejecuta `mypy` por ejercicio siguiendo la estructura real del subject.

## 🧩 Files & Streams

- `open()` se utiliza con el modo adecuado para cada operación.
- `read()` recupera el contenido requerido y `print()` lo muestra correctamente.
- `write()` guarda realmente el contenido actualizado.
- `close()` se utiliza donde lo exige la escala en los primeros ejercicios.
- Se verifica la sobrescritura de archivos existentes con el modo `w`.
- Se añade `#` al final de cada línea en los ejercicios que requieren la transformación.
- En el ejercicio 2, los errores se envían a `stderr` con un prefijo claro.
- En el ejercicio 2, la entrada se lee desde `stdin` mediante `read()` o `readline()`, sin `input()`.
- En el ejercicio 3, `secure_archive()` gestiona las operaciones de archivos mediante `with`.
- Las demostraciones permiten comprobar el contenido de los archivos y el cierre de los recursos.

## 🧠 Understanding & Learning

- El alumno puede explicar las decisiones principales de su código.
- Distingue entre leer un archivo, transformar su contenido y escribir el resultado.
- Entiende que abrir un archivo existente con `w` puede eliminar su contenido anterior.
- Distingue los tres flujos estándar y puede justificar el uso de `stderr` para los errores.
- Entiende la diferencia entre cierre explícito y cierre automático mediante `with`.
- Puede explicar cómo se gestionan los errores de apertura y de acceso.
- Puede demostrar que los resultados proceden de operaciones reales sobre los archivos de prueba.

---
---

# 🚩 6. Defense

## 💬 Questions

1. ¿Qué devuelve `open()` y cómo eliges el modo de apertura?
2. ¿Qué hace `read()` cuando se utiliza sin indicar un tamaño?
3. ¿Por qué es necesario cerrar un archivo después de utilizarlo?
4. ¿Qué ocurre si el archivo no existe o el usuario de ejecución no tiene permiso para leerlo?
5. ¿Cómo añades `#` al final de cada línea sin colocarlo después del salto de línea?
6. ¿Qué diferencia hay entre los modos `w` y `a`?
7. ¿Qué ocurre al abrir con `w` un archivo que ya contiene datos?
8. ¿Cómo compruebas que el archivo generado contiene exactamente la transformación esperada?
9. ¿Qué diferencias hay entre `stdin`, `stdout` y `stderr`?
10. ¿Cómo demostrarías que un mensaje de error se envía realmente a `stderr`?
11. ¿Cómo lees el nombre de salida sin utilizar `input()`?
12. ¿Qué diferencia hay entre leer desde `stdin` con `read()` y con `readline()`?
13. ¿Qué operaciones de archivos gestiona `secure_archive()`?
14. ¿Qué aporta `with` a la gestión de los archivos?
15. ¿Cómo puedes comprobar que un archivo está cerrado después de salir de `with`?
16. ¿Por qué un fallo de apertura no sirve para demostrar el cierre automático de un archivo que llegó a abrirse?

## ⚠️ Stop conditions

Si se detecta una condición que obliga a finalizar la evaluación, utiliza la flag correspondiente.

- **Empty work →** El trabajo es inexistente.
- **Incomplete work →** El trabajo está incompleto.
- **Invalid compilation →** El código no puede compilarse o interpretarse correctamente.
- **Norme →** Incumplimiento de la norma aplicable.
- **Cheat →** Trampa o uso de elementos no autorizados.
- **Crash →** Terminación inesperada, prematura o no controlada del programa.
- **Concerning situation →** Situación preocupante.
- **Leaks →** Fugas de memoria.
- **Forbidden function →** Uso de una función no autorizada.
- **Can't support / explain code →** El alumno no puede defender o explicar su código.

La escala indica que la revisión se detiene si el repositorio contiene archivos distintos de los solicitados. Los errores de apertura correctamente gestionados son parte de las pruebas y no constituyen por sí mismos un crash. La incapacidad de explicar el código no demuestra por sí sola que exista plagio.

## 📝 Evaluation conclusion

- Revisa la valoración final: **Ok**, **Outstanding project** o la flag de incidencia correspondiente.
- Deja un comentario constructivo con los resultados de la evaluación y los problemas encontrados.
- El comentario final de la escala admite un máximo de **2048 caracteres**.
