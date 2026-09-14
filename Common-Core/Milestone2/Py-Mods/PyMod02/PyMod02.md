# 🌱 Python Module 02

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
- La escala solicita expresamente una prueba añadida por el alumno en el ejercicio 3, **sin modificar las tres clases de excepciones**.
- Ante un programa que no funciona u otra incidencia que obliga a finalizar la evaluación, utiliza la flag correspondiente. La escala establece **0**, o **-42 en caso de trampa**.
- No se permiten terminaciones inesperadas, prematuras o no controladas del programa.
- Las excepciones provocadas y **capturadas correctamente** forman parte del módulo; no deben confundirse con un crash.
- Salvo en caso de trampa, se anima a continuar la discusión pedagógica para identificar los problemas y evitar que se repitan, aunque la calificación haya terminado.

### 📁 Structure

- Comprueba que la estructura del proyecto coincide con el subject y que cada ejercicio tiene su archivo correspondiente.
- Si falta contenido requerido, utiliza la flag **Incomplete work**.
- Los archivos exigidos por la escala son los siguientes. Las rutas usan la organización `ex0/`–`ex4/` del ejemplo; contrástala con la estructura indicada en el subject.

```text
ex0/ft_first_exception.py
ex1/ft_raise_exception.py
ex2/ft_different_errors.py
ex3/ft_custom_errors.py
ex4/ft_finally_block.py
```

### 🧰 General concepts to check

- El código está escrito para **Python 3.10 o superior**.
- El código cumple los estándares de `flake8`, **sin errores ni advertencias**.
- Cada ejercicio está en su propio archivo, con el nombre especificado.
- Todas las funciones y métodos tienen **type hints para parámetros y valores de retorno**. Compruébalo con `mypy`.
- **No se requieren docstrings para este módulo.**
- Los programas no terminan inesperadamente por excepciones sin capturar.
- Se utilizan correctamente `try`, `except`, `raise` y `finally` donde corresponde.
- Se demuestra la progresión desde la captura de errores de conversión hasta las excepciones personalizadas y la limpieza de recursos.
- **Excepción de tipado permitida:** en el ejercicio 2 se admite el error de `mypy` correspondiente al código deliberadamente incorrecto que provoca `TypeError`. Esto no exime al resto del código de los requisitos de tipado.

> Guía basada en **PyMod02Eval.pdf**. El PDF no incluye los límites numéricos de temperatura ni el literal del mensaje por defecto de las excepciones: comprueba esos detalles en el subject. Los ejemplos de entrada y las preguntas complementarias sirven para aplicar las comprobaciones de la escala, sin añadir requisitos nuevos.

---
---

# 🌡️ 1. Exercise 0 — Agricultural Data Validation

**Archivo:** `ex0/ft_first_exception.py`

### ▶️ Execution

```bash
python3 ex0/ft_first_exception.py
```

### 🔍 Functionality

- Existe la función `input_temperature(temp_str)` y funciona correctamente.
- Convierte la entrada al tipo numérico previsto por el ejercicio.
- Cuando la entrada es correcta, **devuelve la temperatura**.
- Existe la función `test_temperature()`.
- `test_temperature()` utiliza un bloque `try/except` que captura **`Exception` o `ValueError`**; la escala admite ambas opciones.
- Se prueba `input_temperature()` con entradas válidas e inválidas.
- Cuando ocurre una excepción, `test_temperature()` imprime un mensaje de error y continúa ejecutándose.
- Los errores se producen y capturan realmente; la demostración no se limita a imprimir mensajes simulados.

### 🧪 Tests

| Prueba | Esperado |
|---|---|
| Entrada numérica válida, por ejemplo `"25"` | `input_temperature()` devuelve la temperatura numérica correspondiente |
| Entrada no convertible, como `"abc"` | Se produce un error de conversión que captura `test_temperature()` |
| Comprobar la salida tras el error | Se muestra un mensaje de error |
| Ejecutar otra prueba después de la entrada inválida | El programa continúa funcionando |
| Inspeccionar el retorno de una llamada válida | Se devuelve el valor; no basta con imprimirlo |

