# 🚀 Python Module 03

## 📌 0. Guidelines

### ⚠️ Rules

- La revisión se realiza junto al alumno evaluado, manteniendo una actitud respetuosa y constructiva.
- Se comprueba que el repositorio pertenece al alumno y corresponde al proyecto correcto. Se evalúa únicamente el contenido de su **repositorio Git**.
- Se comprueba que `git clone` se ejecuta en una carpeta vacía.
- Si el repositorio está vacío, la evaluación termina utilizando **Empty work**.
- No se utilizan alias ni scripts maliciosos que alteren el contenido evaluado.
- El evaluador y el evaluado revisan los scripts utilizados para facilitar la evaluación.
- Si el evaluador no ha realizado el proyecto, debe leer previamente el **subject completo**.
- Los ejercicios se evalúan **en el orden del subject**.
- Se comentan los problemas encontrados y se tienen en cuenta posibles diferencias de interpretación del enunciado.
- No debería ser necesario modificar archivos, salvo el de configuración si existe. Cualquier modificación debe explicarse y acordarse previamente con el evaluado.
- Ante una condición de parada contemplada por la escala, se utiliza la flag correspondiente: la evaluación termina con **0**, o **-42 en caso de trampas**.
- No se permite una terminación inesperada, prematura o no controlada del programa. Si ocurre, se aplica la flag correspondiente y la nota final es **0**.
- Salvo en caso de trampas, se puede continuar comentando el trabajo después de finalizar la calificación para identificar errores y aprender de ellos.

### 📁 Structure

- Se comprueba que la estructura del proyecto coincide con el subject y que en la raíz solo están los archivos solicitados.
- Se verifica la existencia de los siguientes archivos en sus ubicaciones correspondientes:
  - `ft_command_quest.py`
  - `ft_score_analytics.py`
  - `ft_coordinate_system.py`
  - `ft_achievement_tracker.py`
  - `ft_inventory_system.py`
  - `ft_data_stream.py`
  - `ft_data_alchemist.py`
- Si faltan entregables obligatorios, se utiliza **Incomplete work**.

> La escala adjunta enumera los nombres de archivo, pero no detalla las carpetas de entrega. Los comandos de esta guía se ejecutan desde la carpeta que contiene cada archivo; comprueba las rutas exactas en el subject.

### 🧰 General Concepts to Check

- El código se ejecuta y demuestra los conceptos requeridos en cada ejercicio.
- Se prueban entradas válidas e inválidas cuando corresponde.
- Se utiliza `sys.argv` para procesar los argumentos de línea de comandos.
- Las listas, tuplas, conjuntos y diccionarios se utilizan correctamente.
- Los generadores utilizan `yield` y producen elementos de forma incremental.
- Las comprensiones realizan las transformaciones y filtrados solicitados.
- El alumno puede explicar las operaciones y estructuras de datos utilizadas.

> **Fuente:** `PyMod03Eval.pdf`, páginas 1–4. Las tablas concretan pruebas para comprobar los criterios de la escala; no añaden requisitos al subject. Algunas líneas del PDF están recortadas por el margen derecho, especialmente en los ejercicios 5 y 6. Los detalles no legibles se señalan donde corresponde.

---
---

# 🖥️ 1. Exercise 0 — Command Quest

**Archivo:** `ft_command_quest.py`

### ▶️ Execution

```bash
python3 ft_command_quest.py
python3 ft_command_quest.py hello world 42
python3 ft_command_quest.py "Data Quest"
```

### 🔍 Functionality

- El programa accede correctamente a `sys.argv`.
- Muestra el nombre del programa mediante `sys.argv[0]`.
- Cuenta y muestra el número total de argumentos, distinguiendo el nombre del programa de los argumentos proporcionados por el usuario.
- Gestiona el caso en el que no se proporcionan argumentos.
- Muestra cada argumento individualmente cuando existen argumentos de usuario.
- El nombre del programa no se vuelve a mostrar como si fuera un argumento de usuario.

### 🧪 Tests

| Prueba | Esperado |
|---|---|
| Sin argumentos | Muestra el nombre del programa y gestiona la ausencia de argumentos de usuario |
| `hello world 42` | Muestra los tres argumentos de usuario por separado |
| `"Data Quest"` | Trata el texto entre comillas como un único argumento de usuario |
| Recuento con `hello world 42` | Distingue los 3 argumentos de usuario de las 4 entradas de `sys.argv` |
| Listado de argumentos | Excluye el nombre del programa del listado de argumentos de usuario |

