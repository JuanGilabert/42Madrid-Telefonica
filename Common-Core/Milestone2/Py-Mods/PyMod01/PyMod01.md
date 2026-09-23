# 🌱 Python Module 01

## 📌 0. Guidelines

### ⚠️ Rules

- La revisión se realiza **en presencia del alumno evaluado**.
- Mantén una actitud educada, respetuosa y constructiva. Comenta con el alumno los problemas encontrados y las posibles diferencias de interpretación del subject.
- Comprueba que el repositorio Git pertenece al alumno y corresponde al proyecto correcto.
- Comprueba que `git clone` se realiza en una carpeta vacía. Se evalúa únicamente el contenido existente en el **repositorio Git del alumno**.
- Si no hay contenido, la evaluación termina aquí: **Empty work**.
- No se han utilizado alias o scripts maliciosos para alterar el contenido evaluado.
- El evaluador y el evaluado han revisado los posibles scripts utilizados durante la evaluación.
- Si el evaluador no ha realizado todavía el proyecto, debe leer previamente el subject completo.
- No debería ser necesario modificar ningún archivo salvo el de configuración, si existe. Cualquier modificación debe explicarse y acordarse previamente con el evaluado.
- Si falta un archivo requerido o su nombre es incorrecto, la evaluación se detiene.
- Si se incumple cualquiera de las instrucciones generales de la escala, **la evaluación debe detenerse**.
- Todos los programas deben ejecutarse sin errores ni cierres inesperados. Una terminación inesperada, prematura o no controlada implica **0** y la flag correspondiente.
- Ante una incidencia que obliga a finalizar la evaluación, utiliza la flag apropiada. La escala establece **0**, o **-42 en caso de trampa**.
- Salvo en caso de trampa, se anima a continuar la discusión pedagógica para identificar los problemas y evitar que se repitan.

### 📁 Structure

- Comprueba que existen los siguientes archivos y que están correctamente nombrados.
- Si falta alguno o está mal nombrado, la evaluación termina aquí: **Incomplete work**.
- Comprueba que no hay archivos adicionales no autorizados.

```text
ex0/ft_garden_intro.py
ex1/ft_garden_data.py
ex2/ft_plant_growth.py
ex3/ft_plant_factory.py
ex4/ft_garden_security.py
ex5/ft_plant_types.py
ex6/ft_garden_analytics.py
```

### 🧰 General concepts to check

- El código está escrito para **Python 3.10 o superior**.
- El código cumple los estándares de `flake8`, sin errores.
- Se respetan las convenciones de nombres de funciones, clases y métodos.
- Todas las funciones y métodos tienen **type hints para parámetros y valores de retorno**. Compruébalo con `mypy`.
- **No se requieren docstrings para este módulo.**
- **No se exige validación de entradas salvo cuando se indica expresamente**, como en el ejercicio de encapsulación.
- Todos los programas se ejecutan sin errores ni crashes.
- Los ejercicios demuestran progresivamente estructura de programa, clases, métodos, inicialización, encapsulación, herencia y programación orientada a objetos avanzada.

> Guía basada en la escala **PyMod01Eval(1).pdf**. Los casos de prueba concretan sus comprobaciones; las preguntas apoyan la defensa. La escala no especifica todos los valores de ejemplo ni los literales de salida: comprueba esos detalles con el subject, sin añadir restricciones que no estén exigidas.

---
---

# 🌱 1. Exercise 0 — Planting Your First Seed (Program Structure)

**Archivo:** `ex0/ft_garden_intro.py`

### ▶️ Execution

```bash
python3 ex0/ft_garden_intro.py
```

### 🔍 Functionality

- El programa utiliza correctamente el patrón `if __name__ == "__main__":`.
- La información de la planta se almacena en **variables simples**.
- Se guardan los datos de **nombre, altura y edad**.
- Se utiliza `print()` para mostrar la información.
- La salida es legible y está bien formateada.
- La estructura del código es limpia y sencilla.

### 🧪 Tests

| Prueba | Esperado |
|---|---|
| Ejecutar el programa con `python3` | Muestra la información de la planta sin errores |
| Inspeccionar nombre, altura y edad | Los datos están almacenados en variables simples |
| Revisar el bloque `if __name__ == "__main__":` | Controla la ejecución del código de entrada del programa |
| Importar el módulo | El bloque protegido por esa condición no se ejecuta |
| Pedir al alumno que lance el programa con y sin shebang | Demuestra y explica las diferencias entre invocar el intérprete y ejecutar directamente el archivo |

### 🧠 Concepts to check