### 🧠 Concepts to check

- ¿Qué ocurre cuando se intenta convertir `"abc"` a un número?
- ¿Por qué el programa no se cierra cuando se produce ese error?
- El alumno puede señalar qué instrucción produce la excepción y dónde se captura.
- Distingue entre devolver una temperatura e imprimir un mensaje.

---
---

# 🚧 2. Exercise 1 — Agricultural Data Validation Pipeline

**Archivo:** `ex1/ft_raise_exception.py`

### ▶️ Execution

```bash
python3 ex1/ft_raise_exception.py
```

### 🔍 Functionality

- `input_temperature(temp_str)` amplía el comportamiento del ejercicio 0.
- Comprueba los límites **mínimo y máximo de temperatura** establecidos en el subject.
- Si la temperatura es demasiado baja o demasiado alta, **lanza una excepción**.
- No basta con imprimir un aviso o devolver un valor especial ante una temperatura fuera de rango: debe producirse la excepción requerida.
- `test_temperature()` captura **`Exception` o `ValueError`** mediante `try/except`.
- La demostración incluye entradas válidas, entradas no numéricas, temperaturas demasiado bajas y temperaturas demasiado altas.
- Ante una excepción, se imprime un mensaje de error y la ejecución continúa.
- Cuando la entrada es numérica y está dentro de los límites permitidos, `input_temperature()` sigue devolviendo la temperatura.

### 🧪 Range Validation Tests

| Caso | Esperado |
|---|---|
| Valor numérico dentro del rango permitido | Devuelve la temperatura |
| Entrada no numérica, como `"abc"` | Se captura el error de conversión y se muestra un mensaje |
| Temperatura inferior al mínimo permitido | `input_temperature()` lanza una excepción; `test_temperature()` la captura |
| Temperatura superior al máximo permitido | `input_temperature()` lanza una excepción; `test_temperature()` la captura |
| Valores en los límites mínimo y máximo | Se aceptan o rechazan según la inclusión de los límites indicada en el subject |
| Una entrada válida después de una inválida | La ejecución continúa y devuelve el resultado correcto |

### 🔎 Raise & Validation

- La validación de rango está implementada en `input_temperature()`.
- Las excepciones permiten comunicar al llamador que la temperatura no es válida.
- La gestión y el mensaje de error se realizan en `test_temperature()`.
- El alumno puede explicar la diferencia entre un error de conversión y un valor numérico fuera del rango permitido.
- Puede señalar dónde se lanza la excepción y cómo llega al bloque `except`.

---
---

# 🧩 3. Exercise 2 — Different Types of Problems

**Archivo:** `ex2/ft_different_errors.py`

### ▶️ Execution

```bash
python3 ex2/ft_different_errors.py
```

### 🔍 Functionality

- Existe `garden_operations()` y crea diferentes escenarios de error.
- Demuestra **`ValueError`** mediante una conversión de datos inválida.
- Demuestra **`ZeroDivisionError`** mediante una división por cero.
- Demuestra **`FileNotFoundError`** mediante el acceso a un archivo inexistente.
- Demuestra **`TypeError`** mediante una operación con tipos incompatibles.
- Existe la función `test_error_types()`.
- La estructura de captura utiliza **un único bloque `try` con varias cláusulas `except`, una para cada tipo de error**.
- Cada escenario se ejecuta de forma que su excepción llegue al manejador correspondiente.
- El programa continúa ejecutándose después de cada error capturado y permite demostrar los cuatro tipos.
- **El error de `mypy` provocado por el código intencionalmente defectuoso del caso `TypeError` está permitido por la escala.**

### 🧪 Error Types Tests