### 🧠 Concepts to Check

- ¿Qué contiene `sys.argv`?
- ¿Qué representa `sys.argv[0]`?
- ¿Qué estrategia se utiliza para excluir el nombre del programa al mostrar los argumentos?
- ¿Qué alternativas existen a esa estrategia?
- ¿Por qué `"Data Quest"` llega como un solo argumento?

---
---

# 📊 2. Exercise 1 — Score Cruncher

**Archivo:** `ft_score_analytics.py`

### ▶️ Execution

```bash
python3 ft_score_analytics.py 100 250 180 90 300
python3 ft_score_analytics.py 100 abc 200
python3 ft_score_analytics.py
```

### 🔍 Functionality

- El programa acepta puntuaciones de jugadores como argumentos de línea de comandos.
- Convierte y procesa correctamente una lista de puntuaciones.
- Gestiona los argumentos no numéricos de forma controlada.
- Gestiona la ausencia de puntuaciones válidas que procesar.
- Muestra el total, la media, la puntuación máxima, la mínima y el rango.
- Los resultados corresponden a las puntuaciones realmente procesadas.

### 🧪 Tests

| Prueba | Esperado |
|---|---|
| `100 250 180 90 300` | Procesa 5 puntuaciones |
| Total de las puntuaciones anteriores | `920` |
| Media | `184` |
| Máximo y mínimo | Máximo `300`; mínimo `90` |
| Rango | `210`, calculado como máximo menos mínimo |
| `100 abc 200` | Gestiona el argumento no numérico sin una terminación no controlada |
| Sin argumentos | Gestiona la ausencia de puntuaciones |
| Solo una entrada no numérica, como `abc` | Gestiona que no haya ninguna puntuación válida |

> La escala exige gestionar las entradas inválidas, pero no concreta aquí si deben descartarse o rechazarse todos los datos. Comprueba la política exigida por el subject antes de penalizar una de estas alternativas.

### 🧹 Code Quality — Exercise 1

- La conversión de argumentos y el cálculo de estadísticas están organizados de forma legible.
- No se calculan medias ni extremos sobre una colección vacía sin gestionarlo previamente.
- Los mensajes de error permiten identificar el problema.
- El alumno puede explicar cómo obtiene cada estadística.

---
---

# 📍 3. Exercise 2 — Position Tracker

**Archivo:** `ft_coordinate_system.py`

### ▶️ Execution

```bash
python3 ft_coordinate_system.py
```

Introduce las coordenadas utilizando el mecanismo y formato previstos por el programa y el subject.

### 🔍 Functionality

- El programa solicita coordenadas y gestiona entradas inválidas.
- Crea y manipula coordenadas tridimensionales mediante tuplas **`(x, y, z)`**.
- Demuestra el acceso a los componentes mediante índices, como `coordinate[0]`, o mediante desempaquetado, como `x, y, z = coordinate`, tal como admite la escala.
- Calcula correctamente distancias euclídeas entre coordenadas 3D.
- La gestión de coordenadas inválidas no provoca una terminación no controlada.

### 🧪 Tests

| Prueba | Esperado |
|---|---|
| Crear una coordenada `(3, 4, 0)` | Se representa mediante una tupla con tres componentes |
| Acceder o desempaquetar `(3, 4, 0)` | Se obtienen `x = 3`, `y = 4`, `z = 0` |
| Distancia entre `(0, 0, 0)` y `(3, 4, 0)` | `5` |
| Distancia entre `(0, 0, 0)` y `(1, 2, 2)` | `3`; intervienen las tres dimensiones |
| Distancia de una coordenada a sí misma | `0` |
| Coordenada con un componente no numérico | Entrada inválida gestionada correctamente |
| Cantidad incorrecta de componentes | Entrada inválida gestionada correctamente |

### 🧠 Concepts to Check

- ¿Qué diferencia hay entre una tupla y una lista?
- ¿Qué significa desempaquetar una tupla?
- ¿Qué ocurre si el número de variables no coincide con el número de elementos al desempaquetar?
- ¿Cómo se aplica la fórmula de distancia euclídea en tres dimensiones?

```text
distancia = sqrt((x2 - x1)² + (y2 - y1)² + (z2 - z1)²)
```

---
---

# 🏆 4. Exercise 3 — Achievement Hunter

**Archivo:** `ft_achievement_tracker.py`

### ▶️ Execution

```bash
python3 ft_achievement_tracker.py
python3 ft_achievement_tracker.py
python3 ft_achievement_tracker.py
```

### 🔍 Functionality

