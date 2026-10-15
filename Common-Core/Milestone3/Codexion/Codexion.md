# 🚀 Codexion

## 🚀 Codexion Project

## 🚀 Codexion Tests

### 📌 0. Guidelines

#### ⚠️ Rules

- La evaluación debe realizarse de forma respetuosa, constructiva y seria.
- La revisión se realiza únicamente sobre el contenido existente en el **repositorio Git del alumno o del grupo**.
- Verifica que el repositorio pertenece al alumno/grupo y que corresponde al proyecto evaluado.
- Comprueba que `git clone` se realiza en una carpeta vacía.
- Comprueba que no se han utilizado aliases maliciosos para mostrar contenido diferente al repositorio oficial.
- El evaluador y el evaluado deben revisar los posibles scripts utilizados para facilitar la evaluación.
- Si el evaluador no ha realizado todavía el proyecto, debe leer previamente el subject completo.
- No se modifica ningún archivo salvo que sea estrictamente necesario y, en ese caso, se explica previamente al evaluado y ambos deben estar de acuerdo.
- Durante la defensa no se permite ningún `segfault`, deadlock, data race, terminación inesperada o terminación prematura/no controlada del programa.
- Debe comprobarse la ausencia de memory leaks.
- Se pueden utilizar herramientas como `leaks`, `valgrind` o `e_fence`.
- Si se detecta una condición que obliga a finalizar la evaluación, debe utilizarse la flag correspondiente.
- Los casos límite relacionados con timing deben discutirse honestamente, especialmente en hardware lento.

#### 🚩 Stop conditions

Si se detecta una condición que obliga a finalizar la evaluación, utiliza la flag correspondiente:

- **Empty work → El repositorio está vacío**
- **Incomplete work → Falta trabajo obligatorio**
- **Invalid compilation → Error de compilación**
- **Norme → Error de norma**
- **Cheat → Uso de cheating o contenido no autorizado**
- **Crash → Segmentation fault, crash o terminación inesperada**
- **Concerning situation → Situación preocupante**
- **Leaks → Memory leaks**
- **Forbidden function → Uso de una función no permitida**
- **Can't support / explain code → El alumno no puede explicar o defender el código**

---

### ⚙️ 1. Preliminaries

#### 🐍 C Standard & Compilation

El proyecto debe estar programado en **C89** y compilar con:

```bash
-Wall -Wextra -Werror -pthread
```

##### 🧪 Compilation Tests

Ejecuta:

```bash
make
```

Verifica:

- El proyecto compila correctamente.
- No aparecen warnings.
- `-Wall -Wextra -Werror -pthread` se utilizan correctamente.
- El binario generado se llama:

```text
codexion
```

##### ❌ Immediate Failure Conditions

Cualquiera de los siguientes implica **0** según la escala:

- Error de compilación.
- `segmentation fault`.
- Data race.
- Deadlock.
- Interleaved log line.
- Memory leak.

---

### 📁 2. Program Arguments

El programa debe aceptar **exactamente** los siguientes argumentos y en este orden:

```text
number_of_coders
time_to_burnout
time_to_compile
time_to_debug
time_to_refactor
number_of_compiles_required
dongle_cooldown
scheduler
```

#### 🔍 Argument Validation

Comprueba que:

- El número de argumentos es exactamente el esperado.
- Los argumentos están en el orden correcto.
- Los valores se interpretan correctamente.
- `scheduler` solo acepta:
  - `fifo`
  - `edf`

#### 🧪 Example Structure

```bash
./codexion number_of_coders time_to_burnout time_to_compile time_to_debug time_to_refactor number_of_compiles_required dongle_cooldown fifo
```

o:

```bash
./codexion number_of_coders time_to_burnout time_to_compile time_to_debug time_to_refactor number_of_compiles_required dongle_cooldown edf
```

---

### 🧵 3. Coder Threads

#### 🔍 Thread Requirements