| Escenario | Excepción esperada | Resultado esperado |
|---|---|---|
| Conversión de datos inválida | `ValueError` | Se ejecuta su cláusula `except` y el programa continúa |
| División por cero | `ZeroDivisionError` | Se ejecuta su cláusula `except` y el programa continúa |
| Apertura de un archivo inexistente | `FileNotFoundError` | Se ejecuta su cláusula `except` y el programa continúa |
| Operación con tipos incompatibles | `TypeError` | Se ejecuta su cláusula `except` y el programa continúa |
| Ejecutar todos los escenarios de prueba | Los cuatro tipos anteriores | Ningún error impide demostrar los siguientes casos |
| Revisar el tipado del caso `TypeError` | Puede aparecer el diagnóstico deliberado de `mypy` | No se penaliza ese diagnóstico autorizado |

### 🔎 Exception Handling Validation

- Cada `except` corresponde al tipo de error que debe gestionar.
- No se sustituye la estructura requerida por varios bloques `try/except` independientes, uno por tipo.
- No basta con colocar cuatro operaciones fallidas consecutivas dentro del mismo `try`: la primera excepción interrumpe ese recorrido. Comprueba que se ejercitan realmente los cuatro escenarios.
- La captura no se simula mediante mensajes impresos sin ejecutar las operaciones que provocan los errores.
- El alumno puede explicar por qué Python dispone de distintos tipos de excepción.
- Puede explicar cómo se selecciona la cláusula `except` que se ejecuta.

---
---

# 🌿 4. Exercise 3 — Making Your Own Error Types

**Archivo:** `ex3/ft_custom_errors.py`

### ▶️ Execution

```bash
python3 ex3/ft_custom_errors.py
```

### 🔍 Functionality

- Existe la clase **`GardenError`** y hereda de **`Exception`**.
- Existe la clase **`PlantError`** y hereda de **`GardenError`**.
- Existe la clase **`WaterError`** y hereda de **`GardenError`**.
- Las clases son simples y están bien estructuradas.
- Existe una estructura de pruebas que **lanza y captura** excepciones de diferentes tipos.
- Se demuestra la captura específica de `PlantError` y `WaterError`.
- Se demuestra que capturar `GardenError` permite capturar también sus excepciones derivadas.
- Una estructura de pruebas idéntica a la del ejercicio 2 está **recomendada, pero no es obligatoria**.
- Cuando no se proporciona un mensaje, se utiliza el **mensaje por defecto establecido en el subject**.

### 🧪 Custom Exceptions & Inheritance Tests

| Caso | Esperado |
|---|---|
| Revisar la herencia de `GardenError` | Hereda de `Exception` |
| Revisar la herencia de `PlantError` y `WaterError` | Ambas heredan de `GardenError` |
| Lanzar `PlantError` y capturarlo específicamente | Se ejecuta el manejador de `PlantError` |
| Lanzar `WaterError` y capturarlo específicamente | Se ejecuta el manejador de `WaterError` |
| Lanzar `PlantError` bajo un manejador `except GardenError` | La excepción se captura mediante la clase base |
| Lanzar `WaterError` bajo un manejador `except GardenError` | La excepción se captura mediante la clase base |
| Lanzar `PlantError()` sin argumentos en la prueba añadida | Se muestra correctamente el mensaje por defecto del subject |

### ✍️ Recode by the Evaluated Learner

- Pide al alumno que añada una prueba que lance **`PlantError()` sin ningún argumento**.
- **No se modifica `GardenError`, `PlantError` ni `WaterError`** para resolver esta prueba.
- La nueva prueba captura la excepción y muestra su mensaje.
- Comprueba que aparece el mensaje por defecto exigido, sin añadirlo artificialmente en el código de la prueba.
- Esta modificación del código de pruebas está solicitada expresamente en la escala y se realiza con el alumno.

### 🧠 Concepts to check

- El alumno puede explicar por qué sus excepciones heredan de `Exception`.
- Puede explicar por qué `except GardenError` captura `PlantError` y `WaterError`.
- Distingue entre capturar un error concreto y capturar una familia de errores.
- Puede mostrar dónde se define el mensaje por defecto y cómo se utiliza al omitir el argumento.

---
---

# 💧 5. Exercise 4 — Finally Block — Always Clean Up

**Archivo:** `ex4/ft_finally_block.py`

### ▶️ Execution

```bash
python3 ex4/ft_finally_block.py
```