- La función `gen_player()` crea y devuelve un **conjunto de logros aleatorios**.
- El programa obtiene los logros de todos los jugadores mediante **unión**.
- Obtiene los logros comunes entre jugadores mediante **intersección**.
- Identifica los logros exclusivos de cada jugador mediante **diferencia**.
- Informa de los logros que le faltan a cada jugador mediante **diferencia**, tomando como referencia el conjunto de logros que corresponda según el subject.
- Se ejecuta el programa varias veces para comprobar la generación aleatoria.

### 🧪 Set Operations Tests

Los siguientes conjuntos son ejemplos de comprobación de las operaciones; no sustituyen la generación aleatoria requerida.

| Prueba | Esperado |
|---|---|
| Llamar a `gen_player()` | Devuelve un `set` de logros |
| Unión de `{'a', 'b'}` y `{'b', 'c'}` | `{'a', 'b', 'c'}` |
| Intersección de esos conjuntos | `{'b'}` |
| Diferencia del primer conjunto respecto al segundo | `{'a'}` |
| Diferencia del segundo conjunto respecto al primero | `{'c'}` |
| Logros de referencia `{'a', 'b', 'c'}` y jugador con `{'a'}` | Le faltan `{'b', 'c'}` |
| Varias ejecuciones | La implementación genera logros aleatoriamente; una repetición aislada no demuestra un fallo |

### 🧠 Concepts to Check

- El alumno explica la unión, la intersección y la diferencia, y sus casos de uso.
- Entiende por qué los conjuntos eliminan duplicados.
- Puede explicar por qué `A - B` y `B - A` no tienen por qué coincidir.
- Distingue los logros exclusivos de un jugador de los logros que todavía no posee.
- No se exige un orden fijo al imprimir los elementos de un conjunto.

---
---

# 🎒 5. Exercise 4 — Inventory Master

**Archivo:** `ft_inventory_system.py`

### ▶️ Execution

```bash
python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3
python3 ft_inventory_system.py
python3 ft_inventory_system.py sword
python3 ft_inventory_system.py potion:abc
```

### 🔍 Functionality

- El programa acepta argumentos con formato **`item:quantity`**.
- Gestiona los parámetros inválidos correctamente.
- Almacena el inventario en un diccionario con nombres de objetos como claves y cantidades como valores.
- Muestra los nombres de los objetos sin sus cantidades.
- Calcula estadísticas de inventario: número de objetos distintos, cantidad total, porcentajes y objetos más y menos abundantes.
- Utiliza `keys()`, `values()` y `update()`, o soluciones alternativas válidas, tal como permite la escala.
- Sin argumentos, muestra un mensaje de uso.

### 🧪 Dictionary & Inventory Tests

| Prueba | Esperado |
|---|---|
| `sword:1 potion:5 shield:2 armor:3` | Diccionario con cuatro claves y sus cantidades correspondientes |
| Número de objetos distintos | `4` |
| Cantidad total | `11` |
| Objeto más abundante | `potion`, con `5` unidades |
| Objeto menos abundante | `sword`, con `1` unidad |
| Porcentajes sobre la cantidad total | `sword ≈ 9,09 %`, `potion ≈ 45,45 %`, `shield ≈ 18,18 %`, `armor ≈ 27,27 %` |
| Listado de nombres | Muestra `sword`, `potion`, `shield` y `armor` sin cantidades en ese listado |
| Sin argumentos | Muestra un mensaje de uso |
| Formato inválido: `sword` | Error gestionado correctamente |
| Cantidad no numérica: `potion:abc` | Error gestionado correctamente |

### 🧠 Concepts to Check

- ¿Qué representan las claves y los valores del diccionario?
- ¿Qué devuelven `keys()` y `values()`?
- ¿Cómo funciona `update()` y qué ocurre cuando una clave ya existe?
- ¿Cómo se obtiene el total de unidades y cómo se diferencia del número de claves?
- ¿Cómo se calculan los porcentajes y los objetos más y menos abundantes?

---
---

# 🌊 6. Exercise 5 — Stream Wizard

**Archivo:** `ft_data_stream.py`

### ▶️ Execution

```bash
python3 ft_data_stream.py
```

### 🔍 Functionality

