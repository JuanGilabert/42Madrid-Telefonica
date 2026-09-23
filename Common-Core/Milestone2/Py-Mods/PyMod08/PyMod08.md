# 🚀 Python Module 08

## 📌 0. Guidelines

### ⚠️ Rules

- La revisión se realiza **en presencia del alumno evaluado**.
- Se debe mantener una actitud educada, respetuosa, constructiva y profesional durante toda la evaluación.
- La evaluación debe realizarse conjuntamente con el alumno, identificando, discutiendo y debatiendo los posibles problemas encontrados.
- Se debe tener en cuenta que puede haber distintas interpretaciones de las instrucciones del proyecto. La evaluación debe ser honesta y objetiva.
- Se evalúa únicamente el trabajo existente en el **repositorio Git del alumno**.
- Se debe comprobar que el repositorio pertenece al alumno o al grupo, que corresponde al proyecto correcto y que `git clone` se ejecuta en una carpeta vacía.
- No se deben utilizar alias maliciosos ni mecanismos que alteren el contenido que se está evaluando.
- El evaluador y el evaluado deben revisar los posibles scripts utilizados para facilitar la evaluación.
- Si el evaluador todavía no ha realizado este proyecto, debe leer previamente el subject completo.
- Si se detecta un repositorio vacío, un programa que no funciona, un error de norma, cheating u otra condición invalidante, se debe utilizar la flag correspondiente y la evaluación termina con nota **0**.
- Salvo que exista un archivo de configuración, no se debe modificar ningún archivo durante la evaluación.
- Si fuera necesario modificar un archivo, se deben explicar previamente los motivos y obtener el acuerdo del alumno.
- No se permite ninguna terminación inesperada, prematura o incontrolada del programa durante la defensa. En ese caso, se debe utilizar la flag correspondiente.

### 📁 Structure(posible preeliminares-basic)

- Deben existir las carpetas:
  - `ex0/`
  - `ex1/`
  - `ex2/`
- Cada carpeta debe contener los archivos requeridos por el subject.
- No debe haber archivos `.env` con secretos reales dentro del repositorio.
- Antes de comenzar la evaluación, se debe verificar que la estructura del proyecto coincide con la especificada en el subject.
- Si alguna comprobación preliminar falla, la evaluación se detiene y se utiliza la flag correspondiente.

### 🧰 General concepts to check

- El código se ejecuta correctamente sin errores inesperados.
- Los entornos virtuales se crean y utilizan correctamente.
- La gestión de dependencias mediante `pip` y Poetry se comprende y se aplica adecuadamente.
- Las dependencias faltantes se gestionan con mensajes claros y útiles.
- Se utilizan correctamente las variables de entorno.
- Los secretos no están hardcodeados ni incluidos en el repositorio.
- Se utiliza `python-dotenv` cuando corresponde.
- Se comprende la relación entre entornos virtuales, gestión de paquetes y configuración mediante variables de entorno.
- El código es compatible con **Python 3.10 o superior**.
- Todas las funciones y métodos tienen **type hints**.
- El código cumple los estándares de `flake8`.
- Los `docstrings` no son obligatorios para este módulo.

---
---
# 🛰️ 1. Exercise 0 — Virtual Environments (The Construct)

**Directory:** `ex0/`

### 📁 Required files

- `ex0/construct.py`

### ▶️ Execution

Se debe ejecutar el programa en los siguientes escenarios:

```bash
cd ex0
python3 construct.py
```

1. Ejecutar `construct.py` fuera de un entorno virtual.
2. Crear y activar un entorno virtual siguiendo las instrucciones mostradas por el programa.
3. Ejecutar `construct.py` de nuevo dentro del entorno virtual.

### 🔍 Functionality

El programa debe:

- Detectar correctamente si se está ejecutando dentro de un entorno virtual.
- Mostrar la salida correspondiente para cada escenario.
- Proporcionar instrucciones claras para crear un entorno virtual.
- Mostrar información relevante sobre las rutas utilizadas.
- Funcionar correctamente tanto fuera como dentro del entorno virtual.
- No terminar de forma inesperada ni producir errores no controlados.

### 🧪 Tests