- El alumno puede explicar qué significa `if __name__ == "__main__":`.
- Puede explicar por qué este patrón es importante en Python.
- ¿Qué podría ocurrir si se elimina esa condición y se deja su contenido sin proteger?
- ¿En qué situación no se ejecuta el bloque protegido?
- Entiende que este patrón permite distinguir la ejecución directa de la importación.
- Puede explicar la función del shebang. Cualquier modificación para la demostración debe acordarse previamente.

---
---

# 🗂️ 2. Exercise 1 — Garden Data Organizer (Classes)

**Archivo:** `ex1/ft_garden_data.py`

### ▶️ Execution

```bash
python3 ex1/ft_garden_data.py
```

### 🔍 Functionality

- El programa **define y utiliza una clase**.
- Los datos de las plantas se organizan mediante **instancias de esa clase**.
- La definición de la clase utiliza la sintaxis correcta.
- Se crean objetos a partir de la clase.
- Las propiedades de las plantas se representan mediante atributos.
- La información de las plantas se muestra correctamente.
- La salida es legible y está bien formateada.

### 🧪 Tests

| Prueba | Esperado |
|---|---|
| Ejecutar el programa | Muestra correctamente la información de las plantas |
| Localizar la definición de la clase | Existe una clase con una estructura lógica y apropiada |
| Localizar la creación de instancias | El programa crea y utiliza objetos de la clase |
| Inspeccionar los atributos de las instancias | Contienen las propiedades de las plantas representadas |
| Relacionar los objetos con la salida | Los datos mostrados corresponden a las instancias utilizadas |

### 🧠 Concepts to check

- El alumno puede explicar qué es una clase y por qué la utiliza.
- Puede señalar dónde define la clase y dónde crea las instancias.
- Distingue entre **clase**, **instancia** y **atributo**.
- Entiende las clases como una herramienta para organizar datos.

---
---

# 📈 3. Exercise 2 — Plant Growth Simulator (Methods)

**Archivo:** `ex2/ft_plant_growth.py`

### ▶️ Execution

```bash
python3 ex2/ft_plant_growth.py
```

### 🔍 Functionality

- El programa utiliza **métodos para realizar acciones sobre las plantas**.
- Los métodos están definidos dentro de las clases.
- Se llaman los métodos sobre las instancias correspondientes.
- Las plantas pueden crecer y envejecer a lo largo del tiempo.
- La simulación muestra cambios durante **varios días**.
- La ejecución de los métodos modifica el estado de los objetos.
- Los cambios de estado persisten después de cada llamada.
- La salida muestra la progresión de las plantas a lo largo del tiempo.

### 🧪 Growth & State Tests

| Prueba | Esperado |
|---|---|
| Consultar el estado antes de una acción | Se identifican los valores iniciales de la planta |
| Llamar al método de crecimiento | La altura cambia según la lógica del ejercicio |
| Llamar al método de envejecimiento | La edad cambia según la lógica del ejercicio |
| Consultar el estado después de las llamadas | Los cambios permanecen en el objeto |
| Realizar varias llamadas consecutivas | Los cambios se acumulan correctamente |
| Ejecutar la simulación de varios días | La salida muestra la evolución temporal del estado |

### 🧠 Concepts to check

- El alumno puede explicar qué es un método y por qué lo utiliza.
- Puede demostrar cómo se llama a un método sobre una planta.
- Entiende los métodos como acciones que los objetos pueden realizar.
- Puede señalar qué atributos modifica cada método.
- La progresión mostrada corresponde a cambios reales del estado del objeto.

---
---

# 🏭 4. Exercise 3 — Plant Factory (Initialization)

**Archivo:** `ex3/ft_plant_factory.py`

### ▶️ Execution

```bash
python3 ex3/ft_plant_factory.py
```

### 🔍 Functionality

- El programa utiliza el método **`__init__` para inicializar los objetos**.
- Las plantas se crean con valores iniciales.
- Los parámetros proporcionados al crear cada objeto se utilizan para establecer sus atributos.
- Se pueden crear varias plantas con propiedades diferentes.
- Cada planta conserva los valores iniciales que le corresponden.
- La lógica de creación permite generar múltiples plantas de forma eficiente.
- Todas las plantas creadas funcionan correctamente.

### 🧪 Initialization Tests

