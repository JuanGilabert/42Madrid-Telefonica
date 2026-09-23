# 🧙‍♂️ Python Module 10 — Evaluation Rubric

## 📌 0. Guidelines

### General rules

- La evaluación debe realizarse de forma respetuosa, constructiva y colaborativa.
- La revisión se realiza en presencia del estudiante evaluado.
- Solo se debe evaluar el contenido existente en el repositorio Git oficial del estudiante.
- Verificar que el repositorio pertenece al estudiante o grupo evaluado.
- Realizar el `git clone` en una carpeta vacía.
- Comprobar que no existen alias maliciosos ni mecanismos destinados a ocultar o sustituir el contenido real del repositorio.
- Si el estudiante evaluador todavía no ha realizado este módulo, debe leer el enunciado completo antes de comenzar la defensa.
- No se deben modificar archivos durante la evaluación, salvo que el enunciado permita modificar un archivo de configuración. Cualquier modificación debe explicarse y acordarse con el estudiante.
- Deben comprobarse escenarios válidos e inválidos.
- Si un ejercicio no funciona, la evaluación se detiene y los ejercicios posteriores no se califican.
- Si durante la defensa se produce una terminación inesperada, prematura o no controlada del programa, la evaluación debe detenerse y aplicarse el flag correspondiente.

### Requisitos preliminares

Comprobar que existen los siguientes archivos:

```text
ex0/lambda_spells.py
ex1/higher_magic.py
ex2/scope_mysteries.py
ex3/functools_artifacts.py
ex4/decorator_mastery.py
```

Además:

- El código debe ejecutarse sin errores.
- Las dependencias deben instalarse mediante una gestión adecuada de paquetes y dentro de un entorno virtual.
- No se deben utilizar variables globales.
- No se deben utilizar operaciones de entrada/salida de archivos.
- Se debe verificar el uso real de las herramientas y patrones funcionales solicitados, evitando implementaciones manuales que sustituyan a `lambda`, `functools` u otras funciones requeridas.

---

## 📁 Structure

```text
.
├── ex0/
│   └── lambda_spells.py
├── ex1/
│   └── higher_magic.py
├── ex2/
│   └── scope_mysteries.py
├── ex3/
│   └── functools_artifacts.py
└── ex4/
    └── decorator_mastery.py
```

---

# 🪄 Exercise 0 — Lambda Sanctum

## Required file

```text
ex0/lambda_spells.py
```

## Functionality

### `artifact_sorter()`

- Debe utilizar `sorted()`.
- Debe utilizar una expresión `lambda` como clave de ordenación.
- Debe ordenar los artefactos por `power` en orden descendente.

### `power_filter()`

- Debe utilizar `filter()`.
- Debe utilizar una expresión `lambda`.
- Debe conservar los magos cuyo poder sea igual o superior al mínimo indicado.

### `spell_transformer()`

- Debe utilizar `map()`.
- Debe utilizar una expresión `lambda`.
- Debe añadir el prefijo y el sufijo `*` a los hechizos.

### `mage_stats()`

- Debe utilizar funciones `lambda` junto con `max()` y `min()`.
- Debe calcular correctamente las estadísticas solicitadas, incluyendo máximo, mínimo y promedio.

## Tests

| Test | Resultado esperado |
|---|---|
| Ordenación de artefactos | Los artefactos aparecen por `power` descendente |
| Filtrado con mínimo bajo | Se incluyen todos los magos que cumplen el umbral |
| Filtrado con mínimo alto | Solo se incluyen los magos suficientemente poderosos |
| Transformación de hechizos | Cada hechizo recibe la decoración `*` correcta |
| Estadísticas | Máximo, mínimo y promedio correctos |
| Uso de lambda | Se utilizan `lambda` en operaciones simples, no funciones `def` innecesarias |

Se puede utilizar `data_generator.py`, incluido en los materiales, para generar datos de prueba.

## Concepts to check

- Diferencia entre `lambda` y `def`.
- Cuándo resulta apropiado utilizar una función anónima.
- Diferencia entre `sorted()`, `filter()` y `map()`.
- Evaluación perezosa de `filter()` y `map()`.
- Uso de funciones como argumentos.

**Si todos los tests funcionan correctamente, marcar “Yes”. En caso contrario, marcar “No” y detener la evaluación.**

---