| Prueba | Resultado esperado |
|---|---|
| Ejecutar fuera de un entorno virtual | Detecta y muestra que no hay entorno virtual activo |
| Ejecutar dentro de un entorno virtual | Detecta y muestra que el entorno virtual está activo |
| Crear el entorno virtual siguiendo las instrucciones | Se crea correctamente |
| Mostrar información de rutas | La información es clara y relevante |
| Ejecutar el programa en ambos escenarios | Las salidas son diferentes y correctas |
| Ejecución completa de `construct.py` | Finaliza correctamente |

### 🧠 Concepts to check

El alumno debe poder explicar:

1. ¿ Qué es un entorno virtual ?
2. ¿ Por qué son importantes los entornos virtuales ?
3. ¿ Qué problemas resuelven ?
4. ¿ Cómo detecta el programa si está dentro de un entorno virtual ?
5. ¿ Qué diferencias existen entre el intérprete del sistema y el intérprete del entorno virtual ?
6. ¿ Por qué no es recomendable instalar todas las dependencias globalmente ?

---
---
# 📦 2. Exercise 1 — Package Management (Loading Programs)

**Directory:** `ex1/`

### 📁 Required files

- `ex1/loading.py`
- `ex1/requirements.txt`
- `ex1/pyproject.toml`

### ▶️ Execution

Se debe comprobar la gestión de dependencias siguiendo estos pasos:

```bash
cd ex1
python3 loading.py
```

1. Intentar ejecutar `loading.py` sin tener instaladas las dependencias.
2. Instalar las dependencias mediante `pip` usando `requirements.txt`.
3. Ejecutar y probar la funcionalidad del programa.
4. Si Poetry está disponible, probar la instalación utilizando `pyproject.toml`.

### 🔍 Functionality

El programa debe:

- Gestionar correctamente la ausencia de dependencias.
- Mostrar mensajes de error claros y útiles cuando falten paquetes.
- Utilizar `numpy`, `pandas` y `matplotlib` según lo requerido.
- Generar algún tipo de análisis de datos o visualización.
- Mostrar información sobre las versiones de los paquetes.
- Funcionar correctamente después de instalar las dependencias.
- No depender de datos hardcodeados cuando se afirma que los datos se simulan mediante `numpy`.
- Simular datos con `numpy` o recuperarlos de una API, según lo implementado.
- Mostrar claramente la funcionalidad relacionada con la gestión de paquetes.

### 🧪 Tests

| Prueba | Resultado esperado |
|---|---|
| Ejecutar sin dependencias instaladas | Mensaje de error útil y controlado |
| Instalar con `pip` y `requirements.txt` | Las dependencias se instalan correctamente |
| Ejecutar con dependencias instaladas | El programa funciona correctamente |
| Utilizar `numpy` | Se emplea para generar o procesar datos |
| Utilizar `pandas` | Se emplea para análisis o manipulación de datos |
| Utilizar `matplotlib` | Se genera una visualización o representación gráfica |
| Mostrar versiones | Se muestran versiones relevantes de paquetes |
| Simular o recuperar datos | Los datos no están simplemente hardcodeados |
| Instalar mediante Poetry, si está disponible | La configuración funciona correctamente |
| Ejecución completa de `loading.py` | Finaliza correctamente |

### 📄 Dependency files

#### `requirements.txt`

Comprobar que:

- Contiene los paquetes requeridos.
- Las versiones están especificadas de forma apropiada, cuando corresponda.
- Incluye las dependencias necesarias para ejecutar el programa.
- No contiene dependencias innecesarias o incoherentes.

#### `pyproject.toml`

Comprobar que:

- Está correctamente formado para Poetry.
- Declara las dependencias necesarias.
- La configuración es coherente con el proyecto.
- Permite instalar las dependencias del proyecto mediante Poetry.

### 🧠 Concepts to check

El alumno debe poder explicar:

1. ¿ Cuál es la diferencia entre `pip` y Poetry ?
2. ¿ Por qué es importante gestionar las dependencias ?
3. ¿ Cómo gestiona el programa las dependencias que faltan ?
4. ¿ Qué ventajas aporta declarar las dependencias en un archivo ?
5. ¿ Cómo se simulan los datos con `numpy` ?
6. ¿ Cómo se recuperan datos desde una API, si se utiliza una ?
7. ¿ Por qué los datos no deben estar simplemente hardcodeados ?
8. ¿ Qué función cumplen `requirements.txt` y `pyproject.toml` ?

---
---
# 🔐 3. Exercise 2 — Environment Variables (The Oracle)

**Directory:** `ex2/`