### 🔍 Functionality

- Existe la función `water_plant(plant_name)`.
- Comprueba que el nombre está capitalizado utilizando **`plant_name.capitalize() == plant_name`**.
- Si no se cumple la condición, lanza una excepción **`PlantError`**.
- Si el nombre cumple la condición, imprime un mensaje de éxito.
- Existe la función `test_watering_system()`.
- Se imprime un mensaje de **apertura** antes de regar las plantas.
- Se utiliza una estructura **`try/except/finally`** que gestiona correctamente los errores.
- Cuando ocurre un error, **`test_watering_system()` se detiene y retorna a la parte principal del archivo**.
- El bloque `finally` imprime un mensaje de **cierre**, tanto en el caso correcto como en el caso de error.
- `finally` se ejecuta también cuando la función retorna debido a un error.
- La demostración incluye una ejecución normal y otra con un nombre no capitalizado.

### 🧪 Watering & Cleanup Tests

| Caso | Esperado |
|---|---|
| Llamar a `water_plant("Rose")` | La condición se cumple y se imprime el mensaje de éxito |
| Llamar a `water_plant("rose")` dentro de la prueba controlada | Se lanza `PlantError` y se captura en el sistema de riego |
| Comprobar un nombre como `"ROSE"` | No cumple la igualdad con `capitalize()`; se lanza `PlantError` |
| Ejecutar el sistema únicamente con nombres válidos | Apertura, mensajes de éxito y cierre |
| Ejecutar el sistema con un nombre inválido | Apertura, captura del error y cierre antes de retornar |
| Colocar una planta pendiente después de la que provoca el error | No se continúa regando dentro de esa llamada a `test_watering_system()` |
| Comprobar la ejecución después del retorno por error | El control vuelve a la parte principal del archivo |
| Comparar el caso correcto y el caso con error | El mensaje de cierre aparece en ambos |

### 🔎 Finally Validation

- La comprobación de capitalización coincide con la expresión exigida; no se limita a comprobar la primera letra.
- El mensaje de apertura aparece antes de comenzar el riego.
- El mensaje de cierre está realmente dentro de `finally`.
- El retorno por error no impide ejecutar `finally`.
- La captura del error evita un crash, pero **no continúa con el resto del riego en esa misma llamada**.
- El alumno puede explicar cuándo se ejecuta `finally` en los escenarios de la demostración.
- Puede explicar por qué es importante realizar la limpieza incluso cuando ocurre un error.
- Puede dar ejemplos de recursos que necesitan liberarse o cerrarse, como archivos, conexiones o bloqueos.

---
---

# 🧹 6. Code Quality & Best Practices

## 🐍 Python

- El código está escrito para **Python 3.10 o superior**.
- El código cumple los estándares de `flake8`, **sin errores ni advertencias**.
- Cada ejercicio está en su archivo correspondiente.
- Todas las funciones y métodos tienen **type hints** para los parámetros y valores de retorno.
- Se comprueba el tipado utilizando `mypy`.
- Se respeta la excepción autorizada para el error deliberado de tipos del ejercicio 2.
- **No se requieren docstrings para este módulo.**
- Los programas no terminan inesperadamente por excepciones sin capturar.
- El código es legible y las demostraciones permiten identificar cada prueba y su resultado.

Comprobación de estilo desde la raíz del repositorio:

```bash
flake8 .
```

Comprobación de tipos por ejercicio, incluyendo funciones sin anotar:

```bash
for exercise in ex0 ex1 ex2 ex3 ex4; do
    mypy --disallow-untyped-defs "$exercise"
done
```

Revisa los diagnósticos individualmente: **solo está autorizado el error de tipado correspondiente al caso deliberado de `TypeError` en `ex2`**. Los comandos presuponen la organización de carpetas indicada en esta guía.

## 🧩 Exceptions & Error Handling

