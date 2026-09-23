# 🚀 Python Module 07

## 📌 0. Guidelines

### ⚠️ Rules

- La revisión se realiza **en presencia del alumno evaluado**.
- Se debe mantener una actitud educada, respetuosa, constructiva y profesional durante toda la evaluación.
- La evaluación debe realizarse conjuntamente con el alumno, identificando, discutiendo y debatiendo los posibles problemas encontrados.
- Se debe tener en cuenta que puede haber distintas interpretaciones de las instrucciones del proyecto. La evaluación debe ser honesta y objetiva.
- Se evalúa únicamente el trabajo existente en el **repositorio Git del alumno**.
- Se debe comprobar que el repositorio pertenece al alumno o al grupo, que corresponde al proyecto correcto y que el comando `git clone` se ejecuta en una carpeta vacía.
- No se deben utilizar alias maliciosos ni mecanismos que alteren el contenido que se está evaluando.
- El evaluador y el evaluado deben revisar los posibles scripts utilizados para facilitar la evaluación.
- Si el evaluador todavía no ha realizado este proyecto, debe leer previamente el subject completo.
- Si se detecta un repositorio vacío, un programa que no funciona, un error de norma, cheating u otra condición invalidante, se debe utilizar la flag correspondiente y la evaluación termina con nota **0** —o **-42** en caso de cheating—.
- Salvo que exista un archivo de configuración, no se debe modificar ningún archivo durante la evaluación.
- Si fuera necesario modificar un archivo, se deben explicar previamente los motivos y obtener el acuerdo del alumno.
- No se permite ninguna terminación inesperada, prematura o incontrolada del programa durante la defensa. En ese caso, se debe utilizar la flag correspondiente.

### 📁 Structure

- La estructura debe corresponder a los requisitos del subject.
- Deben existir las carpetas:
  - `ex0/`
  - `ex1/`
  - `ex2/`
- Cada carpeta debe contener un archivo `__init__.py` y al menos otro archivo.
- Los nombres concretos de las clases, fábricas o criaturas pueden ser diferentes de los sugeridos en el subject, siempre que los patrones de diseño y la funcionalidad requerida estén correctamente implementados.

### 🧰 General concepts to check

- El código se ejecuta correctamente sin errores inesperados.
- Los patrones **Abstract Factory**, **Abstract Capabilities** y **Abstract Strategy** están correctamente implementados.
- Las clases abstractas utilizan `ABC` y métodos abstractos cuando corresponde.
- Las fábricas crean las criaturas adecuadas para cada familia.
- Las capacidades se aplican en el lugar correcto del flujo de ejecución.
- Las estrategias son compatibles con las criaturas y sus capacidades.
- Las funciones reciben los tipos de datos esperados y son reutilizables.
- Todas las funciones y métodos tienen **type hints**.
- El código es compatible con **Python 3.10 o superior**.
- El código cumple los estándares de `flake8`.
- Los `docstrings` no son obligatorios para este módulo.

---

# 🛰️ 1. Exercise 0 — Creature Factory

**Carpeta:** `ex0/`

### 📁 Structure

- Existe el archivo `ex0/__init__.py`.
- Existe al menos otro archivo dentro de `ex0/`.
- El archivo `__init__.py` expone únicamente las fábricas de criaturas, no las clases `Creature`.

### 🔍 Functionality

- Se define una clase abstracta `Creature` que hereda de `ABC`.
- El método `attack()` está definido como método abstracto.
- El método `describe()` está definido como método concreto.
- Existen al menos **cuatro clases concretas diferentes** de criaturas.
- Las clases concretas heredan de `Creature`.
- Se define una clase abstracta `CreatureFactory` que hereda de `ABC`.
- `CreatureFactory` contiene los métodos abstractos:
  - `create_base()`
  - `create_evolved()`
- Existen al menos **dos fábricas concretas**, una para cada familia de criaturas.
- Cada fábrica crea dos tipos de criaturas: una criatura base y una criatura evolucionada.

### ▶️ Execution

Debe comprobarse que el archivo `battle.py` está presente y que sigue el escenario establecido.