### 📁 Required files

- `ex2/oracle.py`
- `ex2/requirements.txt`
- `ex2/.env.example`
- `ex2/.gitignore`

### ⚙️ Preliminary setup

Antes de comenzar las pruebas, pedir al alumno que realice personalmente los siguientes pasos:

1. Mostrar que `python-dotenv` está declarado en `requirements.txt`. Este archivo puede reutilizarse desde `ex1/`.
2. Crear un entorno virtual:

```bash
python3 -m venv .venv
```

3. Activar el entorno virtual:

```bash
source .venv/bin/activate
```

4. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

El evaluador **no debe instalar dependencias manualmente**. El alumno debe realizar y demostrar estos pasos.

### 🧪 Preliminary tests

| Prueba | Resultado esperado |
|---|---|
| `python-dotenv` declarado en `requirements.txt` | Está incluido correctamente |
| Crear el entorno virtual | Se crea correctamente |
| Activar el entorno virtual | El alumno lo realiza correctamente |
| Instalar las dependencias | La instalación finaliza correctamente |
| Preparar la ejecución de `oracle.py` | El entorno queda listo |

### ▶️ Execution

Se debe probar `oracle.py` en los siguientes escenarios:

```bash
cd ex2
python3 oracle.py
```

1. Ejecutar `oracle.py` sin variables de entorno configuradas.
2. Crear un archivo `.env` a partir de `.env.example`, utilizando valores de prueba.
3. Ejecutar el programa de nuevo y comprobar que carga la configuración.
4. Definir algunas variables directamente en la shell.
5. Ejecutar el programa y verificar el comportamiento.

### 🔍 Functionality

El programa debe:

- Utilizar `python-dotenv` para cargar archivos `.env`.
- Cargar la configuración desde variables de entorno.
- Utilizar el archivo `.env` para la configuración de desarrollo.
- Gestionar adecuadamente la ausencia de variables o configuración necesaria.
- Mostrar la configuración cargada sin exponer secretos reales.
- Distinguir correctamente entre configuración de desarrollo y configuración de producción.
- Priorizar o gestionar de forma coherente las variables definidas directamente en el entorno.
- No contener secretos hardcodeados en el código fuente.
- No provocar errores no controlados cuando falte configuración.

### 🧪 Environment and configuration tests

| Caso | Resultado esperado |
|---|---|
| Ejecutar sin variables de entorno | Se informa de la configuración ausente de forma controlada |
| Crear `.env` a partir de `.env.example` | Se puede crear una configuración de prueba |
| Ejecutar con `.env` | La configuración se carga correctamente |
| Definir variables en la shell | El programa las reconoce |
| Configuración incompleta | Se gestiona con un mensaje claro |
| Mostrar configuración | No se exponen secretos reales |
| Utilizar `python-dotenv` | Se utiliza correctamente |
| Ejecutar con configuración válida | El programa funciona correctamente |
| Ejecución completa de `oracle.py` | Finaliza correctamente |

### 🔒 Security Implementation

#### `.env.example`

Comprobar que:

- Contiene valores de ejemplo o plantillas y no secretos reales.
- Permite comprender qué variables necesita el programa.

#### `.gitignore`

Comprobar que:

- Excluye los archivos `.env`, evitando que los secretos de desarrollo se suban al repositorio.
- Contiene reglas adecuadas para la configuración local.

#### `oracle.py`

Comprobar que:

- No contiene secretos hardcodeados.
- Utiliza correctamente `python-dotenv`.
- Lee la configuración desde variables de entorno.
- Gestiona correctamente las variables ausentes.
- No muestra información sensible en la salida.

### 🧠 Concepts to check

El alumno debe poder explicar:

1. ¿ Por qué son importantes las variables de entorno para la seguridad ?
2. ¿ Por qué no se deben subir secretos al control de versiones ?
3. ¿ Qué diferencia existe entre configuración de desarrollo y configuración de producción ?
4. ¿ Cómo ayuda `python-dotenv` a gestionar la configuración ?
5. ¿ Cómo se comporta el programa cuando falta una variable necesaria ?
6. ¿ Cómo permiten las variables de entorno utilizar distintas configuraciones ?
7. ¿ Qué riesgos existen al guardar secretos directamente en el código ?
8. ¿ Qué papel desempeña `.gitignore` ?
9. ¿ Qué diferencia hay entre `.env` y `.env.example` ?

