# 🚀 Call Me Maybe

## 🚀 Call Me Maybe Project

### Introducción a la llamada de funciones en LLM

**Resumen:** ¿Hablan los LLM el lenguaje de los ordenadores? Vamos a descubrirlo.

*Creado en colaboración con @ldevelle, @pcamaren y @crfernan.*

**Versión:** 1.5

---

### Índice

1. [Prólogo](#1-prólogo)
2. [Instrucciones sobre IA](#2-instrucciones-sobre-ia)
3. [Introducción](#3-introducción)
   - [¿Qué es la llamada de funciones?](#31-qué-es-la-llamada-de-funciones)
   - [¿Por qué es importante?](#32-por-qué-es-importante)
   - [El desafío](#33-el-desafío)
4. [Instrucciones comunes](#4-instrucciones-comunes)
   - [Reglas generales](#41-reglas-generales)
   - [Makefile](#42-makefile)
   - [Directrices adicionales](#43-directrices-adicionales)
   - [Requisitos adicionales](#431-requisitos-adicionales)
   - [Uso](#432-uso)
5. [Parte obligatoria](#5-parte-obligatoria)
   - [Resumen](#51-resumen)
   - [Archivos de entrada](#52-archivos-de-entrada)
   - [Interacción con el LLM](#53-interacción-con-el-llm)
   - [Formato del archivo de salida](#54-formato-del-archivo-de-salida)
   - [Rendimiento y fiabilidad](#55-rendimiento-y-fiabilidad)
   - [Prueba de la implementación](#56-prueba-de-la-implementación)
6. [Requisitos del README](#6-requisitos-del-readme)
7. [Parte extra](#7-parte-extra)
8. [Entrega y evaluación entre compañeros](#8-entrega-y-evaluación-entre-compañeros)

---

### 1. Prólogo

Los ingenieros romanos tallaban tablas de piedra con cuadrículas perfectas para llevar el control de los envíos de grano por todo el imperio, de modo que ninguna entrega se perdiera por una mala caligrafía. En el siglo XIX, los marineros registraban las corrientes oceánicas en tablas estructuradas y tan precisas que algunas todavía se utilizan hoy en navegación.

Los primeros pronósticos meteorológicos se enviaban por telégrafo mediante un código fijo: unos pocos números podían describir todo un cielo. En la década de 1960, el centro de control de misiones de la NASA trabajaba con diagramas de flujo plastificados que indicaban exactamente qué significaba cada luz parpadeante, independientemente de quién estuviera de turno. Los lectores de códigos de barras de los supermercados traducían franjas blancas y negras en datos de inventario mucho antes de que la mayoría de los hogares tuviera ordenadores. Incluso los apicultores llevan décadas utilizando formularios estandarizados para registrar la salud de las colmenas, el flujo de néctar y la genealogía de las reinas en pequeñas casillas que pueden interpretar de un vistazo.

La humanidad siempre ha creado estructuras para que la información sea fiable, compartible y útil. Y eso nos lleva al presente, donde el objetivo es conseguir que la IA hable el lenguaje de los ordenadores.

### 2. Instrucciones sobre IA

#### Contexto

Durante tu proceso de aprendizaje, la IA puede ayudarte con muchas tareas diferentes. Dedica tiempo a explorar las distintas capacidades de las herramientas de IA y cómo pueden contribuir a tu trabajo. Sin embargo, utilízalas siempre con cautela y evalúa críticamente sus resultados. Ya se trate de código, documentación, ideas o explicaciones técnicas, nunca puedes estar completamente seguro de que tu pregunta estuviera bien planteada o de que el contenido generado sea correcto. Tus compañeros son un recurso valioso para ayudarte a evitar errores y puntos ciegos.

#### Mensaje principal

- Utiliza la IA para reducir las tareas repetitivas o tediosas.
- Desarrolla habilidades para redactar *prompts*, tanto relacionados con la programación como con otros ámbitos, que te resultarán útiles en tu futuro profesional.
- Aprende cómo funcionan los sistemas de IA para anticipar y evitar mejor los riesgos, sesgos y problemas éticos habituales.
- Sigue desarrollando tus habilidades técnicas y tus competencias transversales trabajando con tus compañeros.
- Utiliza únicamente contenido generado por IA que comprendas por completo y del que puedas responsabilizarte.

#### Reglas para el estudiante

- Dedica tiempo a explorar las herramientas de IA y comprender cómo funcionan, para poder utilizarlas de forma ética y reducir los posibles sesgos.
- Reflexiona sobre el problema antes de escribir un *prompt*. Esto te ayudará a formular instrucciones más claras, detalladas y pertinentes, utilizando vocabulario preciso.
- Adquiere el hábito de comprobar, revisar, cuestionar y probar sistemáticamente todo lo que genere la IA.
- Busca siempre la revisión de tus compañeros: no confíes únicamente en tu propia validación.

#### Resultados de la fase

- Desarrollar habilidades para crear *prompts* de propósito general y específicos de cada ámbito.
- Aumentar tu productividad mediante el uso eficaz de herramientas de IA.
- Seguir reforzando el pensamiento computacional, la resolución de problemas, la adaptabilidad y la colaboración.

#### Comentarios y ejemplos

- Te encontrarás con frecuencia en situaciones —exámenes, evaluaciones y otras— en las que tendrás que demostrar que comprendes realmente el contenido. Prepárate y sigue desarrollando tus habilidades técnicas e interpersonales.
- Explicar tu razonamiento y debatir con tus compañeros suele revelar lagunas en tu comprensión. Da prioridad al aprendizaje entre compañeros.
- Las herramientas de IA a menudo carecen del contexto específico de tu situación y tienden a ofrecer respuestas genéricas. Tus compañeros, que comparten tu entorno, pueden aportar información más pertinente y precisa.
- Mientras que la IA tiende a generar la respuesta más probable, tus compañeros pueden ofrecer perspectivas alternativas y matices valiosos. Recurre a ellos como punto de control de calidad.

##### ✓ Buena práctica

Le pregunto a la IA: «¿Cómo puedo probar una función de ordenación?». Me da algunas ideas. Las pruebo y reviso los resultados con un compañero. Juntos perfeccionamos el enfoque.

##### ✗ Mala práctica

Le pido a la IA que escriba una función completa y la copio y pego en mi proyecto. Durante la evaluación entre compañeros, no puedo explicar qué hace ni por qué. Pierdo credibilidad y suspendo el proyecto.

##### ✓ Buena práctica

Utilizo la IA para ayudarme a diseñar un analizador (*parser*). Después repaso la lógica con un compañero. Detectamos dos errores y reescribimos el código juntos: queda mejor, más limpio y lo comprendemos por completo.

##### ✗ Mala práctica

Dejo que Copilot genere código para una parte clave de mi proyecto. Compila, pero no puedo explicar cómo gestiona las tuberías (`|`). Durante la evaluación no consigo justificarlo y suspendo el proyecto.

### 3. Introducción

#### 3.1. ¿Qué es la llamada de funciones?

Los modelos de lenguaje grandes (*Large Language Models*, LLM) son muy buenos comprendiendo y generando lenguaje humano, pero no producen de forma natural salidas estructuradas que puedan ejecutar las máquinas. La llamada de funciones (*function calling*) cierra esa brecha al traducir solicitudes en lenguaje natural en llamadas a funciones precisas, con argumentos tipados.

Considera este ejemplo: de lenguaje natural a una llamada de función.

**Usuario:** «¿Cuánto suman 40 y 2?»

**LLM tradicional:** «La suma de 40 y 2 es 42».

**Sistema de llamada de funciones:**

```json
{
  "function": "add_numbers",
  "arguments": {"a": 40, "b": 2}
}
```

El sistema de llamada de funciones no responde directamente a la pregunta. En su lugar, proporciona las herramientas para resolverla: el nombre de la función adecuado y los argumentos correctos con sus tipos correspondientes.

#### 3.2. ¿Por qué es importante?

La llamada de funciones permite a los LLM:

- **Interactuar con sistemas externos:** llamar a API, consultar bases de datos y controlar dispositivos.
- **Ejecutar código:** realizar cálculos, transformar datos y operar con archivos.
- **Encadenar operaciones:** dividir tareas complejas en pasos ejecutables.
- **Producir salidas estructuradas:** generar JSON, XML u otros formatos legibles por máquinas.
- **Extraer datos estructurados de texto no estructurado:** por ejemplo, extraer de un libro extenso campos como `{nombre del protagonista, sexo del protagonista, edad del protagonista}`.

Esta tecnología impulsa los asistentes de IA modernos, las herramientas de generación de código y los agentes autónomos. También permite tareas como la extracción automática de información y la estructuración del conocimiento a partir de texto sin procesar.

#### 3.3. El desafío

Los modelos de lenguaje pequeños —como el modelo de 0,6 mil millones de parámetros que utilizarás— son notoriamente poco fiables al generar salidas estructuradas. Cuando se les pide que produzcan JSON, quizá solo lo consigan el 30 % de las veces. Sin embargo, los sistemas de producción alcanzan una fiabilidad superior al 99 % con esos mismos modelos pequeños.

¿Cómo? La respuesta está en la **decodificación restringida** (*constrained decoding*): una técnica que guía la salida del modelo token a token para garantizar una estructura válida, sin depender únicamente de las instrucciones del *prompt*.

### 4. Instrucciones comunes

#### 4.1. Reglas generales

- El proyecto debe estar escrito en Python 3.10 o posterior.
- El proyecto debe cumplir el estándar de estilo de código `flake8`.
- Las funciones deben gestionar las excepciones correctamente para evitar cierres inesperados. Utiliza bloques `try-except` para gestionar posibles errores. Da preferencia a los gestores de contexto para recursos como archivos o conexiones, a fin de garantizar su liberación automática. Si el programa se bloquea por excepciones no controladas durante la revisión, se considerará que no funciona.
- Todos los recursos (por ejemplo, descriptores de archivos y conexiones de red) deben gestionarse correctamente para evitar fugas. Cuando sea posible, utiliza gestores de contexto para automatizar esta gestión.
- El código debe incluir anotaciones de tipos para los parámetros, los valores de retorno y las variables cuando corresponda (mediante el módulo `typing`). Utiliza `mypy` para la comprobación estática de tipos. Todas las funciones deben superar `mypy` sin errores.
- Incluye *docstrings* en las funciones y clases siguiendo PEP 257 (por ejemplo, el estilo de Google o NumPy) para documentar su finalidad, parámetros y valores de retorno.

#### 4.2. Makefile

Incluye un `Makefile` en el proyecto para automatizar tareas habituales. Debe contener las siguientes reglas (el *lint* obligatorio implica los indicadores especificados; se recomienda encarecidamente probar `--strict` para realizar comprobaciones más exhaustivas):

- `install`: instalar las dependencias del proyecto mediante `pip`, `uv`, `pipx` o cualquier otro gestor de paquetes que elijas.
- `run`: ejecutar el script principal del proyecto (por ejemplo, mediante el intérprete de Python).
- `debug`: ejecutar el script principal en modo depuración utilizando el depurador integrado de Python (por ejemplo, `pdb`).
- `clean`: eliminar archivos temporales o cachés (por ejemplo, `__pycache__` y `.mypy_cache`) para mantener limpio el entorno del proyecto.
- `lint`: ejecutar los comandos `flake8 .` y `mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs`.
- `lint-strict` (opcional): ejecutar los comandos `flake8 .` y `mypy . --strict`.

#### 4.3. Directrices adicionales

- Crea programas de prueba para verificar la funcionalidad del proyecto (no se entregan ni se califican). Utiliza marcos de pruebas como `pytest` o `unittest` para las pruebas unitarias y cubre los casos límite.
- Incluye un archivo `.gitignore` para excluir los artefactos de Python.
- Se recomienda utilizar entornos virtuales (por ejemplo, `venv` o `conda`) para aislar las dependencias durante el desarrollo.

Si existen requisitos adicionales específicos del proyecto, se indicarán inmediatamente a continuación de esta sección.

##### 4.3.1. Requisitos adicionales

- Todas las clases deben utilizar `pydantic` para la validación.
- Puedes utilizar los paquetes `numpy` y `json`.
- Está completamente prohibido utilizar `dspy` (o cualquier paquete similar), incluidos `pytorch`, `huggingface`, `transformers`, `outlines`, etc.
- Debes utilizar los siguientes modelos:
  - `Qwen/Qwen3-0.6B` (predeterminado).
  - Puedes utilizar otros modelos, siempre que el proyecto funcione con `Qwen/Qwen3-0.6B`.
- La función que se debe llamar debe seleccionarse mediante el LLM, no mediante heurísticas ni ningún otro tipo de magia anticuada.
- Está prohibido utilizar métodos o atributos privados del paquete `llm_sdk`.
- Debes crear un entorno virtual e instalar los paquetes `numpy` y `pydantic` mediante `uv`. Para utilizar `llm_sdk`, puedes copiarlo al mismo directorio en el que se encuentra `src`.
- Tanto la persona evaluadora como la *moulinette* ejecutarán únicamente `uv sync`.
- Todos los errores deben gestionarse correctamente. El programa nunca debe bloquearse de forma inesperada y siempre debe mostrar mensajes de error claros al usuario.

##### 4.3.2. Uso

El programa debe ejecutarse con el siguiente comando (donde `src` es la carpeta que contiene tus archivos):

```bash
uv run python -m src [--functions_definition <function_definition_file>] [--input <input_file>] [--output <output_file>]
```

Por defecto, el programa leerá los archivos de entrada del directorio `data/input/` y escribirá los resultados en `data/output/`. Puedes especificar rutas personalizadas mediante los argumentos `--input` y `--output`. Por ejemplo:

```bash
uv run python -m src \
  --functions_definition data/input/functions_definition.json \
  --input data/input/function_calling_tests.json \
  --output data/output/function_calls.json
```

### 5. Parte obligatoria

#### 5.1. Resumen

En este proyecto crearás una herramienta de llamada de funciones que traduzca *prompts* en lenguaje natural a llamadas de funciones estructuradas. Ante una pregunta como «¿Cuánto suman 40 y 2?», tu solución no debe devolver `42`, sino proporcionar:

- El nombre de la función: `fn_add_numbers`.
- Los argumentos: `{"a": 40, "b": 2}`.

La implementación debe utilizar decodificación restringida para garantizar una salida JSON válida al 100 %, lo que permite una fiabilidad prácticamente perfecta incluso con un modelo pequeño de 0,6 mil millones de parámetros.

#### 5.2. Archivos de entrada

La solución procesará dos archivos de entrada situados en el directorio `data/input/`.

##### `function_calling_tests.json`

Contiene un array JSON de *prompts* en lenguaje natural que el sistema debe procesar.

Ejemplo:

```json
[
  {"prompt": "What is the sum of 2 and 3?"},
  {"prompt": "What is the sum of 265 and 345?"},
  {"prompt": "Greet shrek"},
  {"prompt": "Greet john"},
  {"prompt": "Reverse the string 'hello'"},
  ...
]
```

##### `functions_definition.json`

Contiene las funciones disponibles que el sistema puede llamar. Cada función incluye:

- Nombre de la función.
- Nombres y tipos de los argumentos.
- Tipo de retorno.
- Descripción.

Ejemplo:

```json
[
  {
    "name": "fn_add_numbers",
    "description": "Add two numbers together and return their sum.",
    "parameters": {
      "a": {"type": "number"},
      "b": {"type": "number"}
    },
    "returns": {"type": "number"}
  },
  {
    "name": "fn_greet",
    "description": "Generate a greeting message for a person by name.",
    "parameters": {
      "name": {"type": "string"}
    },
    "returns": {"type": "string"}
  },
  {
    "name": "fn_reverse_string",
    "description": "Reverse a string and return the reversed result.",
    "parameters": {
      "s": {"type": "string"}
    },
    "returns": {"type": "string"}
  }
]
```

Estos ejemplos establecen el nivel de complejidad esperado. Sin embargo, la solución se probará con distintos *prompts* y conjuntos de funciones. Debes implementar una gestión adecuada de errores JSON en los archivos de entrada, ya que podrían contener JSON no válido o no existir.

#### 5.3. Interacción con el LLM

##### 5.3.1. El SDK del LLM

Junto con este proyecto encontrarás una clase envoltorio `Small_LLM_Model` en el paquete `llm_sdk`, que puedes utilizar para interactuar con el LLM.

El SDK proporciona varios métodos esenciales:

- `get_logits_from_input_ids(input_ids: List[int]) -> List[float]`: recibe una lista de identificadores de tokens y devuelve los *logits* generados por el modelo LLM.
- `get_path_to_vocab_file() -> str`: devuelve la ruta al archivo de vocabulario que contiene la correspondencia entre los identificadores y los tokens.
- `encode(text: str) -> Tensor`: codifica una cadena de texto en un tensor de identificadores de tokens mediante el tokenizador del modelo.
- `decode(token_ids: List[int]) -> str` (opcional): decodifica una lista de identificadores de tokens y la convierte de nuevo en una cadena de texto.

##### 5.3.2. El proceso de generación

El proceso de generación del LLM sigue estos pasos:

1. **Prompt:** la pregunta en lenguaje natural.  
   Ejemplo: `What is the sum of 2 and 3?`
2. **Tokenización:** el texto se divide en unidades de subpalabra (*tokens*). A diferencia de una simple división por palabras, los tokenizadores suelen incluir espacios iniciales, gestionar la puntuación y dividir palabras en componentes más pequeños mediante algoritmos como BPE o SentencePiece.  
   Ejemplo realista: `["What", "Ġis", "Ġthe", "Ġsum", "Ġof", "Ġ2", "Ġand", "Ġ3", "?"]`  
   Nota: el símbolo `Ġ` indica que hay un espacio delante; los tokenizadores reales conservan estos detalles para reconstruir el texto con precisión.
3. **Identificadores de entrada:** los tokens se convierten en identificadores numéricos que el modelo puede interpretar.  
   Ejemplo ilustrativo: `[892, 318, 262, 4771, 286, 16, 290, 17, 30]`.
4. **Procesamiento del LLM:** el modelo procesa estos números mediante su red neuronal.
5. **Logits:** el modelo genera puntuaciones de probabilidad para cada posible token siguiente.  
   Ejemplo: `token_5: 0.001`, `token_42: 0.85`, `token_100: 0.02`, etc.
6. **Selección del token:** el siguiente token se elige en función de esas probabilidades, normalmente el de mayor puntuación. En esta etapa pueden aplicarse técnicas como la decodificación restringida para limitar los tokens posibles y garantizar que la salida siga una estructura específica, como JSON válido al 100 %.

**Importante:** este proceso se repite token a token. Cada token generado se añade al *prompt* y se repiten los pasos 2 a 6 hasta producir la respuesta completa.

Vista simplificada:

```text
Prompt -> Tokenización -> Identificadores de entrada -> LLM -> Logits -> Selección del siguiente token
```

##### 5.3.3. Comprender la decodificación restringida

Los modelos de lenguaje generan texto token a token. En cada paso, el modelo produce una distribución de probabilidades (*logits*) sobre todos los posibles tokens siguientes. Normalmente, se muestrea de esa distribución o se elige el token con mayor probabilidad.

La decodificación restringida interviene en el proceso modificando los *logits* antes de seleccionar el token:

1. El modelo produce *logits* para todos los tokens posibles.
2. Se identifican los tokens que mantienen una estructura JSON válida y cumplen el esquema esperado.
3. Se asigna el valor de infinito negativo a los *logits* de los tokens no válidos (los que romperían el esquema o la estructura).
4. Se selecciona un token únicamente entre los que siguen siendo válidos.

En este proyecto, la decodificación restringida no solo debe garantizar que el JSON sea sintácticamente válido, sino también imponer un esquema específico. Por ejemplo, si un campo está restringido a un número en `functions_definition.json`, el decodificador limita la selección a valores que sean un entero o un número decimal, manteniendo tanto la validez JSON como el cumplimiento del esquema. Así se garantiza que cada token generado preserve la validez estructural y semántica y cumpla el esquema requerido. Como resultado, el JSON producido siempre puede recuperarse y analizarse sin errores.

> **Tu solución no debe confiar en que el modelo produzca JSON correcto espontáneamente.** Pedir al modelo, mediante un *prompt*, que utilice las definiciones de las funciones y esperar una salida estructurada no es fiable, y no es la habilidad que se espera que desarrolles aquí.

> Piensa cómo utilizar el archivo JSON del vocabulario para relacionar los tokens con sus representaciones en texto. Esto es crucial para determinar qué tokens son válidos en cada paso de la generación.

#### 5.4. Formato del archivo de salida

El programa producirá un único archivo JSON: `data/output/function_calling_results.json`.

Por cada *prompt*, añade un objeto JSON a ese archivo. Cada objeto del array debe contener exactamente las siguientes claves:

- `prompt` (cadena): la solicitud original en lenguaje natural.
- `name` (cadena): el nombre de la función que se debe llamar.
- `parameters` (objeto): todos los argumentos requeridos con los tipos correctos.

##### 5.4.1. Ejemplo de salida

```json
[
  {
    "prompt": "What is the sum of 2 and 3?",
    "name": "fn_add_numbers",
    "parameters": {"a": 2.0, "b": 3.0}
  },
  {
    "prompt": "Reverse the string 'hello'",
    "name": "fn_reverse_string",
    "parameters": {"s": "hello"}
  }
]
```

##### 5.4.2. Reglas de validación

- El archivo debe contener JSON válido (sin comas finales ni comentarios).
- Las claves y los tipos deben coincidir exactamente con el esquema de `functions_definition.json`.
- No se permiten claves adicionales ni texto explicativo en ninguna parte de la salida.
- Deben estar presentes todos los argumentos requeridos.
- Los tipos de los argumentos deben coincidir con la definición de la función (número, cadena, booleano, etc.).

> Los archivos de entrada proporcionados pueden cambiar durante la evaluación entre compañeros. No codifiques soluciones rígidas basadas en los ejemplos proporcionados.

#### 5.5. Rendimiento y fiabilidad

La implementación debería alcanzar:

- **Precisión casi perfecta:** más del 90 % de aciertos en la selección de funciones y la extracción de argumentos.
- **JSON válido al 100 %:** todas las salidas deben poder analizarse y cumplir el esquema.
- **Velocidad razonable:** procesar todos los *prompts* de prueba en menos de 5 minutos en hardware estándar.
- **Gestión de errores robusta:** gestionar correctamente entradas mal formadas, archivos inexistentes y casos límite.

> El modelo Qwen3-0.6B solo tiene 500 millones de parámetros, pero, con una decodificación restringida adecuada, puede lograr una fiabilidad comparable a la de modelos mucho mayores. Esto demuestra el poder de la guía estructural frente al tamaño bruto del modelo.

#### 5.6. Prueba de la implementación

Para comprobar que la solución funciona:

1. Asegúrate de que los archivos de entrada estén en `data/input/`.
2. Ejecuta:

   ```bash
   uv run python -m src [--functions_definition <function_definition_file>] [--input <input_file>] [--output <output_file>]
   ```

3. Comprueba que se haya creado `output/function_calling_results.json`.
4. Valida la estructura y el contenido del JSON.
5. Verifica que los nombres de las funciones y los tipos de los argumentos coincidan con las definiciones.

> Prueba diversos casos límite: cadenas vacías, números grandes, caracteres especiales, tipos incorrectos, *prompts* ambiguos y funciones con varios parámetros.

### 6. Requisitos del README

Debe incluirse un archivo `README.md` en la raíz del repositorio Git. Su objetivo es permitir que cualquier persona que no conozca el proyecto (compañeros, personal docente, reclutadores, etc.) entienda rápidamente de qué trata, cómo ejecutarlo y dónde encontrar más información.

El `README.md` debe incluir, como mínimo:

- La primera línea debe estar en cursiva y decir exactamente:  
  `This project has been created as part of the 42 curriculum by <login1>[, <login2>[, <login3>[...]]].`
- Una sección **Description** que presente claramente el proyecto, su objetivo y una breve descripción general.
- Una sección **Instructions** con la información pertinente sobre compilación, instalación o ejecución.
- Una sección **Resources** que enumere referencias habituales relacionadas con el tema (documentación, artículos, tutoriales, etc.) y describa cómo se ha utilizado la IA, especificando para qué tareas y partes del proyecto.

Pueden ser necesarias otras secciones según el proyecto (por ejemplo, ejemplos de uso, lista de funcionalidades o decisiones técnicas). Los requisitos adicionales que sean obligatorios se indicarán explícitamente a continuación.

Para este proyecto, el `README.md` también debe incluir:

- **Explicación del algoritmo:** describir detalladamente el enfoque de decodificación restringida.
- **Decisiones de diseño:** explicar las decisiones principales de la implementación.
- **Análisis del rendimiento:** comentar la precisión, la velocidad y la fiabilidad de la solución.
- **Dificultades encontradas:** documentar los problemas surgidos y cómo se resolvieron.
- **Estrategia de pruebas:** describir cómo se validó la implementación.
- **Ejemplos de uso:** ofrecer ejemplos claros de ejecución del programa.

> **El README debe estar escrito en inglés.**

### 7. Parte extra

Consulta las funcionalidades extra opcionales (no son necesarias para aprobar):

- Compatibilidad con varios modelos LLM además de `Qwen/Qwen3-0.6B`.
- Reimplementación del tokenizador: evitar el uso directo de `encode` y `decode` en el código principal y utilizar, en su lugar, `get_logits_from_input_ids` y `get_path_to_vocab_file`.
- Mecanismos avanzados de recuperación ante errores.
- Optimizaciones de rendimiento (caché, procesamiento por lotes).
- Una batería de pruebas completa.
- Visualización del proceso de generación.
- Compatibilidad con argumentos de función complejos y anidados.
- Implementación pública de los métodos `encode` y `decode` opcional del tokenizador.
- Demostración de cómo se integran la codificación y la decodificación con la decodificación restringida.

Las funcionalidades extra deben estar implementadas y funcionar; no basta con describirlas en el `README.md`. Es posible que te pidan demostrarlas durante la evaluación.

### 8. Entrega y evaluación entre compañeros

Entrega el trabajo en tu repositorio Git como de costumbre. Durante la defensa solo se revisará el contenido que esté dentro del repositorio. Comprueba los nombres de los archivos para asegurarte de que sean correctos.

El repositorio debe contener:

- El directorio `src/` con la implementación.
- `pyproject.toml` y `uv.lock` para gestionar las dependencias.
- El directorio `llm_sdk/` (copiado del paquete proporcionado).
- El directorio `data/input/` con los archivos de prueba (para la demostración).
- `README.md` con documentación completa.
- Cualquier otro archivo necesario para ejecutar la solución.

> **No incluyas el directorio `output/` en el repositorio.** Se generará durante la evaluación entre compañeros.

Durante la evaluación, puede que ocasionalmente te pidan realizar una pequeña modificación del proyecto. Podría tratarse de un cambio menor de comportamiento, escribir o reescribir unas pocas líneas de código, o añadir una funcionalidad sencilla.

Aunque este paso no siempre se aplique, debes estar preparado para ello si aparece en las directrices de evaluación. Su objetivo es comprobar que realmente comprendes una parte concreta del proyecto. La modificación puede realizarse en cualquier entorno de desarrollo que elijas (por ejemplo, el que utilizas habitualmente) y debería poder completarse en unos minutos, salvo que se indique un plazo específico.

Por ejemplo, podrían pedirte que actualices una función o un script, modifiques una visualización o ajustes una estructura de datos para almacenar nueva información. Los detalles (alcance, objetivo, etc.) se especificarán en las directrices de evaluación y pueden variar entre evaluaciones del mismo proyecto.

## 🚀 Call Me Maybe Tests

### 📌 0. Guidelines

#### ⚠️ Rules

- La revisión se realiza **en presencia del alumno evaluado**.
- Se ha comprobado que el repositorio pertenece al alumno o al grupo y corresponde al proyecto correcto.
- Se trabaja únicamente con el contenido existente en el **repositorio Git del alumno**.
- Se comprueba que el repositorio se clona en una carpeta vacía.
- No se han utilizado alias/scripts maliciosos para alterar el contenido evaluado.
- El evaluador y el evaluado han revisado los posibles scripts utilizados durante la evaluación.
- Si el evaluador no ha realizado todavía el proyecto, ha leído previamente el subject completo.
- No se modifica ningún archivo salvo que sea estrictamente necesario y, en ese caso, se explica y acuerda previamente con el evaluado.
- Todos los errores deben gestionarse correctamente sin provocar crashes.
- El proyecto debe ejecutarse mediante `uv run python -m src`.
- Se debe comprobar que la salida JSON cumple exactamente el formato especificado.
- Se debe comprobar que el **constrained decoding** está realmente implementado y no se limita únicamente a realizar prompting.
- La salida generada debe ser **100 % parseable como JSON**.
- Si se produce una condición que obliga a finalizar la evaluación, se utiliza la flag correspondiente.

#### 📁 Estructure

- Se comprueba que el proyecto tiene una estructura válida.
- Se verifica que existe el directorio `input/`.
- Se verifica que el directorio `output/` se crea durante la ejecución.
- Se comprueba que están disponibles los archivos de entrada requeridos:
  - `function_calling_tests.json`
  - `functions_definition.json`
- Se comprueba que el proyecto puede instalar y sincronizar correctamente sus dependencias mediante `uv sync`.

#### ⚠️ Stop conditions

Si se detecta una condición que obliga a finalizar la evaluación, debe utilizarse la flag correspondiente.

- **Empty work → El trabajo es inexistente**
- **Incomplete work → El trabajo está incompleto**
- **Invalid compilation → El proyecto no funciona correctamente**
- **Norme → Error de norma de 42**
- **Cheat → Uso de cheats/elementos no autorizados**
- **Crash → Error de ejecución**
- **Concerning situation → Situación preocupante**
- **Forbidden function → Función no autorizada**
- **Can't support / explain code → El alumno no puede explicar o defender el código**

#### 🧰 General concepts to check

- Verifica que `uv sync` termina correctamente.
- Verifica que el proyecto puede ejecutarse mediante `uv run python -m src`.
- Verifica que `llm_sdk` está correctamente integrado.
- Verifica que las clases utilizan **Pydantic** para la validación.
- Verifica que el modelo utilizado es **Qwen/Qwen3-0.6B**.
- Verifica que no se accede a métodos o atributos privados del SDK.
- Verifica que los errores se gestionan correctamente y no provocan crashes.
- Verifica que todos los resultados generados son JSON válido y parseable.
- Verifica que el **constrained decoding** está implementado realmente.
- Verifica que la selección de funciones y la extracción de argumentos alcanzan los requisitos establecidos.

---
---

### 🧪 1. Preliminaries

#### ▶️ Execution

```bash
uv sync
uv run python -m src
```

#### 🔍 Functionality

- El proyecto se ejecuta utilizando `uv run python -m src`.
- `uv sync` termina correctamente.
- El proyecto utiliza correctamente `llm_sdk`.
- Las clases utilizan Pydantic para la validación.
- Todos los errores se gestionan de forma controlada.
- El programa no termina inesperadamente ante entradas inválidas.
- El formato de salida JSON cumple exactamente las especificaciones requeridas.
- El **constrained decoding** está implementado y no consiste únicamente en añadir instrucciones al prompt.
- El 100 % de las salidas generadas son JSON parseable.

#### 🧪 Tests

| Prueba | Esperado |
|---|---|
| `uv sync` | Finaliza correctamente |
| `uv run python -m src` | Ejecuta correctamente |
| Entrada válida | Se procesa correctamente |
| Entrada inválida | Error controlado |
| Salida generada | JSON válido |
| JSON generado | 100 % parseable |
| Constrained decoding | Está realmente implementado |
| Uso de Pydantic | Correctamente implementado |

---
---

### 📁 2. Project Structure & Dependencies

#### 🔍 Functionality

- La estructura del proyecto es correcta.
- Existe el directorio `input/`.
- El directorio `output/` se crea durante la ejecución.
- El proyecto utiliza correctamente las dependencias definidas.
- `llm_sdk` está integrado correctamente.
- Las clases que requieren validación utilizan Pydantic.
- El proyecto puede instalarse y ejecutarse mediante `uv`.

#### 🧪 Tests

| Prueba | Resultado Esperado |
|---|---|
| Ejecutar `uv sync` | Correcto |
| Ejecutar `uv run python -m src` | Correcto |
| Comprobar `input/` | Existe y contiene los archivos necesarios |
| Ejecutar el programa | Se crea `output/` |
| Comprobar `llm_sdk` | Integración correcta |
| Comprobar Pydantic | Se utiliza para validación |

---
---

### 📥 3. Input File Handling

#### 🔍 Functionality

- El programa lee correctamente `function_calling_tests.json`.
- El programa lee correctamente `functions_definition.json`.
- Los datos de entrada se procesan correctamente.
- Los archivos JSON inválidos se gestionan de forma controlada.
- Los archivos de entrada inexistentes generan mensajes de error claros.
- Ninguna de estas situaciones provoca un crash inesperado.

#### 🧪 Tests

| Caso | Resultado Esperado |
|---|---|
| `function_calling_tests.json` válido | Se procesa correctamente |
| `functions_definition.json` válido | Se procesa correctamente |
| JSON de entrada mal formado | Error controlado |
| Archivo de entrada inexistente | Mensaje de error claro |
| Funciones no definidas | Error controlado |
| Entrada inesperada | El programa no hace crash |

#### 🧠 Concepts to check

- El alumno puede explicar cómo se cargan los archivos JSON.
- El alumno puede explicar cómo se validan los datos.
- El alumno puede explicar qué ocurre cuando un archivo no existe.
- El alumno puede explicar cómo se gestionan errores de parsing JSON.

---
---

### 📤 4. Output File Format

#### 🔍 Functionality

- El archivo de salida se crea correctamente.
- Por defecto se utiliza:

```text
data/output/function_calling_results.json
```

- Se permite especificar una ruta diferente mediante `--output`.
- El archivo contiene JSON válido y completamente parseable.
- El esquema JSON coincide exactamente con el formato esperado.
- Cada entrada contiene exactamente las claves:
  - `prompt`
  - `name`
  - `parameters`
- Los argumentos requeridos están presentes.
- Los argumentos coinciden con el esquema de la función correspondiente.
- Los tipos de los argumentos son correctos.
- Los valores permitidos respetan las restricciones definidas por las funciones.
- Para parámetros de tipo `number`, se aceptan tanto enteros JSON como valores de coma flotante salvo que la definición de la función indique lo contrario.
- No existen claves adicionales.
- No existe texto o prosa fuera de la estructura JSON.

#### 🧪 Output Validation Tests

| Caso | Resultado Esperado |
|---|---|
| Archivo de salida generado | Correcto |
| JSON válido | 100 % parseable |
| Entrada con `prompt` | Presente |
| Entrada con `name` | Presente |
| Entrada con `parameters` | Presente |
| Argumentos obligatorios | Presentes |
| Tipos de argumentos | Correctos |
| Valores restringidos | Respetan el esquema |
| Claves adicionales | No existen |
| Texto fuera del JSON | No existe |
| Parámetro `number` entero | Válido cuando corresponda |
| Parámetro `number` float | Válido cuando corresponda |

#### 🧠 Concepts to check

- El alumno puede explicar el esquema de salida.
- El alumno puede explicar por qué la salida debe ser JSON estrictamente válido.
- El alumno puede explicar cómo se garantiza que no aparecen claves adicionales.
- El alumno puede explicar cómo se validan los argumentos de las funciones.

---
---

### 🤖 5. Function Calling Accuracy

#### 🔍 Functionality

- El sistema selecciona correctamente la función correspondiente al prompt.
- La extracción de argumentos es correcta.
- Se realizan pruebas con prompts sencillos.
- Se realizan pruebas con prompts ambiguos.
- Se prueban casos límite.
- Se prueban strings vacíos.
- Se prueban números grandes.
- La selección de funciones alcanza una precisión superior al **90 %** en las pruebas correspondientes.
- La extracción de argumentos cumple los requisitos establecidos.

#### 🧪 Function Calling Tests

| Prueba | Resultado Esperado |
|---|---|
| `"add 2 and 3"` | Selecciona la función correcta |
| Prompt sencillo | Selección correcta |
| Argumentos sencillos | Extracción correcta |
| Prompt ambiguo | Gestión correcta |
| String vacío | Gestión controlada |
| Número grande | Gestión correcta |
| Selección de función | >90 % de precisión |
| Extracción de argumentos | >90 % según las pruebas |

#### 🧠 Defense

- ¿Cómo determina el sistema qué función debe utilizar?
- ¿Cómo extrae los argumentos del prompt?
- ¿Qué ocurre cuando un prompt es ambiguo?
- ¿Qué ocurre cuando ninguna función coincide con el prompt?
- ¿Cómo se comprueba la precisión de la selección de funciones?
- ¿Cómo se comprueba la precisión de los argumentos?

---
---

### 🧠 6. Constrained Decoding

#### 🔍 Functionality

- El proyecto implementa **constrained decoding**.
- El constrained decoding no consiste únicamente en añadir instrucciones al prompt.
- La generación está restringida para producir una estructura compatible con el formato esperado.
- La solución garantiza la generación de JSON válido.
- La implementación se integra correctamente con el SDK proporcionado.

#### 🧪 Tests

| Prueba | Resultado Esperado |
|---|---|
| Prompt válido | Generación válida |
| Prompt ambiguo | Salida controlada |
| Generación de JSON | JSON válido |
| Generación repetida | Resultados parseables |
| Restricciones de esquema | Se respetan |
| Prompting sin restricciones reales | No debe considerarse constrained decoding |

#### 🧠 Concepts to check

- El alumno puede explicar qué significa **constrained decoding**.
- El alumno puede explicar la diferencia entre prompting y constrained decoding.
- El alumno puede explicar cómo se aplican las restricciones durante la generación.
- El alumno puede explicar cómo se garantiza la validez estructural del JSON.

---
---

### 🤗 7. LLM SDK Usage

#### 🔍 Functionality

- Se utiliza correctamente el SDK proporcionado.
- Los métodos utilizados corresponden con la implementación disponible del SDK.
- No se accede a métodos privados.
- No se accede a atributos privados.
- Se utiliza el modelo:

```text
Qwen/Qwen3-0.6B
```

- La integración con `llm_sdk` funciona correctamente.

#### 🧪 SDK Tests

| Prueba | Resultado Esperado |
|---|---|
| Inicialización del SDK | Correcta |
| Uso de métodos públicos | Correcto |
| Acceso a métodos privados | No utilizado |
| Acceso a atributos privados | No utilizado |
| Modelo utilizado | `Qwen/Qwen3-0.6B` |
| Generación | Funciona correctamente |

#### 🧠 Defense

- ¿Qué método del SDK utilizas para realizar la generación?
- ¿Por qué utilizas ese método?
- ¿Cómo sabes que forma parte de la API pública?
- ¿Qué modelo estás utilizando?
- ¿Cómo se integra el SDK con el constrained decoding?

---
---

### 🛡️ 8. Error Handling & Robustness

#### 🔍 Functionality

- Los errores de entrada se gestionan correctamente.
- Los JSON malformados no provocan crashes.
- Los archivos inexistentes generan mensajes claros.
- Las definiciones de funciones inexistentes se gestionan correctamente.
- Los prompts que no coinciden con ninguna función se gestionan correctamente.
- El programa nunca termina inesperadamente.
- Los mensajes de error son claros y útiles.

#### 🧪 Error Handling Tests

| Caso | Resultado Esperado |
|---|---|
| JSON malformado | Error controlado |
| Archivo inexistente | Mensaje claro |
| Function definition inexistente | Error controlado |
| Prompt sin función correspondiente | Gestión correcta |
| Entrada inesperada | No crash |
| Error durante generación | Gestión correcta |
| Error durante parsing | Gestión correcta |

#### 🧠 Concepts to check

- El alumno puede explicar cómo se capturan los errores.
- El alumno puede explicar qué ocurre ante un JSON inválido.
- El alumno puede explicar qué ocurre cuando no existe una función adecuada.
- El alumno puede explicar cómo se evita un crash inesperado.

---
---

### ⚡ 9. Performance & Reliability

#### 🔍 Functionality

- Todos los prompts de prueba se procesan en un tiempo razonable.
- El tiempo total de procesamiento debe ser inferior a **5 minutos**.
- El 100 % de las salidas son JSON parseable.
- La solución alcanza más del **90 % de precisión** en las pruebas proporcionadas.
- La solución mantiene un comportamiento fiable durante múltiples ejecuciones.

#### 🧪 Performance Tests

| Prueba | Resultado Esperado |
|---|---|
| Procesamiento completo de tests | < 5 minutos |
| JSON válido | 100 % |
| Precisión en tests proporcionados | >90 % |
| Primera ejecución | Correcta |
| Segunda ejecución | Correcta |
| Múltiples ejecuciones | Comportamiento estable |

#### 🧠 Concepts to check

- ¿El alumno puede explicar las decisiones que afectan al rendimiento?
- ¿La solución depende de comportamientos no deterministas?
- ¿La solución mantiene resultados válidos en múltiples ejecuciones?

---
---

### 🧹 10. Code Quality & Documentation

#### 🐍 Python

- El código está bien organizado.
- El código es legible.
- Las responsabilidades están correctamente separadas.
- Se utilizan **type hints** apropiadamente.
- El código está correctamente documentado cuando es necesario.
- No existen accesos innecesarios a APIs privadas.
- La implementación es comprensible para otro estudiante.

#### 🧩 Pydantic

- Pydantic se utiliza correctamente para la validación.
- Los modelos representan correctamente los datos utilizados.
- Las restricciones de los modelos son apropiadas.
- Los datos generados se validan correctamente.

#### 📚 README

- Existe un `README.md` adecuado.
- El README explica claramente el algoritmo.
- El README explica las decisiones de diseño.
- El README explica los principales problemas o desafíos encontrados.
- La documentación permite comprender el funcionamiento general del proyecto.

#### 🧠 Understanding & Learning

- El alumno puede explicar la arquitectura general.
- El alumno puede explicar el flujo desde el prompt hasta la función seleccionada.
- El alumno puede explicar cómo se generan los argumentos.
- El alumno entiende el papel de Pydantic.
- El alumno entiende el papel de `llm_sdk`.
- El alumno entiende el constrained decoding.
- El alumno puede explicar las principales decisiones de diseño.

---
---

### 🧪 11. Moulinette Evaluation

#### ▶️ Execution

Navegar hasta el directorio de `moulinette` y ejecutar:

```bash
uv sync
uv run python -m moulinette prepare_exercises --set private
uv run python -m moulinette grade_student_answers --set private --student <path>
```

#### 🔍 Functionality

- `uv sync` termina correctamente.
- `prepare_exercises --set private` termina correctamente.
- `grade_student_answers --set private --student <path>` termina correctamente.
- La evaluación genera un resultado válido.
- El resultado total es superior a `0`.
- La evaluación de Moulinette termina sin errores.

#### 🧪 Moulinette Tests

| Prueba | Resultado Esperado |
|---|---|
| `uv sync` | Correcto |
| `prepare_exercises` | Correcto |
| `grade_student_answers` | Correcto |
| Score total | > 0 |
| Evaluación completa | Sin errores |

---
---

### ⭐ 12. Bonus

Los siguientes elementos son opcionales y no son necesarios para superar la parte obligatoria.

#### 🔍 Bonus Features

- Soporte para múltiples modelos LLM además de `Qwen/Qwen3-0.6B`.
- Recodificación del tokenizer sin utilizar directamente los métodos `encode` y `decode` en el código principal.
- Uso de `get_logits_from_input_ids`.
- Uso de `get_path_to_vocab_file`.
- Mecanismos avanzados de recuperación de errores.
- Optimizaciones de rendimiento mediante caching.
- Batching.
- Uso exclusivo de PyTorch para batching cuando se interactúa con el `llm_sdk`.
- Suite de tests completa.
- Visualización del proceso de generación.
- Soporte para argumentos complejos y anidados de funciones.
- Implementación pública de métodos `encode` y `decode` del tokenizer compatibles con los proporcionados por el SDK.
- Demostración de la integración entre encoding/decoding y constrained decoding.

#### 🧪 Bonus Evaluation

| Bonus | Comprobación |
|---|---|
| Múltiples modelos LLM | Implementado correctamente |
| Tokenizer recodificado | Implementado correctamente |
| Error recovery avanzado | Presente y funcional |
| Caching / batching | Presente y funcional |
| Suite de tests | Completa |
| Visualización | Funcional |
| Argumentos anidados | Soportados |
| Encode/decode públicos | Compatibles |
| Integración tokenizer + constrained decoding | Demostrada |

#### ⭐ Bonus Rating

- **0** → No hay bonus destacable.
- **1** → Bonus limitado.
- **2** → Algunas funcionalidades adicionales.
- **3** → Varias funcionalidades adicionales.
- **4** → Implementación avanzada de bonus.
- **5** → Implementación de bonus especialmente completa.

---
---

### 🚩 13. Defense

#### 💬 Questions

1. ¿Por qué el proyecto utiliza `uv`?

2. ¿Por qué el programa debe ejecutarse mediante `uv run python -m src`?

3. ¿Qué función cumple `llm_sdk`?

4. ¿Qué modelo LLM se utiliza?

5. ¿Cómo se selecciona la función que debe ejecutar el modelo?

6. ¿Cómo se extraen los argumentos de una función?

7. ¿Qué es el **constrained decoding**?

8. ¿Qué diferencia existe entre prompting y constrained decoding?

9. ¿Cómo garantizas que el resultado sea JSON válido?

10. ¿Qué ocurre si el JSON de entrada está mal formado?

11. ¿Qué ocurre si falta `function_calling_tests.json`?

12. ¿Qué ocurre si falta `functions_definition.json`?

13. ¿Qué ocurre si el prompt no coincide con ninguna función?

14. ¿Cómo validas los argumentos generados por el modelo?

15. ¿Por qué se utiliza Pydantic?

16. ¿Cómo compruebas que no existen claves adicionales en el JSON de salida?

17. ¿Qué ocurre con un parámetro cuyo tipo es `number`?

18. ¿Cómo compruebas la precisión de selección de funciones?

19. ¿Cómo compruebas la precisión de extracción de argumentos?

20. ¿Qué medidas has tomado para garantizar que el programa no haga crash?

21. ¿Cómo garantizas que el 100 % de las salidas sean JSON parseable?

22. ¿Qué métodos públicos del SDK estás utilizando?

23. ¿Has utilizado algún método o atributo privado del SDK?

24. ¿Cómo has implementado el constrained decoding?

25. ¿Qué decisiones de diseño explicas en el README?

26. ¿Qué problemas o desafíos encontraste durante la implementación?

27. ¿Cómo has comprobado el rendimiento del programa?

28. ¿Qué ocurre si el programa recibe una entrada inesperada?

29. ¿Cómo funciona la evaluación de Moulinette?

30. ¿Puedes explicar el flujo completo desde el prompt de entrada hasta el JSON final?

---
---

### 🏁 14. Final Evaluation

#### ⚠️ Final Checks

- Repositorio correcto.
- Proyecto correcto.
- No existen cheats ni scripts maliciosos.
- `uv sync` funciona.
- `uv run python -m src` funciona.
- Los archivos de entrada se procesan correctamente.
- Los errores se gestionan sin crashes.
- La salida JSON es 100 % válida.
- El esquema de salida es correcto.
- La selección de funciones supera el 90 %.
- La extracción de argumentos cumple los requisitos.
- El modelo utilizado es `Qwen/Qwen3-0.6B`.
- No se utilizan APIs privadas del SDK.
- El rendimiento cumple el límite establecido.
- Moulinette termina correctamente.
- Se ha comprobado la documentación.
- El alumno puede defender y explicar el código.
