# 🌱 Python Module 00

## 📌 0. Guidelines

### ⚠️ Rules

- La revisión se realiza **en presencia del alumno evaluado**.
- Mantén una actitud educada, respetuosa y constructiva. Comenta con el alumno los problemas encontrados y las posibles diferencias de interpretación del subject.
- Comprueba que el repositorio Git pertenece al alumno y corresponde al proyecto correcto.
- Comprueba que `git clone` se realiza en una carpeta vacía. Se evalúa únicamente el contenido del **repositorio Git del alumno**.
- Si no se ha presentado ningún trabajo, la evaluación termina con **0 — Empty work**.
- No se han utilizado alias maliciosos para alterar el contenido evaluado.
- El evaluador y el evaluado han revisado los posibles scripts utilizados durante la evaluación.
- Si el evaluador todavía no ha completado el proyecto, debe leer el subject completo antes de iniciar la defensa.
- No debería ser necesario editar archivos, salvo el de configuración, si existe. Cualquier modificación debe explicarse y acordarse previamente con el alumno.
- Si un ejercicio no funciona, **la evaluación se detiene en ese punto**. Los ejercicios posteriores pueden inspeccionarse, pero no se califican.
- Una terminación inesperada, prematura o no controlada del programa implica **0** y la flag correspondiente.
- Cuando una incidencia obliga a finalizar la evaluación, utiliza la flag apropiada. La escala indica **0**, o **-42 en caso de trampa**. Salvo en caso de trampa, se anima a continuar la discusión pedagógica.

### 📁 Structure

- Comprueba que los ejercicios están en los directorios correspondientes y contienen las funciones requeridas.
- Los nombres de archivo siguientes siguen los nombres de las funciones; el PDF exige expresamente ambos nombres de archivo de `ex6/`.
- Si falta contenido requerido, utiliza la flag correspondiente y aplica la regla de interrupción de la evaluación.

```text
ex0/ft_hello_garden.py
ex1/ft_garden_name.py
ex2/ft_plot_area.py
ex3/ft_harvest_total.py
ex4/ft_plant_age.py
ex5/ft_water_reminder.py
ex6/ft_count_harvest_iterative.py
ex6/ft_count_harvest_recursive.py
ex7/ft_seed_inventory.py
```

### 🧰 General concepts to check

- Los ejercicios definen las funciones solicitadas, **no un programa principal**.
- Las funciones tienen los nombres correctos y pueden ejecutarse mediante el helper `main.py` proporcionado con la escala.
- Las soluciones demuestran los conceptos previstos: salida por pantalla, entradas, operaciones aritméticas, condicionales, iteración, recursión y anotaciones de tipo.
- Los resultados dependen de los datos proporcionados y se calculan correctamente.
- El formato de salida coincide con el requerido, incluidos mayúsculas, espacios y puntuación.
- Las funciones están en sus directorios correspondientes, de `ex0/` a `ex7/`.
- La regla general de entregar una función admite la **excepción explícita de funciones auxiliares en la versión recursiva de `ex6`**.

### 📎 Reference & execution notes

> Esta guía adapta la escala del PDF **PyMod00Eval(2).pdf**. El documento contiene traducciones inconsistentes de mensajes, identificadores y unidades. Los mensajes en español que aparecen abajo describen la salida indicada en el PDF; para comprobar cadenas exactas, utiliza el **subject y el helper `main.py` originales**. Por ejemplo, el PDF usa varias traducciones para el prefijo del área de una parcela. No penalices diferencias basándote únicamente en esas traducciones.

- La escala enlaza un subject y un helper `main.py`; sus contenidos no están incluidos en el PDF adjunto.
- Ejecuta cada función mediante ese helper, siguiendo su interfaz real. No basta con ejecutar directamente un archivo que solo define una función.
- Las pruebas de las tablas proceden de la escala. Las preguntas de defensa son un apoyo añadido para conservar la estructura del ejemplo y no constituyen requisitos nuevos.

---
---

# 👋 1. Exercise 0 — ft_hello_garden

**Directorio:** `ex0/`  
**Archivo de referencia:** `ft_hello_garden.py`

### ▶️ Execution

Ejecuta `ft_hello_garden()` mediante el helper `main.py`, sin pasar parámetros.

### 🔍 Functionality