# 🧠 Exercise 1 — Higher Realm

## Required file

```text
ex1/higher_magic.py
```

## Functionality

### `spell_combiner()`

- Debe devolver una función.
- La función devuelta debe ejecutar las dos funciones recibidas.
- Debe combinar correctamente sus resultados.

### `power_amplifier()`

- Debe devolver una función.
- La función devuelta debe multiplicar el resultado del hechizo base por el multiplicador indicado.

### `conditional_caster()`

- Debe devolver una función.
- La función devuelta debe comprobar una condición antes de ejecutar el hechizo.
- Debe comportarse correctamente tanto cuando la condición es verdadera como cuando es falsa.

### `spell_sequence()`

- Debe devolver una función.
- La función devuelta debe ejecutar todos los hechizos en el orden recibido.
- Debe devolver una lista con los resultados correspondientes.

## Tests

| Test | Resultado esperado |
|---|---|
| Combinación de hechizos | Se ejecutan ambas funciones y se combinan sus resultados |
| Amplificación con multiplicador 1 | El resultado permanece igual |
| Amplificación con distintos multiplicadores | El resultado se multiplica correctamente |
| Condición verdadera | El hechizo se ejecuta |
| Condición falsa | El hechizo no se ejecuta o devuelve el resultado previsto por el enunciado |
| Secuencia de hechizos | Todos se ejecutan en el orden correcto |
| Funciones como valores | Las funciones se pasan como argumentos y se devuelven como resultados |

Se pueden generar datos de ejemplo para hechizos, objetivos y valores de poder.

## Concepts to check

- Funciones de orden superior.
- Funciones como ciudadanos de primera clase.
- Funciones que reciben otras funciones.
- Funciones que devuelven otras funciones.
- Cierres y estado capturado, cuando corresponda.

**Si todos los tests funcionan correctamente, marcar “Yes”. En caso contrario, marcar “No” y detener la evaluación.**

---

# 🔐 Exercise 2 — Memory Depths

## Required file

```text
ex2/scope_mysteries.py
```

## Functionality

### `mage_counter()`

- Debe devolver una función.
- La función devuelta debe mantener un contador entre llamadas.
- Cada contador creado debe conservar su propio estado independiente.

### `spell_accumulator()`

- Debe devolver una función que acumule poder entre llamadas.
- Debe respetar el poder inicial indicado.
- Debe actualizar y devolver correctamente el acumulado.

### `enchantment_factory()`

- Debe crear funciones que recuerden el tipo de encantamiento.
- Diferentes fábricas deben poder producir comportamientos independientes.
- El encantamiento debe aplicarse correctamente al objeto recibido.

### `memory_vault()`

- Debe devolver un diccionario con funciones de almacenamiento y recuperación.
- Las funciones deben compartir un almacenamiento privado.
- Debe ser posible guardar varios valores y recuperarlos posteriormente.

## Tests

| Test | Resultado esperado |
|---|---|
| Dos contadores independientes | Cada contador mantiene su propio estado |
| Contador repetido | El valor aumenta correctamente entre llamadas |
| Acumulador con valor inicial 0 | Las sumas sucesivas producen el total esperado |
| Acumulador con otro valor inicial | Se respeta el valor inicial |
| Fábricas de encantamientos distintas | Cada función recuerda su tipo de encantamiento |
| Aplicación repetida de un encantamiento | El resultado es coherente con el estado capturado |
| Memory vault | Se almacenan y recuperan todos los valores correctamente |
| Estado privado | El almacenamiento no se expone directamente |

## Restrictions

- No utilizar la palabra clave `global`.
- No crear clases.
- Deben utilizarse cierres y alcance léxico real.

## Concepts to check

- Alcance léxico.
- Cierres (`closures`).
- Captura de variables.
- Diferencia entre variables locales, no locales y globales.
- Persistencia del estado entre llamadas.
- Independencia entre distintos cierres.

Durante la defensa, pedir al estudiante que explique cómo se conserva el estado y qué ocurre en cada llamada.

**Si todos los tests funcionan correctamente, marcar “Yes”. En caso contrario, marcar “No” y detener la evaluación.**

---

# 📚 Exercise 3 — Ancient Library

## Required file

```text
ex3/functools_artifacts.py
```

## Functionality

### `spell_reducer()`