- Cada coder debe estar representado por un thread.
- Debe utilizarse `pthread_create`.
- El comportamiento concurrente debe estar correctamente sincronizado.
- No debe existir data race.
- No debe existir deadlock.
- Los threads deben finalizar correctamente.

#### 🧪 Tests

| Prueba | Resultado esperado |
|---|---|
| Ejecutar con pocos coders | Todos los threads funcionan correctamente |
| Ejecutar con varios coders | No existen race conditions |
| Finalización del programa | No quedan threads sin gestionar |
| Ejecución concurrente | No existe deadlock |
| Logs simultáneos | No existen líneas intercaladas |

---

### 🌐 4. Global Mutable State

#### ⚠️ Critical Check

Comprueba si existe alguna **variable global mutable** utilizada para gestionar:

- Recursos compartidos (`dongles`).
- Política de scheduling.
- Logging.

#### ❌ Required behavior

Si se encuentra estado global mutable utilizado para cualquiera de estos propósitos:

> **La evaluación se detiene aquí.**

Se puede continuar inspeccionando el código, pero **no se califican los ejercicios**.

---

### 💻 5. Codexion Testing — Easy

#### ▶️ Basic Execution

No utilizar más de **200 coders**.

No utilizar valores de timing inferiores a **60ms**.

#### 🔍 Required Behavior

Comprueba que:

- Ningún coder se quema (`burns out`).
- Todos los coders completan el número requerido de compiles.
- La ejecución termina correctamente.
- No existen crashes.
- No existen deadlocks.
- No existen data races.
- Los logs son coherentes.

#### 🧪 Tests

| Caso | Resultado esperado |
|---|---|
| Pocos coders | Todos completan correctamente |
| Varios coders | Todos completan correctamente |
| `time_to_burnout` suficiente | Ningún coder se quema |
| Compiles requeridos | Todos completan la cantidad solicitada |
| Ejecución completa | Finaliza correctamente |

---

### 🔥 6. Codexion Testing — Less Easy

#### 🧪 Burnout Edge Cases

Valida los casos límite relacionados con el burnout:

- Valores próximos al límite de burnout.
- Situaciones de alta contención.
- Diferentes combinaciones de timings.
- Casos en hardware más lento.

> ⚠️ La escala indica que los casos borderline de timing deben discutirse honestamente antes de considerarlos fallos.

#### 📝 Logging & Timing

Comprueba:

- Logging correcto.
- Timing dentro de las tolerancias razonables.
- Las líneas de log no se intercalan.
- Los estados de los coders son coherentes.

#### 🔌 Dongle State

Comprueba:

- No existe duplicación de dongles.
- Los estados de los dongles son correctos.
- La adquisición y liberación de recursos están correctamente sincronizadas.
- No se utilizan dos coders simultáneamente sobre un mismo dongle cuando no corresponde.

---

### ⏱️ 7. Codexion Testing — Medium

#### ❄️ Dongle Cooldown

Comprueba el comportamiento de:

```text
dongle_cooldown
```

Verifica que:

- El cooldown se respeta.
- Los dongles no pueden reutilizarse incorrectamente durante el cooldown.
- El comportamiento sigue siendo correcto bajo contención.

#### 📋 Scheduler — FIFO

Ejecuta utilizando:

```text
fifo
```

Comprueba que la política FIFO se respeta.

#### ⏰ Scheduler — EDF

Ejecuta utilizando:

```text
edf
```

Comprueba que la política EDF funciona correctamente.

##### 🧪 Scheduler Tests

| Caso | Resultado esperado |
|---|---|
| `fifo` | Se utiliza FIFO |
| `edf` | Se utiliza EDF |
| Alta contención | Scheduling consistente |
| Cambio FIFO → EDF | Comportamiento diferente cuando corresponda |
| Ejecución completa | No aparecen deadlocks ni races |

#### 🔧 Refactoring

Comprueba:

- Timing del refactoring.
- Transiciones de estado correctas.
- Logging correcto durante el refactoring.
- Serialización correcta de los logs.

---

### 🧠 8. Concurrency & Synchronization

#### 🔍 Blocking Cases

El `README.md` debe incluir una sección:

```text
Blocking cases handled
```

Debe describir **todos los problemas de concurrencia** que la solución aborda.

Comprueba que el alumno puede explicar:

- Qué recursos son compartidos.
- Qué situaciones pueden producir carreras.
- Cómo se evita que dos coders accedan incorrectamente a un mismo recurso.
- Cómo se evita el deadlock.
- Cómo se controla el acceso a los dongles.
- Cómo se gestiona el scheduling.
- Cómo se serializa el logging.

#### 🔐 Thread Synchronization Mechanisms

El `README.md` debe incluir una sección:

```text
Thread synchronization mechanisms
```

Debe explicar los primitives de threading utilizados.

##### 💬 Defense Questions

- ¿Qué mecanismos de sincronización utilizaste?
- ¿Por qué son necesarios?
- ¿Dónde se utilizan?
- ¿Qué problema de concurrencia resuelve cada uno?
- ¿Cómo evitas una data race?
- ¿Cómo evitas un deadlock?
- ¿Cómo proteges el logging?

---

### 📖 9. README.md

**Archivo:** `README.md`

#### 🔍 Required Content

- El archivo existe en la raíz del repositorio.
- La primera línea está en cursiva y tiene exactamente el formato:

```text
This project has been created as part of the 42 curriculum by <login1>[, <login2>, <login3>...].
```

- Existe una sección **Description**.
- Existe una sección **Instructions** con información relevante sobre:
  - compilación,
  - instalación,
  - ejecución.
- Existe una sección **Resources**.
- `Resources` incluye referencias como documentación/tutoriales/etc.
- Se explica cómo se utilizó la IA.
- Se especifica para qué tareas y qué partes del proyecto se utilizó IA.
- Existe una sección **Blocking cases handled**.
- Se describen todos los problemas de concurrencia tratados.
- Existe una sección **Thread synchronization mechanisms**.
- Se explican los primitives de threading utilizados.

#### 🧪 README Tests

| Prueba | Esperado |
|---|---|
| `README.md` en la raíz | Presente |
| Primera línea obligatoria | Formato correcto |
| Description | Presente |
| Instructions | Presente |
| Resources | Presente |
| Uso de IA documentado | Presente |
| Blocking cases handled | Presente |
| Thread synchronization mechanisms | Presente |

---

### 🧪 10. Memory & Concurrency Safety

#### 💾 Memory Leaks

Toda la memoria asignada en heap debe liberarse correctamente antes del final de la ejecución.

Puedes utilizar:

```bash
leaks
```

o:

```bash
valgrind
```

o:

```bash
e_fence
```

##### 🧪 Tests

- Ejecuta el programa con diferentes cantidades de coders.
- Comprueba ejecuciones normales.
- Comprueba ejecuciones con alta contención.
- Comprueba que toda la memoria se libera correctamente.

##### ❌ Failure

Si se detecta un memory leak:

> Utiliza la flag **Leaks**.

---

### 🧹 11. Code Quality & Best Practices

#### 🐍 C89

- El código cumple C89.
- Compila con:
  - `-Wall`
  - `-Wextra`
  - `-Werror`
  - `-pthread`
- No existen warnings.
- El código es legible.
- La gestión de errores es clara.
- Los threads se gestionan correctamente.
- Los recursos se liberan correctamente.

#### 🧵 Concurrency

- No existe data race.
- No existe deadlock.
- No existe acceso incorrecto a recursos compartidos.
- Los logs no se intercalan.
- Los estados de los dongles son coherentes.
- El scheduler funciona según el modo seleccionado.
- No existe estado global mutable prohibido.

#### 🧠 Understanding & Learning