- El archivo contiene una función llamada `ft_hello_garden()` y no un programa principal.
- La función no requiere parámetros.
- Utiliza `print()` para mostrar el saludo.
- La salida coincide exactamente con el saludo exigido por el original. El PDF lo muestra como `Hola, Garden Community!`.
- El archivo está en `ex0/`.

### 🧪 Tests

| Prueba | Esperado |
|---|---|
| Llamar a `ft_hello_garden()` sin argumentos | Se ejecuta correctamente |
| Comprobar el mensaje impreso | Saludo exacto requerido, sin texto adicional |
| Inspeccionar la implementación | Utiliza `print()` dentro de la función |

### 🧹 Code Quality — Exercise 0

- El nombre de la función es correcto.
- El código es legible y está bien estructurado.
- La solución se entrega como función, no como programa principal.

---
---

# 🏡 2. Exercise 1 — ft_garden_name

**Directorio:** `ex1/`  
**Archivo de referencia:** `ft_garden_name.py`

### ▶️ Execution

Ejecuta `ft_garden_name()` mediante el helper e introduce los nombres indicados en las pruebas.

### 🔍 Functionality

- El archivo contiene una función llamada `ft_garden_name()` y no un programa principal.
- Muestra correctamente `Garden: [name]`, sustituyendo `[name]` por el nombre introducido.
- Muestra el mensaje de estado requerido. El PDF lo presenta como `Estado: ¡Creciendo bien!`.
- El nombre mostrado cambia con la entrada proporcionada.
- El archivo está en `ex1/`.

### 🧪 Tests

| Entrada | Esperado |
|---|---|
| `Jardín comunitario` | `Garden: Jardín comunitario` y el mensaje de estado requerido |
| `Mi jardín` | `Garden: Mi jardín` y el mensaje de estado requerido |
| Comparar ambas ejecuciones | El nombre refleja cada entrada y el estado conserva el formato exigido |

### 🧹 Code Quality — Exercise 1

- El código distingue correctamente el nombre variable del mensaje de estado fijo.
- El formato de salida coincide con el original.
- El código es legible y está bien estructurado.

---
---

# 📐 3. Exercise 2 — ft_plot_area

**Directorio:** `ex2/`  
**Archivo de referencia:** `ft_plot_area.py`

### ▶️ Execution

Ejecuta `ft_plot_area()` mediante el helper y prueba las parejas de longitud y anchura de la tabla.

### 🔍 Functionality

- El archivo contiene una función llamada `ft_plot_area()` y no un programa principal.
- Calcula el área mediante la **multiplicación de longitud por anchura**.
- Muestra el área calculada con el formato exacto exigido por el original.
- Los resultados se calculan a partir de las entradas.
- El archivo está en `ex2/`.

### 🧪 Tests

| Longitud | Anchura | Esperado |
|---|---|---|
| `10` | `5` | Área igual a `50` |
| `7` | `3` | Área igual a `21` |
| `1` | `1` | Área igual a `1` |

### 🧹 Code Quality — Exercise 2

- La operación utilizada es la multiplicación.
- La salida incluye el resultado correcto y el prefijo requerido.
- El PDF alterna entre «Área de parcela», «Área de la parcela» y «Área de trazo»: comprueba el literal en el original.

---
---

# 🧺 4. Exercise 3 — ft_harvest_total

**Directorio:** `ex3/`  
**Archivo de referencia:** `ft_harvest_total.py`

### ▶️ Execution

Ejecuta `ft_harvest_total()` mediante el helper y proporciona los valores de los tres días.

### 🔍 Functionality

- El archivo contiene una función llamada `ft_harvest_total()` y no un programa principal.
- Suma correctamente las cosechas de los **tres días**.
- Los valores iguales a cero se incluyen correctamente en el cálculo.
- La salida respeta el formato requerido, descrito en el PDF como `Cosecha total: X`.
- El archivo está en `ex3/`.

### 🧪 Tests

| Día 1 | Día 2 | Día 3 | Esperado |
|---|---|---|---|
| `5` | `8` | `3` | Cosecha total igual a `16` |
| `10` | `0` | `5` | Cosecha total igual a `15` |
| `0` | `0` | `0` | Cosecha total igual a `0` |

### 🧹 Code Quality — Exercise 3

- Se suman los tres valores, sin omitir ninguno.
- La operación y los nombres utilizados permiten entender el cálculo.
- La salida se construye a partir del total calculado.