- Debe utilizar `functools.reduce`.
- Debe utilizar funciones del módulo `operator`.
- Para la operación `add`, debe utilizar `operator.add`.
- Para la operación `multiply`, debe utilizar `operator.mul`.
- Debe gestionar también las operaciones `min` y `max`.
- El estudiante debe poder explicar cómo se implementan esas operaciones y proponer otras soluciones posibles.

### `partial_enchanter()`

- Debe utilizar `functools.partial`.
- Debe crear funciones especializadas a partir de una función general.
- No debe sustituirse `partial` por lambdas u otras implementaciones manuales.
- El resultado asociado a `fire_enchant` debe ser realmente de tipo `functools.partial`.

### `memoized_fibonacci()`

- Debe utilizar `functools.lru_cache`.
- Debe memorizar los resultados de Fibonacci.
- Las llamadas repetidas deben beneficiarse de la caché.
- Tras llamar, por ejemplo, a `fib(10)`, `cache_info()` debe mostrar `hits > 0` cuando se repitan cálculos.

### `spell_dispatcher()`

- Debe utilizar `functools.singledispatch`.
- Debe realizar dispatch según el tipo del argumento.
- Debe comportarse correctamente con distintos tipos, incluyendo `float`.

## Tests

| Test | Resultado esperado |
|---|---|
| `reduce` con suma | Resultado correcto usando `operator.add` |
| `reduce` con multiplicación | Resultado correcto usando `operator.mul` |
| `reduce` con mínimo y máximo | Resultados correctos |
| `reduce` sobre lista vacía | El estudiante explica el comportamiento sin inicializador |
| Partial enchanter | Se crean funciones especializadas funcionales |
| Tipo de `fire_enchant` | Es `functools.partial` |
| Fibonacci repetido | Se observan hits en la caché |
| Dispatcher con varios tipos | Cada tipo utiliza el comportamiento adecuado |
| Dispatcher con `float` | Se gestiona según la implementación requerida |

## Concepts to check

- Funcionamiento de `functools.reduce`.
- Uso del módulo `operator`.
- Diferencia entre `partial` y una función nueva.
- Memoización frente a almacenamiento manual de resultados.
- Funcionamiento de `lru_cache`.
- Dispatch basado en tipos mediante `singledispatch`.

Preguntas sugeridas:

- ¿Qué ocurre al llamar a `reduce()` sobre una lista vacía sin inicializador?
- ¿Cuál es la diferencia entre memoización y guardar resultados en un diccionario global?

**Si todos los tests funcionan correctamente y se utilizan realmente las herramientas de `functools`, marcar “Yes”. En caso contrario, marcar “No” y detener la evaluación.**

---

# 🏰 Exercise 4 — Master's Tower

## Required file

```text
ex4/decorator_mastery.py
```

## Functionality

### `spell_timer()`

- Debe crear un decorador.
- El decorador debe medir el tiempo de ejecución de la función decorada.
- Debe mostrar o devolver la información de tiempo según lo solicitado.

### `power_validator()`

- Debe crear un decorador parametrizado.
- Debe validar el nivel de poder recibido.
- Debe funcionar correctamente con valores válidos e inválidos.

### `retry_spell()`

- Debe crear un decorador que reintente una función que falla.
- Debe respetar el número de reintentos configurado.
- Debe detenerse cuando la función tenga éxito o se agoten los intentos.

### `MageGuild`

- Debe utilizar correctamente `@staticmethod`.
- Sus métodos estáticos deben poder invocarse sin crear una instancia.

### `cast_spell()`

- Debe utilizar `power_validator` con `min_power=10`.
- Debe comportarse correctamente tanto con poder suficiente como insuficiente.

### `functools.wraps`

- Los decoradores deben utilizar `functools.wraps` para preservar los metadatos de las funciones decoradas.

## Tests

| Test | Resultado esperado |
|---|---|
| `spell_timer` | Se mide y muestra el tiempo de ejecución |
| `power_validator` válido | La función se ejecuta correctamente |
| `power_validator` inválido | La validación impide la ejecución o produce el error esperado |
| `retry_spell` con éxito inmediato | No realiza reintentos innecesarios |
| `retry_spell` con fallos y éxito posterior | Reintenta hasta conseguir éxito |
| `retry_spell` con fallo permanente | Se detiene tras agotar los intentos |
| `staticmethod` | Se invoca sin instancia |
| Nombres válidos e inválidos | `MageGuild` valida correctamente |
| `cast_spell` con poder suficiente | La operación tiene éxito |
| `cast_spell` con poder insuficiente | Se aplica la validación esperada |
| Metadatos | `functools.wraps` conserva nombre y documentación/metadatos disponibles |