- El alumno puede explicar la arquitectura concurrente.
- El alumno puede explicar cómo se sincronizan los threads.
- El alumno puede explicar la gestión de los dongles.
- El alumno puede explicar FIFO.
- El alumno puede explicar EDF.
- El alumno puede explicar el cooldown.
- El alumno puede explicar las condiciones de burnout.
- El alumno puede justificar sus decisiones de sincronización.

---

### 🔄 12. Codexion Recode — EDF Tie-Breaker

#### 🎯 Requirement

Modificar la implementación de EDF para que:

> En caso de deadlines iguales, se prefiera el **coder con mayor `coder_id`**.

#### 🧪 Test

- Provoca una situación de contention con deadlines iguales.
- Comprueba qué coder obtiene prioridad.
- Verifica que, en caso de empate:
  - `higher coder_id` → mayor prioridad.
- Comprueba que la modificación no rompe el resto del scheduler EDF.

##### 💬 Defense Questions

1. ¿Dónde implementaste el tie-breaker?
2. ¿Cómo detectas dos deadlines iguales?
3. ¿Por qué utilizas `coder_id` como segundo criterio?
4. ¿Puedes demostrar el comportamiento mediante un test de contention?

---

### 🚩 13. Defense

#### 💬 Questions

1. ¿Por qué cada coder debe representarse mediante un thread?

2. ¿Qué función cumple `pthread_create`?

3. ¿Qué problemas de concurrencia existen en este proyecto?

4. ¿Cómo evitas una data race?

5. ¿Cómo evitas un deadlock?

6. ¿Cómo gestionas los dongles compartidos?

7. ¿Cómo garantizas que un dongle no se duplica o utiliza incorrectamente?

8. ¿Cómo funciona el cooldown de los dongles?

9. ¿Qué ocurre cuando un coder está cerca de quemarse?

10. ¿Cómo se determina si un coder completa correctamente sus compiles?

11. ¿Qué diferencia hay entre FIFO y EDF?

12. ¿Cómo implementaste FIFO?

13. ¿Cómo implementaste EDF?

14. ¿Qué ocurre cuando dos coders tienen el mismo deadline en EDF?

15. ¿Cómo implementarías el tie-breaker de EDF solicitado?

16. ¿Qué mecanismos de sincronización utilizaste?

17. ¿Por qué elegiste esos mecanismos?

18. ¿Cómo proteges el logging para evitar líneas intercaladas?

19. ¿Qué estado se comparte entre los threads?

20. ¿Por qué no puedes utilizar determinadas variables globales mutables?

21. ¿Cómo verificaste la ausencia de memory leaks?

22. ¿Qué herramientas utilizaste para comprobar memory leaks?

23. ¿Cómo comprobarías una data race?

24. ¿Cómo comprobarías un deadlock?

25. ¿Qué ocurre si el programa recibe argumentos incorrectos?

26. ¿Por qué el proyecto utiliza `-pthread`?

27. ¿Qué partes del proyecto te resultaron más difíciles?

28. ¿Puedes explicar el flujo completo de un coder desde que comienza hasta que termina?

---

### 📝 14. Final Evaluation

#### Checklist

- Repository correcto
- Repository no vacío
- Trabajo completo
- C89
- `make` correcto
- `-Wall`
- `-Wextra`
- `-Werror`
- `-pthread`
- Binary `codexion`
- Argumentos correctos
- Threads mediante `pthread_create`
- No global mutable state prohibido
- No segmentation fault
- No data race
- No deadlock
- No interleaved log lines
- No memory leaks
- Burnout tests
- Logging correcto
- Dongle state correcto
- Dongle cooldown correcto
- FIFO correcto
- EDF correcto
- Refactoring correcto
- README completo
- Blocking cases documentados
- Synchronization mechanisms documentados
- EDF tie-breaker comprobado
- Defense completada
- El alumno puede explicar el código