---
---

# 🌿 5. Exercise 4 — ft_plant_age

**Directorio:** `ex4/`  
**Archivo de referencia:** `ft_plant_age.py`

### ▶️ Execution

Ejecuta `ft_plant_age()` mediante el helper y prueba las edades indicadas, especialmente `60` y `61`.

### 🔍 Functionality

- El archivo contiene una función llamada `ft_plant_age()` y no un programa principal.
- Una edad **mayor que 60** produce el mensaje de planta lista para cosechar.
- Una edad **igual o inferior a 60** produce el mensaje de que necesita más tiempo.
- La condición utiliza `> 60` o una expresión matemáticamente equivalente para las entradas del ejercicio.
- Se aceptan alternativas como `>= 61` para edades enteras o comparaciones con los operandos invertidos.
- El valor límite `60` queda en la rama correcta.
- El archivo está en `ex4/`.

### 🧪 Tests

| Edad | Esperado, según la traducción del PDF |
|---|---|
| `75` | `Planta está lista para cosechar!` |
| `60` | `La planta necesita más tiempo para crecer` |
| `61` | `Planta está lista para cosechar!` |
| `30` | `La planta necesita más tiempo para crecer` |

### 🧠 Concepts to check

- El alumno entiende la diferencia entre `>` y `>=`.
- Puede explicar por qué `60` y `61` producen resultados diferentes.
- El formato literal de ambos mensajes se comprueba con el original.

---
---

# 💧 6. Exercise 5 — ft_water_reminder

**Directorio:** `ex5/`  
**Archivo de referencia:** `ft_water_reminder.py`

### ▶️ Execution

Ejecuta `ft_water_reminder()` mediante el helper y prueba los días indicados, especialmente `2` y `3`.

### 🔍 Functionality

- El archivo contiene una función llamada `ft_water_reminder()` y no un programa principal.
- Si han pasado **más de 2 días**, muestra el recordatorio de riego.
- Con **2 días o menos**, muestra que las plantas están bien.
- La condición utiliza `> 2` o una expresión matemáticamente equivalente para las entradas del ejercicio.
- Se aceptan alternativas como `>= 3` para días enteros o comparaciones con los operandos invertidos.
- El valor límite `2` queda en la rama correcta.
- El archivo está en `ex5/`.

### 🧪 Tests

| Días | Esperado |
|---|---|
| `4` | Mensaje de que hay que regar las plantas |
| `2` | Mensaje de que las plantas están bien |
| `3` | Mensaje de que hay que regar las plantas |
| `1` | Mensaje de que las plantas están bien |

### 🧠 Concepts to check

- El alumno puede explicar la condición de riego.
- Distingue correctamente los casos límite `2` y `3`.
- La salida coincide con el original. El PDF traduce los mensajes como `¡Agua las plantas!` y `Las plantas están bien`, con inconsistencias de puntuación.

---
---

# 🔁 7. Exercise 6 — ft_count_harvest (Iterative)

**Archivo:** `ex6/ft_count_harvest_iterative.py`

### ▶️ Execution

Ejecuta `ft_count_harvest_iterative()` mediante el helper para `5`, `1` y `3` días.

### 🔍 Functionality

- Existe el archivo `ft_count_harvest_iterative.py` dentro de `ex6/`.
- Contiene una función llamada `ft_count_harvest_iterative()` y no un programa principal.
- Utiliza un enfoque **iterativo**, mediante un bucle `for` o `while`.
- Cuenta desde el día `1` hasta el número de días indicado, ambos incluidos.
- Muestra los días en orden, sin omisiones ni repeticiones.
- El mensaje final de cosecha aparece después del último día.

### 🧪 Iterative Tests

| Días | Secuencia esperada, según la traducción del PDF |
|---|---|
| `5` | `Día 1`, `Día 2`, `Día 3`, `Día 4`, `Día 5`, mensaje final de cosecha |
| `1` | `Día 1`, mensaje final de cosecha |
| `3` | `Día 1`, `Día 2`, `Día 3`, mensaje final de cosecha |

### 🧠 Concepts to check

- El alumno puede explicar el inicio, el avance y el final del bucle.
- El contador incluye el último día solicitado.
- El mensaje final aparece una sola vez, al terminar el conteo.
- El literal del mensaje final se verifica con el original; el PDF lo traduce como `Tiempo de cosecha!`.