---
---
# 🧠 4. Overall Understanding & Best Practices

## 🔗 Understanding

Pedir al alumno que explique cómo trabajan conjuntamente estos tres conceptos en un proyecto real de ingeniería de datos:

- Entornos virtuales.
- Gestión de paquetes y dependencias.
- Variables de entorno.

El alumno debe poder explicar:

1. Por qué cada herramienta es importante en el desarrollo profesional.
2. Qué problemas aparecerían si no se utilizaran.
3. Cómo prepararía un nuevo proyecto de ingeniería de datos usando los tres conceptos.
4. Cómo aislaría las dependencias del proyecto.
5. Cómo instalaría y documentaría los paquetes necesarios.
6. Cómo gestionaría las configuraciones para desarrollo, pruebas y producción.
7. Cómo protegería las credenciales y secretos.
8. Cómo garantizaría que otro desarrollador pudiera reproducir el entorno.

La evaluación no debe limitarse a comprobar que el código funciona: el alumno debe comprender el **porqué** de las decisiones y ser capaz de explicarlas claramente.

## 🐍 Code Quality & Best Practices

- El código está escrito para **Python 3.10 o superior**.
- El código cumple los estándares de `flake8`.
- No existen errores relevantes de linting.
- Todas las funciones y métodos tienen **type hints** para parámetros y valores de retorno.
- Los type hints son comprobables mediante `mypy`.
- No se requieren `docstrings` para este módulo.
- El código es legible y está bien estructurado.
- Los errores y las dependencias ausentes se gestionan correctamente.
- Los casos límite están contemplados.
- Se siguen buenas prácticas de Python.
- La documentación y los mensajes mostrados son claros y útiles.
- La implementación refleja prácticas razonables de ingeniería de software y de ingeniería de datos.
- No se exponen secretos en la salida del programa.
- No se utilizan datos hardcodeados cuando el ejercicio exige simulación o carga de datos.
- La documentación del proyecto es clara y suficiente.

---
---
# 🚩 5. Defense

## 💬 Questions

1. ¿Qué es un entorno virtual?
2. ¿Por qué es importante utilizar un entorno virtual?
3. ¿Cómo detecta `construct.py` si está dentro de un entorno virtual?
4. ¿Qué diferencias existen entre un entorno virtual y la instalación global de paquetes?
5. ¿Qué problemas resuelve la gestión de dependencias?
6. ¿Cuál es la diferencia entre `pip` y Poetry?
7. ¿Qué función cumplen `requirements.txt` y `pyproject.toml`?
8. ¿Cómo se gestionan las dependencias que faltan?
9. ¿Por qué es importante especificar versiones de paquetes?
10. ¿Cómo se utilizan `pandas`, `numpy` y `matplotlib` en el ejercicio?
11. ¿Cómo se generan o recuperan los datos del programa?
12. ¿Por qué los datos no deben estar hardcodeados?
13. ¿Qué son las variables de entorno?
14. ¿Por qué son importantes para la seguridad?
15. ¿Qué función cumple `python-dotenv`?
16. ¿Qué diferencia existe entre `.env` y `.env.example`?
17. ¿Qué función cumple `.gitignore` en este contexto?
18. ¿Qué ocurre si falta una variable de entorno necesaria?
19. ¿Por qué no deben guardarse secretos en el código fuente?
20. ¿Cómo configurarías un proyecto para desarrollo y producción?
21. ¿Cómo se relacionan los entornos virtuales, las dependencias y las variables de entorno?
22. ¿Qué problemas aparecerían en un proyecto profesional si no se utilizasen estas herramientas?

## ⚠️ Stop conditions

Si se detecta una condición que obliga a finalizar la evaluación, debe utilizarse la flag correspondiente.

- **Empty work → El repositorio está vacío.**
- **Incomplete work → El trabajo está incompleto.**
- **Invalid compilation → El código no funciona o no puede ejecutarse correctamente.**
- **Norme → Se incumplen las normas de 42(42 norme).**
- **Cheat → Uso de cheats, alias maliciosos o elementos no autorizados.**
- **Concerning situation → Situación preocupante durante la evaluación.**
- **Leaks → Fugas de memoria.**
- **Forbidden function → Uso de una función no autorizada.**
- **Can't support / explain code → El alumno no puede justificar o explicar el código, lo que puede indicar plagio.**