- Los bloques `try` contienen las operaciones que pueden fallar.
- Las cláusulas `except` capturan las excepciones previstas por cada ejercicio.
- En los ejercicios 0 y 1, la escala admite capturar `Exception` o `ValueError`.
- En el ejercicio 2 se utiliza el único `try` con varios `except` requerido, y se prueban los cuatro errores.
- `raise` se utiliza para comunicar los errores que el programa detecta explícitamente.
- Las excepciones personalizadas respetan la jerarquía `Exception` → `GardenError` → `PlantError` / `WaterError`.
- Las pruebas demuestran tanto capturas específicas como capturas mediante la clase base.
- El mensaje por defecto funciona sin modificar las clases durante la prueba de defensa.
- `finally` realiza el cierre en las rutas normal y de error del ejercicio 4, incluido el retorno desde la función.

## 🧠 Understanding & Learning

- El alumno distingue entre producir, lanzar y capturar una excepción.
- Puede explicar cómo cambia el flujo de ejecución cuando ocurre un error.
- Entiende por qué la ejecución de un bloque `try` no continúa en la instrucción siguiente a la que ha fallado.
- Entiende la utilidad de los distintos tipos de excepción.
- Puede explicar la herencia de las excepciones personalizadas.
- Distingue entre continuar el programa y continuar la función que ha fallado.
- Puede justificar la necesidad de ejecutar acciones de limpieza al abandonar una operación.

---
---

# 🚩 7. Defense

## 💬 Questions

1. ¿Qué ocurre al intentar convertir `"abc"` a un número?
2. ¿Por qué el programa no se cierra cuando se captura esa excepción?
3. ¿Qué diferencia hay entre devolver un valor, imprimir un mensaje y lanzar una excepción?
4. ¿Qué diferencia hay entre una entrada no numérica y una temperatura numérica fuera de rango?
5. ¿Por qué Python tiene distintos tipos de excepción?
6. ¿Cómo decide Python qué cláusula `except` ejecutar?
7. ¿Por qué no basta con poner cuatro operaciones fallidas consecutivas en un único `try` para demostrar los cuatro errores?
8. ¿Qué error de `mypy` está permitido en este módulo y por qué?
9. ¿Por qué `GardenError` hereda de `Exception`?
10. ¿Por qué `except GardenError` también captura `PlantError` y `WaterError`?
11. ¿Qué mensaje debe aparecer al lanzar `PlantError()` sin argumentos? Demuéstralo sin modificar las clases.
12. ¿Qué comprueba exactamente `plant_name.capitalize() == plant_name`? ¿Aceptaría `"ROSE"`?
13. ¿Qué ocurre con `finally` cuando se ejecuta un `return` debido a un error?
14. ¿Se siguen regando plantas después de un error dentro de la misma llamada a `test_watering_system()`?
15. ¿Por qué es importante la limpieza de recursos incluso cuando una operación falla? Da ejemplos.

## ⚠️ Stop conditions

Si se detecta una condición que obliga a finalizar la evaluación, debe utilizarse la flag correspondiente.

- **Empty work →** El trabajo es inexistente.
- **Incomplete work →** El trabajo está incompleto.
- **Invalid compilation →** El código no puede compilarse o interpretarse correctamente.
- **Norme →** Incumplimiento de la norma aplicable.
- **Cheat →** Trampa o uso de elementos no autorizados.
- **Crash →** Terminación inesperada, prematura o no controlada, incluida una excepción sin capturar que termina el programa.
- **Concerning situation →** Situación preocupante.
- **Leaks →** Fugas de memoria.
- **Forbidden function →** Uso de una función no autorizada.
- **Can't support / explain code →** El alumno no puede defender o explicar su código.

Las excepciones deliberadas que se gestionan correctamente no constituyen un crash. Tampoco debe penalizarse el diagnóstico de `mypy` autorizado para el caso `TypeError` del ejercicio 2. La incapacidad de explicar el código no demuestra por sí sola que exista plagio.

## 📝 Evaluation conclusion

- Revisa la valoración final: **Ok**, **Outstanding project** o la flag de incidencia correspondiente.
- Deja un comentario constructivo con los resultados y problemas encontrados.
- El comentario final de la escala admite un máximo de **2048 caracteres**.