---
---

# 🪆 8. Exercise 6 — ft_count_harvest (Recursive)

**Archivo:** `ex6/ft_count_harvest_recursive.py`

### ▶️ Execution

Ejecuta `ft_count_harvest_recursive()` mediante el helper para `5`, `1` y `3` días. Compara la salida con la versión iterativa para las mismas entradas.

### 🔍 Functionality

- Existe el archivo `ft_count_harvest_recursive.py` dentro de `ex6/`.
- Contiene una función llamada `ft_count_harvest_recursive()` y no un programa principal.
- Utiliza un enfoque **recursivo**: la función se llama a sí misma o utiliza una función auxiliar recursiva.
- Cuenta desde `1` hasta el número de días indicado, en orden ascendente.
- El mensaje final de cosecha aparece al terminar el conteo.
- Ambas versiones producen una **salida idéntica** para la misma entrada.

### 🧪 Recursive Tests

| Días / prueba | Esperado |
|---|---|
| `5` | Días del `1` al `5`, seguidos del mensaje final de cosecha |
| `1` | Día `1`, seguido del mensaje final de cosecha |
| `3` | Días del `1` al `3`, seguidos del mensaje final de cosecha |
| Comparación con la versión iterativa | Salida idéntica para cada entrada |
| Inspección del código | Existe recursión real, directa o mediante una función auxiliar |

### 🔎 Recursive Implementation Validation

- Existe una condición de terminación y las llamadas avanzan hacia ella.
- El orden de impresión produce el conteo ascendente solicitado.
- El mensaje de cosecha no se repite al regresar de cada llamada.
- **Se aceptan expresamente** funciones auxiliares anidadas, parámetros con valores por defecto y funciones auxiliares separadas llamadas por la función principal.
- No se rechaza una solución por utilizar una de estas variantes: la escala las autoriza explícitamente.

---
---

# 🌾 9. Exercise 7 — ft_seed_inventory

**Directorio:** `ex7/`  
**Archivo de referencia:** `ft_seed_inventory.py`

### ▶️ Execution

Utiliza el `main.py` proporcionado para ejecutar sus cuatro pruebas. Después, **crea una copia del helper**, cambia las cuatro pruebas y ejecuta esa copia para comprobar nuevos valores.

### 🔍 Functionality

- El archivo contiene una función llamada `ft_seed_inventory()` y no un programa principal.
- La función recibe el tipo de semilla, la cantidad y la unidad.
- Los parámetros tienen las anotaciones `str`, `int` y `str`, respectivamente, y el retorno está anotado como `None`.
- El PDF traduce algunos identificadores; conserva los nombres exactos de la firma indicada en el subject/helper original.
- Con la unidad `packets`, muestra la cantidad de paquetes disponibles.
- Con la unidad `grams`, muestra la cantidad total de gramos.
- Con la unidad de superficie, muestra la cantidad de metros cuadrados cubiertos. El PDF traduce esta unidad como `área`; comprueba el valor literal aceptado en el original.
- Ante una unidad desconocida, muestra **únicamente** el mensaje de unidad desconocida.
- Capitaliza correctamente el tipo de semilla en la salida.
- Los resultados se adaptan a los nuevos datos de la copia del helper.
- El archivo está en `ex7/`.
- Todas las funciones de este ejercicio tienen anotaciones apropiadas para sus parámetros y valores de retorno.

### 🧪 Inventory Tests

| Tipo de semilla | Cantidad | Unidad | Esperado |
|---|---|---|---|
| `tomato` | `15` | `packets` | Tipo de semilla capitalizado y `15` paquetes disponibles |
| Zanahoria, según el valor del helper original | `8` | `grams` | Tipo de semilla capitalizado y `8` gramos en total |
| `lettuce` | `12` | Unidad de superficie del helper original | Tipo de semilla capitalizado y cobertura de `12` metros cuadrados |
| El utilizado en la cuarta prueba del helper | La utilizada en esa prueba | Una unidad desconocida | Solo el mensaje de tipo de unidad desconocida |
| Las cuatro pruebas modificadas en una copia de `main.py` | Nuevas cantidades | Mantener cobertura de las cuatro ramas | Los resultados reflejan los nuevos datos |

### 🧹 Code Quality — Exercise 7