```bash
python3 ex0/battle.py
```

### ⚔️ Battle Scenario

- `battle.py` instancia las dos fábricas concretas.
- Existe una función que acepta cualquier fábrica.
- Dicha función:
  1. Crea una criatura base.
  2. Ejecuta `describe()`.
  3. Ejecuta `attack()`.
  4. Crea una criatura evolucionada.
  5. Ejecuta `describe()`.
  6. Ejecuta `attack()`.
- La función funciona con ambas fábricas.
- Existe otra función que recibe dos fábricas.
- Esta segunda función crea dos criaturas —base o evolucionadas— a partir de las fábricas recibidas.
- Las dos criaturas se enfrentan entre sí.

### 🧪 Tests

| Prueba | Esperado |
|---|---|
| Instanciar la primera fábrica | Se crea correctamente |
| Instanciar la segunda fábrica | Se crea correctamente |
| Crear una criatura base | Devuelve una `Creature` válida |
| Crear una criatura evolucionada | Devuelve una `Creature` válida |
| Ejecutar `describe()` | Muestra la descripción de la criatura |
| Ejecutar `attack()` | Ejecuta el ataque correspondiente |
| Usar la función con ambas fábricas | Funciona correctamente |
| Hacer luchar a dos criaturas | Se ejecuta el enfrentamiento |
| Uso de clases abstractas | No se pueden instanciar directamente |
| Ejecución completa de `battle.py` | Finaliza correctamente |

### 🧠 Concepts to check

- El alumno entiende qué es una clase abstracta.
- El alumno puede explicar el papel de `ABC`.
- El alumno entiende el patrón **Abstract Factory**.
- El alumno puede explicar la diferencia entre una fábrica abstracta y una fábrica concreta.
- El alumno entiende cómo se crean familias de objetos relacionados.
- La lógica no está simulada ni hardcodeada mediante `print()`.

---

# 🧬 2. Exercise 1 — Capabilities

**Carpeta:** `ex1/`

### 📁 Structure

- Existe el archivo `ex1/__init__.py`.
- Existe al menos otro archivo dentro de `ex1/`.
- El archivo `__init__.py` expone únicamente las fábricas de criaturas, no las clases `Creature`.

### 🔍 Functionality

- Se define una clase abstracta `HealCapability`.
- Se define una clase abstracta `TransformCapability`.
- Ambas clases heredan de `ABC`.
- `HealCapability` contiene el método abstracto `heal()`.
- `TransformCapability` contiene los métodos abstractos:
  - `transform()`
  - `revert()`
- Se definen al menos **cuatro nuevas clases concretas de criaturas**.
- Las nuevas criaturas heredan de `Creature` y utilizan las capacidades correspondientes.
- Deben existir:
  - **Dos criaturas con capacidad de curación**.
  - **Dos criaturas con capacidad de transformación**.
- Existen al menos **dos fábricas concretas nuevas**, una para cada familia.
- Cada fábrica crea dos criaturas.

### ▶️ Execution

Debe comprobarse que el archivo `capacitor.py` está presente y que sigue el escenario establecido.

```bash
python3 ex1/capacitor.py
```

### ⚙️ Capability Scenario

- `capacitor.py` instancia las dos nuevas fábricas.
- Se prueba cada fábrica.
- Para las criaturas base y evolucionadas se utilizan los métodos estándar:
  - `describe()`
  - `attack()`
- La capacidad correspondiente se ejecuta en el lugar correcto del proceso.
- Las capacidades de curación y transformación están implementadas mediante clases abstractas y métodos concretos apropiados.
- La funcionalidad de las capacidades no está simulada mediante salidas hardcodeadas.

### 🧪 Tests

| Prueba | Esperado |
|---|---|
| Instanciar una fábrica nueva | Se crea correctamente |
| Crear criatura con `HealCapability` | La criatura dispone de `heal()` |
| Crear criatura con `TransformCapability` | La criatura dispone de `transform()` y `revert()` |
| Ejecutar `describe()` | Muestra la descripción |
| Ejecutar `attack()` | Ejecuta el ataque |
| Ejecutar `heal()` | La criatura se cura correctamente |
| Ejecutar `transform()` | La criatura se transforma correctamente |
| Ejecutar `revert()` | La transformación se revierte correctamente |
| Probar criaturas base y evolucionadas | Funciona en ambos casos |
| Ejecución completa de `capacitor.py` | Finaliza correctamente |