- Se define la función generadora **`gen_event()`**, que utiliza `yield` para producir eventos representados mediante tuplas.
- Se utiliza `next()` para obtener el siguiente evento dentro de un bucle `for` de **1000 iteraciones**.
- Se imprimen los **1000 eventos**.
- No se crea una lista ni otra estructura que almacene los **1000 eventos**.
- A continuación, se construye una lista de **10 tuplas** generadas mediante `gen_event()`.
- Se define la función generadora **`consume_event()`**, que utiliza `yield` para entregar elementos restantes de esa lista y los elimina al consumirlos.
- El generador obtenido al llamar a `consume_event()` se asigna a una variable y se recorre mediante una construcción como **`for e in consume_ev:`**.

> El margen derecho del PDF recorta parte de las indicaciones sobre el evento, la selección de elementos y el bucle de consumo. Confirma esos detalles en el subject; esta guía recoge únicamente el comportamiento legible.

### 🧪 Generator & Consumption Tests

| Prueba | Esperado |
|---|---|
| Inspeccionar `gen_event()` | Utiliza `yield` para generar eventos |
| Obtener el siguiente evento con `next()` | Devuelve una tupla de evento |
| Primera fase de procesamiento | Ejecuta 1000 iteraciones e imprime 1000 eventos |
| Inspeccionar el almacenamiento de la primera fase | No acumula los 1000 eventos en una colección |
| Crear la lista posterior | Contiene 10 tuplas producidas por `gen_event()` |
| Inspeccionar `consume_event()` | Utiliza `yield` y elimina de la lista los elementos que entrega |
| Recorrer el generador de consumo hasta agotarlo | Consume los 10 elementos y la lista termina vacía |
| Uso del generador de consumo | Se recorre con `for e in consume_ev:` o la construcción equivalente exigida por el subject |

### 🧠 Concepts to Check

- ¿Qué diferencia hay entre una función que utiliza `return` y una función generadora que utiliza `yield`?
- ¿Qué ocurre al llamar a una función generadora?
- ¿Qué hace `next()`?
- ¿Qué estado conserva el generador entre dos iteraciones?
- ¿Por qué producir elementos de uno en uno puede ahorrar memoria?
- ¿Por qué guardar todos los elementos generados en una lista eliminaría esa ventaja en la primera fase?
- ¿Cómo se coordina la entrega de cada elemento con su eliminación de la lista?

---
---

# ⚗️ 7. Exercise 6 — Data Alchemist

**Archivo:** `ft_data_alchemist.py`

### ▶️ Execution

```bash
python3 ft_data_alchemist.py
python3 ft_data_alchemist.py
python3 ft_data_alchemist.py
```

### 🔍 Functionality

- El programa crea y muestra una lista de nombres.
- Utiliza una **list comprehension** para obtener la lista con todos los nombres capitalizados.
- Utiliza otra **list comprehension** para obtener la sublista de nombres ya capitalizados, conforme al criterio del subject.
- Crea un diccionario mediante una **dict comprehension**, basado en los nombres anteriores y sus puntuaciones.
- Utiliza otra **dict comprehension** para obtener el diccionario de puntuaciones altas.
- Al ejecutar varias veces el programa, se comprueba la variación de las puntuaciones.
- Se comprueba que el comportamiento se adapta al cambiar la lista de jugadores, explicando y acordando previamente cualquier modificación del archivo con el evaluado.

> El PDF recorta el final de las líneas sobre la sublista de nombres y el diccionario inicial. Tampoco permite establecer aquí el rango de puntuaciones ni el umbral de puntuación alta: compruébalos en el subject. Aunque la introducción del ejercicio menciona «todos los tipos de comprensiones», los puntos legibles solo concretan listas y diccionarios; no se añade una comprensión de conjuntos como requisito sin confirmarlo.

### 🧪 Comprehension Tests

| Prueba | Esperado |
|---|---|
| Lista inicial de nombres | Se crea y se muestra |
| Comprensión de capitalización | Genera una lista con todos los nombres capitalizados según el subject |
| Comprensión de filtrado de nombres | Incluye únicamente los nombres que cumplen el criterio requerido |
| Diccionario inicial | Se construye mediante una comprensión y relaciona los nombres con sus puntuaciones |
| Diccionario de puntuaciones altas | Se construye mediante otra comprensión y conserva solo las entradas que cumplen el umbral del subject |
| Varias ejecuciones | Permiten comprobar la generación de puntuaciones distintas; no se exige que todas las ejecuciones difieran |
| Cambiar la lista de jugadores de forma acordada | Las listas y los diccionarios resultantes se adaptan a los nuevos datos |

### 🧠 Concepts to Check