| Prueba | Esperado |
|---|---|
| Crear una planta con valores iniciales concretos | Sus atributos contienen esos valores |
| Crear otra planta con propiedades distintas | Conserva sus propios valores iniciales |
| Inspeccionar `__init__` | Inicializa el estado a partir de los parámetros recibidos |
| Crear varias plantas mediante la lógica de fábrica | Se obtienen los objetos previstos con sus propiedades correspondientes |
| Mostrar o utilizar las plantas creadas | Todas funcionan correctamente |

### 🧠 Concepts to check

- El alumno puede explicar qué hace `__init__` y para qué se utiliza.
- Puede señalar dónde se establecen los valores iniciales de los atributos.
- Entiende el paso de parámetros durante la creación de objetos.
- Distingue entre crear una instancia e inicializar su estado.
- Puede explicar cómo la solución facilita crear múltiples plantas.

---
---

# 🔒 5. Exercise 4 — Garden Security System (Encapsulation)

**Archivo:** `ex4/ft_garden_security.py`

### ▶️ Execution

```bash
python3 ex4/ft_garden_security.py
```

### 🔍 Functionality

- El programa utiliza **encapsulación para proteger los datos**.
- Los atributos protegidos utilizan la convención del prefijo **`_`**.
- El acceso a los datos de la planta se controla mediante métodos.
- Se utilizan getters y setters para consultar y modificar los datos de forma controlada.
- Los datos se validan antes de permitir cambios.
- Los valores inválidos, como los negativos en los campos que no los admiten, se rechazan **tanto durante la inicialización como en actualizaciones posteriores**.
- Las actualizaciones válidas se realizan correctamente.
- Las operaciones inválidas generan mensajes apropiados y se gestionan sin provocar un cierre inesperado.
- Se mantiene la integridad de los datos de la planta.
- Se desaconseja modificar directamente los atributos protegidos.

### 🧪 Encapsulation & Validation Tests

| Caso | Esperado |
|---|---|
| Inicializar una planta con datos válidos | El estado inicial es válido |
| Intentar inicializar con un valor negativo no permitido | El valor se rechaza con el mensaje correspondiente; no se acepta un estado inválido |
| Consultar un dato mediante su getter | Devuelve el valor correspondiente |
| Actualizar un dato con un valor válido mediante su setter | El atributo se actualiza correctamente |
| Intentar una actualización con un valor negativo no permitido | La actualización se rechaza con un mensaje apropiado |
| Consultar el estado tras una actualización rechazada | El dato válido anterior se conserva |
| Revisar el uso de los atributos protegidos | Se utiliza el acceso controlado previsto por la clase |

### 🔎 Data Protection Validation

- La validación ocurre antes de aceptar un valor inválido.
- La protección se aplica al estado inicial y a las modificaciones posteriores.
- Los mensajes permiten entender por qué se ha rechazado la operación.
- El alumno puede explicar qué es la encapsulación y por qué es importante.
- Puede mostrar cómo ha protegido los datos mediante el prefijo `_` y los métodos de acceso.
- Entiende que `_` es una **convención de acceso protegido**, no una prohibición técnica de acceder al atributo desde fuera.

---
---

# 🌸 6. Exercise 5 — Specialized Plant Types (Inheritance)

**Archivo:** `ex5/ft_plant_types.py`

### ▶️ Execution

```bash
python3 ex5/ft_plant_types.py
```

### 🔍 Functionality

- El programa utiliza **herencia para crear tipos de plantas especializados**.
- Existe una clase base **`Plant`** con las características comunes.
- Existen las clases derivadas **`Flower`**, **`Tree`** y **`Vegetable`**, cuya clase padre es `Plant`.
- Cada tipo mantiene las características comunes y añade características especializadas.
- Se utiliza `super()` para llamar a métodos de la clase padre.
- Hay sobrescritura de métodos para adaptar el comportamiento, **al menos de `show()`**.
- La implementación de `show()` puede llamar a `super().show()` o sobrescribir completamente su comportamiento; ambas opciones están admitidas.
- Las funcionalidades especializadas relacionadas con floración, sombra y nutrición funcionan correctamente.
- La cadena de herencia funciona como se espera.

### 🧪 Inheritance & Specialized Behavior Tests

| Caso | Esperado |
|---|---|
| Inspeccionar `Plant` | Contiene las características comunes de las plantas |
| Crear una `Flower` | Hereda de `Plant` y dispone de su funcionalidad de floración |
| Crear un `Tree` | Hereda de `Plant` y dispone de su funcionalidad de sombra |
| Crear un `Vegetable` | Hereda de `Plant` y dispone de su funcionalidad de nutrición |
| Utilizar funcionalidades comunes en los tres tipos | Todos mantienen el comportamiento común correspondiente |
| Ejecutar los métodos especializados | Cada tipo realiza su acción específica correctamente |
| Llamar a `show()` en los tipos especializados | Se utiliza la versión sobrescrita correspondiente |
| Revisar las llamadas a `super()` | Reutilizan correctamente los métodos de la clase padre |