### 🧠 Concepts to check

- El alumno entiende qué es una capacidad abstracta.
- Puede explicar por qué `heal()`, `transform()` y `revert()` son métodos abstractos.
- Comprende cómo añadir capacidades a las criaturas.
- Puede explicar la diferencia entre herencia y composición de capacidades.
- Entiende cómo las fábricas crean criaturas con capacidades específicas.
- Puede justificar en qué momento del flujo se aplica cada capacidad.

---

# 🏟️ 3. Exercise 2 — Abstract Strategy

**Carpeta:** `ex2/`

### 📁 Structure

- Existe el archivo `ex2/__init__.py`.
- Existe al menos otro archivo dentro de `ex2/`.

### 🔍 Functionality

- Se define una clase abstracta `BattleStrategy` que hereda de `ABC`.
- `BattleStrategy` contiene los métodos abstractos:
  - `act()`
  - `is_valid()`
- Existen al menos **tres clases concretas de estrategia**.
- Existe una estrategia **normal** que es válida para cualquier criatura, independientemente de su familia o capacidades.
- Existen estrategias adicionales relacionadas con las capacidades implementadas en `ex1`.
- Por ejemplo, una estrategia defensiva puede utilizarse con una criatura que tenga `HealCapability` y ejecutar `heal()` después de `attack()`.

### ▶️ Execution

Debe comprobarse que el archivo `tournament.py` está presente y que sigue el escenario establecido.

```bash
python3 ex2/tournament.py
```

### 🏆 Tournament Scenario

- `tournament.py` instancia las fábricas de criaturas de `ex0` y `ex1`.
- Se instancian las diferentes estrategias disponibles.
- Existe una función `battle()` que gestiona el torneo. Puede utilizar funciones auxiliares.
- `battle()` recibe como parámetro una lista de tuplas formada por:
  - Una `CreatureFactory`.
  - Una `BattleStrategy`.
- La función organiza un combate entre cada pareja de oponentes.
- Una criatura:
  - No lucha contra sí misma.
  - No lucha dos veces contra la misma criatura.
  - No participa en los dos enfrentamientos equivalentes `A-B` y `B-A`.
- Durante cada combate se aplica la estrategia asociada a la criatura.
- Una estrategia defensiva, por ejemplo, puede ejecutar `heal()` después de `attack()`.
- La estrategia normal no debe ejecutar capacidades que no le correspondan.
- Si una estrategia no es adecuada para una criatura, el torneo debe detenerse.

### 🧪 Strategy Validation Tests

| Caso | Resultado esperado |
|---|---|
| Crear una estrategia normal | Se crea correctamente |
| Crear una estrategia específica | Se crea correctamente |
| Usar estrategia normal con cualquier criatura | Válido |
| Usar estrategia defensiva con criatura con curación | Válido |
| Usar estrategia de transformación con criatura compatible | Válido |
| Usar estrategia incompatible | El torneo se detiene |
| Una criatura contra sí misma | No debe ocurrir |
| Combate `A-B` y después `B-A` | No debe repetirse |
| Aplicación de la estrategia durante el combate | Se ejecuta correctamente |
| Ejecución completa de `tournament.py` | Finaliza correctamente |

### 🧠 Concepts to check

- El alumno entiende el patrón **Strategy**.
- Puede explicar la función de `BattleStrategy`.
- Comprende la diferencia entre estrategia abstracta y estrategias concretas.
- Entiende cómo se selecciona y aplica una estrategia.
- Puede explicar cómo se comprueba que una estrategia es válida para una criatura.
- Comprende cómo evitar enfrentamientos duplicados.
- Puede explicar por qué un torneo debe detenerse cuando una estrategia no es adecuada.

---

# 🧹 4. Code Quality & Best Practices

## 🐍 Python