## Concepts to check

- Qué es un decorador.
- Cómo transforma un decorador el comportamiento de una función.
- Diferencia entre decoradores simples y parametrizados.
- Funcionamiento de `staticmethod`.
- Necesidad de `functools.wraps`.
- Orden y composición de decoradores.
- Manejo de excepciones y reintentos.

**Si todos los tests funcionan correctamente, marcar “Yes”. En caso contrario, marcar “No” y detener la evaluación.**

---

# 🧪 Overall Code Quality & Understanding

## Functional programming understanding

Comprobar si el estudiante puede explicar:

- La diferencia entre `lambda` y `def`.
- Qué significa que las funciones sean ciudadanos de primera clase.
- Qué son las funciones de orden superior.
- Cómo funcionan los cierres y cómo capturan el alcance léxico.
- Qué ventajas ofrecen las utilidades de `functools`.
- Cómo funcionan `reduce`, `partial`, `lru_cache` y `singledispatch`.
- Cómo los decoradores transforman funciones.
- Por qué `functools.wraps` es importante.

## Code quality

- [ ] El código utiliza Python 3.10 o superior.
- [ ] El código cumple las normas de `flake8`, sin errores.
- [ ] Todas las funciones y métodos tienen type hints en parámetros y valores de retorno.
- [ ] Los docstrings no son obligatorios en este módulo.
- [ ] El código es limpio, legible y está bien estructurado.
- [ ] Los patrones funcionales se utilizan correctamente.
- [ ] No se utilizan variables globales.
- [ ] No se realizan operaciones de entrada/salida de archivos.
- [ ] Las dependencias se gestionan correctamente dentro de un entorno virtual.
- [ ] La solución demuestra comprensión real y no una simple copia.
- [ ] El estudiante puede explicar las decisiones principales de su implementación.

## Final understanding check

Pedir al estudiante que explique, con ejemplos de su código:

1. Cuándo utilizaría `lambda` y cuándo una función definida con `def`.
2. Cómo se mantiene el estado en un cierre.
3. Qué diferencia existe entre una función de orden superior y una función normal.
4. Por qué `lru_cache` puede mejorar Fibonacci.
5. Qué diferencia hay entre `partial` y crear una nueva función manualmente.
6. Cómo funciona `singledispatch`.
7. Qué sucede cuando se aplica un decorador a una función.
8. Por qué se debe utilizar `functools.wraps`.
9. Cómo se controlan los reintentos y las excepciones.
10. Qué problemas pueden aparecer si se utilizan variables globales para almacenar estado.

**Si el estudiante demuestra una buena comprensión de la programación funcional, marcar “Yes”. En caso contrario, marcar “No”.**

---

# 🚩 Stop Conditions / Flags

La evaluación debe detenerse y aplicarse el flag correspondiente cuando proceda:

- **Ok** — El proyecto cumple los requisitos y la defensa es satisfactoria.
- **Outstanding project** — Trabajo especialmente completo, sólido y bien explicado.
- **Empty work** — No hay trabajo entregado.
- **Incomplete work** — El trabajo está incompleto.
- **Invalid compilation / Crash** — El código no compila, no se ejecuta o termina de forma inesperada.
- **Norme** — Incumplimiento de las normas de estilo o requisitos formales.
- **Cheat** — Evidencias de copia, fraude o manipulación de la evaluación.
- **Concerning situation** — Situación preocupante que debe señalarse.
- **Leaks** — Uso o presencia de información filtrada.
- **Forbidden function** — Uso de funciones o mecanismos prohibidos.
- **Can’t support / explain code** — El estudiante no puede explicar o defender adecuadamente su código.

## Important

- Si no hay trabajo entregado, la nota es **0** y la evaluación termina.
- Si un ejercicio no funciona, la revisión se detiene y los ejercicios posteriores no se califican.
- En caso de cheating, la calificación puede ser **-42**.
- Si durante la defensa ocurre una terminación inesperada, prematura o no controlada, debe aplicarse el flag correspondiente.