- ¿Qué diferencia hay entre transformar y filtrar elementos mediante una comprensión?
- ¿Qué partes forman una list comprehension?
- ¿Cómo se definen las claves y los valores en una dict comprehension?
- ¿De qué diccionario parte el filtrado de puntuaciones altas?
- ¿Cómo afectan los cambios en la lista de jugadores a las estructuras derivadas?

---
---

# 🧹 8. Code Quality & Best Practices

## 🐍 Python

- El código está escrito para **Python 3.10 o superior**.
- El código cumple los estándares de **flake8**, sin errores.
- Todas las funciones y métodos tienen **type hints** para parámetros y valores de retorno; se comprueban con **mypy**.
- **No se requieren docstrings** para este módulo.
- El código está bien estructurado y es legible.
- La gestión de errores es apropiada.

## 🧩 Data Structures & Processing

- Los argumentos de línea de comandos se procesan de acuerdo con cada ejercicio.
- Las listas permiten procesar las puntuaciones y calcular sus estadísticas.
- Las tuplas representan coordenadas 3D y eventos donde se requieren.
- Los conjuntos resuelven las operaciones sobre logros.
- Los diccionarios relacionan objetos con cantidades y jugadores con puntuaciones.
- Los generadores producen y consumen elementos respetando los requisitos del ejercicio 5.
- Las comprensiones realizan las transformaciones y filtrados del ejercicio 6.

## 🧠 Understanding & Learning

- El alumno puede explicar las decisiones principales de su código.
- Entiende las diferencias entre listas, tuplas, conjuntos y diccionarios.
- Puede explicar los cálculos y operaciones utilizados.
- Comprende cómo funcionan los generadores y por qué pueden reducir el uso de memoria.
- Puede explicar la sintaxis y el comportamiento de las comprensiones.
- Puede razonar sobre el comportamiento ante las entradas inválidas contempladas por la escala.

---
---

# 🚩 9. Defense

## 💬 Questions

1. ¿Qué contiene `sys.argv` y cómo evitas incluir el nombre del programa entre los argumentos de usuario?
2. ¿Cómo conviertes las puntuaciones recibidas por terminal y gestionas un argumento no numérico?
3. ¿Qué haces si no hay ninguna puntuación válida para calcular estadísticas?
4. ¿Qué es una tupla y cómo accedes a sus componentes o la desempaquetas?
5. ¿Cómo calculas la distancia euclídea entre dos puntos tridimensionales?
6. ¿Qué diferencias hay entre unión, intersección y diferencia de conjuntos? Pon un caso de uso de cada operación.
7. ¿Cómo distingues los logros exclusivos de un jugador de los que le faltan?
8. ¿Cómo funcionan `keys()`, `values()` y `update()` en un diccionario?
9. ¿Qué diferencia hay entre el número de objetos distintos del inventario y la cantidad total de unidades?
10. ¿Qué hace `yield` y qué sucede cuando se llama a `next()` sobre un generador?
11. ¿Por qué el procesamiento de 1000 eventos del ejercicio 5 no necesita almacenarlos todos?
12. ¿Cómo consume y elimina elementos `consume_event()`?
13. ¿Cómo se transforma una lista y cómo se filtra mediante comprensiones?
14. ¿Cómo construyes el diccionario de puntuaciones altas a partir de los datos anteriores?

## ⚠️ Stop Conditions

Cuando se detecta una condición de parada, se utiliza la flag correspondiente de la escala. Según las Guidelines del PDF, la nota final es **0**, o **-42 en caso de trampas**.

- **Empty work** → Repositorio sin trabajo evaluable.
- **Incomplete work** → Entrega incompleta.
- **Invalid compilation** → El programa no puede ejecutarse correctamente por errores que impiden su puesta en funcionamiento.
- **Norme** → Incumplimiento de las normas exigidas.
- **Cheat** → Trampas o uso de elementos no autorizados.
- **Concerning situation** → Situación preocupante que requiere señalarse en la evaluación.
- **Leaks** → Fugas de memoria, cuando corresponda aplicar esta flag.
- **Forbidden function** → Uso de una función no autorizada.
- **Can't support / explain code** → El alumno no puede defender o explicar su código.

> La escala prohíbe las terminaciones inesperadas, prematuras o no controladas y exige aplicar la flag apropiada. No se distingue una flag específica llamada `Crash` en el listado visible del PDF.

## 📝 Evaluation Comment

- Selecciona la calificación o flag que corresponda a la defensa.
- Deja un comentario constructivo con las pruebas realizadas, los problemas encontrados y las explicaciones relevantes del alumno.
- El comentario final de la plataforma tiene un límite de **2048 caracteres**.