- Las ramas correspondientes a paquetes, gramos, superficie y unidad desconocida funcionan correctamente.
- El nombre de la semilla se capitaliza mediante una operación sobre la entrada.
- Los textos y las cantidades se generan a partir de los parámetros.
- Las anotaciones describen correctamente los tipos esperados y el retorno `None`.

---
---

# 🧹 10. Code Quality & Best Practices

## 🐍 Python

- Ejecuta `flake8` sobre **todos los archivos Python de la entrega**. Desde la raíz del repositorio:

```bash
flake8 .
```

- Revisa los errores y advertencias que aparezcan.
- Si un ejercicio tiene errores de `flake8`, **ese ejercicio suspende**. Corrige su calificación anterior si es necesario.
- **No se requieren docstrings para este módulo.**
- Todas las funciones están correctamente definidas y tienen los nombres solicitados.
- El código es legible y está bien estructurado.
- Los archivos están en los directorios correctos.
- Cada ejercicio se entrega como función, no como programa principal, respetando la excepción de auxiliares recursivos de `ex6`.
- Se comprueban las anotaciones de tipo exigidas en el apartado de `ex7`.

## 🧩 Python Fundamentals

- `print()` se utiliza correctamente para mostrar los resultados.
- Las operaciones aritméticas producen los valores esperados.
- Las condiciones sitúan correctamente los límites de edad y días sin riego.
- La versión iterativa utiliza un bucle y la recursiva utiliza recursión real.
- Las salidas coinciden con los formatos requeridos por el original.

## 🧠 Understanding & Learning

- Las soluciones demuestran los conceptos de Python previstos por la escala.
- El alumno puede explicar las decisiones principales de su código.
- Puede relacionar las entradas con las operaciones y las salidas obtenidas.
- Puede explicar las diferencias entre iteración y recursión.
- Las preguntas siguientes sirven para apoyar esa conversación, sin añadir criterios técnicos ajenos al PDF.

---
---

# 🚩 11. Defense

## 💬 Questions

1. ¿Qué diferencia hay entre definir una función y ejecutarla? ¿Qué papel cumple el helper `main.py`?
2. ¿Por qué `ft_hello_garden()` no necesita parámetros?
3. ¿Cómo se obtiene el nombre del jardín y cómo se incorpora a la salida?
4. ¿Cómo se calcula el área de la parcela? ¿Y la cosecha total de tres días?
5. ¿Por qué una planta de `60` días necesita más tiempo, pero una de `61` está lista?
6. ¿Por qué el recordatorio de riego cambia entre `2` y `3` días?
7. ¿Cómo consigue el bucle contar desde `1` hasta el último día incluido?
8. ¿Cuál es el caso base de la solución recursiva y cómo se alcanza?
9. ¿Dónde se imprime el mensaje final para que aparezca una sola vez?
10. ¿Qué significan las anotaciones `str`, `int` y `-> None` en el inventario?
11. ¿Cómo se capitaliza el tipo de semilla y qué ocurre con una unidad desconocida?
12. ¿Por qué conviene cambiar las cuatro pruebas en una copia de `main.py`?

## ⚠️ Stop conditions

Si se detecta una condición que obliga a finalizar la evaluación, utiliza la flag correspondiente de la escala:

- **Empty work →** No se ha presentado ningún trabajo.
- **Incomplete work →** El trabajo está incompleto.
- **Invalid compilation →** El código no puede compilarse o interpretarse correctamente.
- **Norme →** Incumplimiento de la norma aplicable. Los errores de `flake8` hacen suspender el ejercicio afectado según la regla específica de calidad.
- **Cheat →** Trampa o elementos no autorizados; la escala indica una calificación de **-42**.
- **Crash →** Terminación inesperada, prematura o no controlada del programa.
- **Concerning situation →** Situación preocupante.
- **Leaks →** Fugas de memoria.
- **Forbidden function →** Uso de una función no autorizada.
- **Can't support / explain code →** El alumno no puede defender o explicar su código.

La disponibilidad de una flag no añade por sí sola una prueba técnica al módulo. Aplica los criterios de la escala y del subject.

## 📝 Evaluation conclusion

- Revisa la valoración final y la flag seleccionada: evaluación correcta, proyecto excepcional o incidencia aplicable.
- Deja un comentario constructivo con los resultados y problemas encontrados.
- El comentario final de la escala tiene un máximo de **2048 caracteres**.