### 🧠 Concepts to check

- El alumno puede explicar qué es la herencia y por qué la utiliza.
- Puede señalar las relaciones padre-hijo entre las clases.
- Distingue los atributos y métodos comunes de los especializados.
- Puede explicar qué hace `super()`.
- Entiende la sobrescritura de métodos y su relación con la reutilización de código.

---
---

# 📊 7. Exercise 6 — Garden Analytics Platform (Advanced OOP)

**Archivo:** `ex6/ft_garden_analytics.py`

### ▶️ Execution

```bash
python3 ex6/ft_garden_analytics.py
```

### 🔍 Functionality

- El programa demuestra conceptos avanzados de programación orientada a objetos.
- Existen **clases anidadas**, definidas dentro de otras clases.
- Existen **cadenas de herencia de varios niveles**, como `A → B → C`.
- Se utilizan métodos de instancia, métodos de clase y métodos estáticos, distinguiendo su finalidad.
- Los métodos de clase se definen mediante `classmethod()` o `@classmethod`.
- Los métodos estáticos se definen mediante `staticmethod()` o `@staticmethod`.
- Existen funciones externas a las clases y se distingue su uso del de los métodos.
- La función independiente que muestra estadísticas funciona para cada tipo de `Plant`. Según la escala, recibe como parámetro un tipo de `Plant` y llama a la función de visualización de la **clase anidada que contiene las estadísticas**.
- Se demuestra la sobrescritura de clases anidadas y métodos a través de la herencia: por ejemplo, la clase anidada `N` de una clase derivada `B` sustituye a la `N` heredada de `A`.
- La cadena de herencia demuestra un uso correcto de `super()`.

### 🧪 Advanced OOP Tests

| Caso | Esperado |
|---|---|
| Utilizar la funcionalidad de la clase anidada | Funciona correctamente dentro del diseño del programa |
| Recorrer la cadena de herencia de varios niveles | Las clases mantienen y especializan el comportamiento previsto |
| Revisar las llamadas a `super()` | La delegación a través de la jerarquía es correcta |
| Llamar al método de clase destinado a crear instancias | Crea las instancias correspondientes |
| Llamar a un método estático desde la clase, sin crear una instancia | Funciona mediante la sintaxis habitual |
| Llamar a una función externa que opera sobre una instancia | Trabaja correctamente con el objeto recibido |
| Ejecutar la función independiente de estadísticas para cada tipo de `Plant` | Muestra las estadísticas mediante la función de visualización de la clase anidada correspondiente |
| Comprobar una clase anidada sobrescrita en una subclase | Se utiliza la definición correspondiente a la subclase |
| Comprobar los métodos sobrescritos | Se ejecuta el comportamiento especializado que corresponde |

### 🔎 Methods & Nested Classes Validation

- El alumno distingue entre un método de instancia, uno de clase, uno estático y una función externa.
- Puede justificar cuándo utilizar cada tipo de método.
- Los métodos de clase pueden crear instancias y se diferencian de los métodos ligados a una instancia.
- Los métodos estáticos funcionan sin una instancia y se diferencian de las funciones externas.
- Las funciones externas están definidas fuera de las clases y operan sobre los objetos previstos.
- La función de estadísticas delega realmente en la clase anidada correspondiente.
- Puede explicar la utilidad de las clases anidadas y cómo se sobrescriben a través de la herencia.
- Puede justificar las decisiones de diseño de la cadena de herencia.

---
---

# 🧹 8. Code Quality & Best Practices

## 🐍 Python

- El código está escrito para **Python 3.10 o superior**.
- Todos los programas se ejecutan sin errores ni crashes.
- El código cumple los estándares de `flake8`, sin errores.
- Todas las funciones y métodos tienen **type hints** para sus parámetros y valores de retorno.
- Se utiliza `mypy` para comprobar el tipado.
- **No se requieren docstrings para este módulo.**
- Se respetan las convenciones de nombres de Python para funciones, clases y métodos.
- El código es legible y está bien estructurado.
- Los outputs de las demostraciones son claros y están bien formateados.
- No se exige validación de entradas donde el ejercicio no la solicita expresamente.
- Si se incumple una instrucción general, la evaluación se detiene según la escala.

Comprobación de estilo desde la raíz del repositorio:

```bash
flake8 .
```