- El código está escrito para **Python 3.10 o superior**.
- El código cumple los estándares de `flake8`.
- No existen errores relevantes de linting.
- Todas las funciones y métodos tienen **type hints** para parámetros y valores de retorno.
- Los type hints son comprobables mediante `mypy`.
- No se requieren `docstrings` para este módulo.
- Se respetan las convenciones de nombres de Python.
- El código es legible y está bien estructurado.
- Los outputs de las demostraciones son claros e informativos.
- No hay terminaciones inesperadas, errores no controlados ni comportamientos prematuros.

## 🧩 Design Patterns

- Se utiliza correctamente el patrón **Abstract Factory**.
- Se utilizan correctamente las clases abstractas y los métodos abstractos.
- Las fábricas concretas crean familias coherentes de criaturas.
- Las capacidades están separadas de forma clara y reutilizable.
- Se utiliza correctamente el patrón **Strategy**.
- Las estrategias comprueban su compatibilidad antes de ejecutarse.
- La lógica de negocio no está hardcodeada mediante simples `print()`.
- Las responsabilidades están correctamente distribuidas entre criaturas, fábricas, capacidades y estrategias.

## 🧠 Understanding & Learning

- El alumno puede explicar el funcionamiento del patrón Abstract Factory.
- El alumno puede explicar el uso de `ABC` y `@abstractmethod`.
- El alumno comprende la finalidad de las capacidades abstractas.
- El alumno entiende cómo se incorporan capacidades a las criaturas.
- El alumno puede explicar el patrón Strategy.
- El alumno comprende cómo se valida una estrategia.
- El alumno puede explicar cómo se evita repetir enfrentamientos.
- El código demuestra una progresión desde la creación de familias de objetos hasta la aplicación de capacidades y estrategias.
- El alumno puede justificar las principales decisiones de diseño.

---

# 🚩 5. Defense

## 💬 Questions

1. ¿Por qué se utiliza `ABC`?
2. ¿Qué diferencia hay entre una clase abstracta y una clase concreta?
3. ¿Qué función cumple `@abstractmethod`?
4. ¿En qué consiste el patrón **Abstract Factory**?
5. ¿Por qué se utilizan fábricas abstractas y fábricas concretas?
6. ¿Qué ventajas aporta crear familias de objetos relacionados?
7. ¿Qué es una capacidad abstracta?
8. ¿Cómo se implementan `HealCapability` y `TransformCapability`?
9. ¿Qué diferencia existe entre `transform()` y `revert()`?
10. ¿En qué consiste el patrón **Strategy**?
11. ¿Qué responsabilidad tiene `BattleStrategy`?
12. ¿Para qué sirve `is_valid()`?
13. ¿Cómo se evita que una criatura luche contra sí misma?
14. ¿Cómo se evita repetir los combates `A-B` y `B-A`?
15. ¿Qué ocurre cuando una estrategia no es compatible con una criatura?
16. ¿Por qué es importante utilizar type hints?
17. ¿Cómo comprobarías que el código cumple `flake8` y `mypy`?

## ⚠️ Stop conditions

Si se detecta una condición que obliga a finalizar la evaluación, debe utilizarse la flag correspondiente.

- **Empty work → El repositorio está vacío.**
- **Incomplete work → El trabajo está incompleto.**
- **Invalid compilation → El código no funciona o no puede ejecutarse correctamente.**
- **Norme → Se incumplen las normas de estilo o las reglas del proyecto.**
- **Cheat → Uso de cheats, alias maliciosos o elementos no autorizados.**
- **Concerning situation → Situación preocupante durante la evaluación.**
- **Leaks → Fugas de memoria.**
- **Forbidden function → Uso de una función no autorizada.**
- **Can't support / explain code → El alumno no puede justificar o explicar el código, lo que puede indicar plagio.**

## 🏁 Final evaluation

- Si todo funciona correctamente y el alumno comprende los patrones implementados, la evaluación puede considerarse satisfactoria.
- No olvidar comprobar la flag correspondiente a la defensa.
- La evaluación debe finalizar con un comentario claro y constructivo.