Comprobación de tipos, incluyendo funciones sin anotar. Se ejecuta por ejercicio para mantener independientes sus posibles definiciones de clases:

```bash
for exercise in ex0 ex1 ex2 ex3 ex4 ex5 ex6; do
    mypy --disallow-untyped-defs "$exercise"
done
```

## 🧩 Object-Oriented Programming

- Las clases organizan los datos de las plantas.
- Los métodos representan acciones y modifican el estado de las instancias cuando corresponde.
- `__init__` establece correctamente el estado inicial de cada objeto.
- La encapsulación controla las consultas y actualizaciones de datos.
- La validación del ejercicio 4 impide aceptar valores inválidos.
- La herencia permite compartir características y añadir comportamientos especializados.
- `super()` se utiliza correctamente en las jerarquías.
- La sobrescritura adapta métodos y, en el ejercicio avanzado, clases anidadas.
- Se distinguen los métodos de instancia, de clase, estáticos y las funciones externas.

## 🧠 Understanding & Learning

- Los ejemplos demuestran los conceptos requeridos en cada ejercicio.
- El alumno puede explicar las decisiones principales del código y mostrar dónde se implementan.
- Entiende la diferencia entre clase e instancia.
- Entiende cómo los métodos modifican y conservan el estado de los objetos.
- Puede explicar la inicialización, la encapsulación y la herencia.
- Puede justificar la elección de cada tipo de método y la estructura de las clases anidadas.
- Las demostraciones permiten comprobar el comportamiento real de los objetos.

---
---

# 🚩 9. Defense

## 💬 Questions

1. ¿Qué significa `if __name__ == "__main__":` y por qué es importante?
2. ¿Qué ocurriría al quitar esa condición? ¿Cuándo no se ejecuta su bloque?
3. ¿Para qué sirve un shebang y qué cambia al lanzar un archivo directamente o mediante `python3`?
4. ¿Qué es una clase? ¿Qué diferencia hay entre clase, instancia y atributo?
5. ¿Dónde defines tus clases y dónde creas sus instancias?
6. ¿Qué es un método y cómo cambia el estado de una planta al llamarlo varias veces?
7. ¿Qué hace `__init__` y cómo recibe los valores iniciales de una planta?
8. ¿Qué es la encapsulación y cómo proteges los datos durante la inicialización y las actualizaciones?
9. ¿Qué significa el prefijo `_`? ¿Impide técnicamente acceder a un atributo desde fuera?
10. ¿Cómo compruebas que una actualización inválida no altera el estado válido anterior?
11. ¿Qué relación tienen `Flower`, `Tree` y `Vegetable` con `Plant`?
12. ¿Qué hace `super()` y qué significa sobrescribir `show()`?
13. ¿Qué diferencias hay entre un método de instancia, uno de clase, uno estático y una función externa?
14. ¿Cuándo usarías cada tipo de método? ¿Cómo puede un método de clase crear instancias?
15. ¿Qué aporta una clase anidada y cómo puede una subclase sobrescribirla?
16. ¿Cómo funciona la cadena de herencia de tu plataforma de análisis?
17. ¿Cómo consigue la función externa mostrar las estadísticas correspondientes a cada tipo de planta?

## ⚠️ Stop conditions

Si se detecta una condición que obliga a finalizar la evaluación, debe utilizarse la flag correspondiente.

- **Empty work →** El trabajo es inexistente.
- **Incomplete work →** El trabajo está incompleto; falta un archivo requerido o está mal nombrado.
- **Invalid compilation →** El código no puede compilarse o interpretarse correctamente.
- **Norme →** Incumplimiento de la norma aplicable.
- **Cheat →** Trampa o uso de elementos no autorizados.
- **Crash →** Terminación inesperada, prematura o no controlada del programa.
- **Concerning situation →** Situación preocupante.
- **Leaks →** Fugas de memoria.
- **Forbidden function →** Uso de una función no autorizada.
- **Can't support / explain code →** El alumno no puede defender o explicar su código.

La escala exige detener la evaluación si falta un archivo, su nombre es incorrecto o se incumple una instrucción general. Ante las incidencias que dan por terminada la calificación, establece **0**, o **-42 en caso de trampa**. La incapacidad de explicar el código no demuestra por sí sola que exista plagio.

## 📝 Evaluation conclusion

- Revisa la valoración final: **Ok**, **Outstanding project** o la flag de incidencia correspondiente.
- Deja un comentario constructivo con los resultados de la evaluación y los problemas encontrados.
- El comentario final admite un máximo de **2048 caracteres**.
