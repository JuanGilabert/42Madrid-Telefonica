# 🚀 Python Module 09

## 📌 0. Guidelines

### ⚠️ Rules

- La revisión se realiza **en presencia del alumno evaluado**.265
- Se ha comprobado que el repositorio pertenece al alumno y corresponde al proyecto correcto ya que se trabaja únicamente con el contenido existente en el **repositorio Git del alumno**. Si no hay contenido, la evaluación termina aqui(Empty-Work).
- No se han utilizado alias/scripts maliciosos para alterar el contenido evaluado.
- El evaluador y el evaluado han revisado los posibles scripts utilizados durante la evaluación.
- Si el evaluador no ha realizado todavía el proyecto, ha leído previamente el subject completo.
- No se modifica ningún archivo salvo que sea estrictamente necesario y, en ese caso, se explica y acuerda previamente con el evaluado.
- Si un ejercicio no funciona: la evaluación se detiene en ese punto. Los ejercicios posteriores pueden inspeccionarse, pero no se califican(se quedan suspensos).

### 📁 Estructure

- Si falta alguno de los siguientes ficheros/archivos, la evaluacion termina aqui(Incomplete-Work).
- `ex0/space_station.py`
- `ex1/alien_contact.py`
- `ex2/space_crew.py`

### ⚠️ Stop conditions
Si se detecta una condición que obliga a finalizar la evaluación, debe utilizarse la flag correspondiente.

- **Empty/Incomplete work → El trabajo es inexistente o incompleto**
- **Invalid compilation → El codigo no compila**
- **Norme → Error de norma de 42 (42 norme)**
- **Cheat → Uso de cheats/elementos no autorizados**
- **Crash → Error de ejecucion**
- **Concerning situation → Situación preocupante**
- **Leaks → Fugas de memoria**
- **Forbidden function  → Funcion no autorizada**
- **Can't support / explain code → Posible plagio de codigo**

### 🧰 General concepts to check

- Verififca que el codigo se ejecuta sin errores y demuestra los conceptos requeridos
- Verifica probando datos válidos e invalidos que la valdacion funciona correctamente.
- Se utiliza `BaseModel` correctamente.
- Se utiliza `Field()` con restricciones apropiadas.
- Se utiliza `@model_validator` para validaciones personalizadas.
- No se utilizan decoradores obsoletos como `@validator`(Pydantic v1).

---
---
# 🛰️ 1. Exercise 0 — Space Station Data

**Archivo:** `ex0/space_station.py`

### ▶️ Execution

```bash
python3 ex0/space_station.py
```

### 🔍 Functionality

- `SpaceStation` hereda de `BaseModel`.
- Todos los campos obligatorios utilizan `Field()` con restricciones apropiadas.
- Se pueden crear estaciones espaciales con datos válidos.
- Los datos inválidos generan errores de validación.
- `crew_size > 20` es rechazado correctamente.
- La demostración muestra tanto una creación válida como errores de validación.
- La estación válida y la inválida se crean realmente mediante Pydantic; el resultado **no está hardcodeado**.
- Los errores de validación se gestionan correctamente y no provocan una salida inesperada.

### 🧪 Tests

| Prueba | Esperado |
|---|---|
| Datos completamente válidos | Se crea `SpaceStation` |
| `crew_size > 20` | Error de validación |
| Valor fuera de rango en otro campo restringido | Error de validación |
| Ejecución completa del script | Finaliza correctamente |
| Salida generada dinámicamente | No está hardcodeada |

### 🧹 Code Quality — Exercise 0

- El código es legible.
- El código está bien estructurado.
- Las restricciones de los campos son apropiadas.
- `crew_size` respeta el rango esperado **1–20**.
- `power_level` respeta el rango esperado **0–100**.
- Los campos opcionales, como `notes`, están definidos correctamente.
- El campo `last_maintenance` utiliza correctamente `datetime`.
- ¿ Al proporcionar un timestamp como `string` en `last_maintenance`, Pydantic lo procesa correctamente ?
- ¿ Que pasa cuando pasas un string timestamp en `last_maintenance` ?

---
---
# 👽 2. Exercise 1 — Alien Contact Data

**Archivo:** `ex1/alien_contact.py`

### ▶️ Execution

```bash
python3 ex1/alien_contact.py
```

### 🔍 Functionality

- Se muestran contactos válidos.
- Se muestran errores de validación.
- Todos los valores requeridos del `enum` están implementados y correctamente definidos.
- `ContactType` está correctamente definido y se utiliza realmente en el modelo.
- `message_received` es opcional y tiene una longitud máxima de **500 caracteres**.
- No se utiliza el decorador obsoleto `@validator`.
- `AlienContact` utiliza `@model_validator` para validación personalizada:
    - `contact_id` debe comenzar por `"AC"`.
    - Un contacto físico requiere estar `verified`.
    - Un contacto con señal fuerte requiere un `message`.
    - Los contactos telepáticos respetan el requisito de mínimo **3 witnesses**.

### 🧪 Customized Validation Tests

| Caso | Esperado |
|---|---|
| `contact_id` no empieza por `AC` | Debe fallar |
| Contacto telepático con `< 3` witnesses | Debe fallar |
| Strong signal sin `message` | Debe fallar |
| Contacto físico no verificado | Debe fallar |
| `is_verified` omitido | Debe ser `False` por defecto |
| `message_received` > 500 caracteres | Debe fallar |
| Datos válidos | Debe crear el modelo |

### 🔎 `model_validator` Validation

- El validador recibe correctamente los datos/modelo.
- Las condiciones se comprueban correctamente.
- El validador devuelve `self` cuando corresponde.
- Los mensajes de error son claros y útiles.
- La lógica está implementada en el modelo y no simulada/hardcodeada mediante `print()`.

---
---
# 👨‍🚀 3. Exercise 2 — Space Crew Management

**Archivo:** `ex2/space_crew.py`

### ▶️ Execution

```bash
python3 ex2/space_crew.py
```

### 🔍 Functionality

- Los modelos `CrewMember` & `SpaceMission` están correctamente definidos.
- El campo `crew` acepta una lista de objetos `CrewMember`(modelos anidados).
- Se utilizan correctamente **nested models**.
- Están implementados los **5 rangos** requeridos.

- Las reglas de validación de la misión funcionan. Prueba que funcionan todas las reglas.
- Se muestran los detalles de la tripulación y mision correctamente.
- Las misiones inválidas( sin un oficial de alto rango) son rechazadas correctamente generando el error correspondiente.

### 🧪 Nested Models Functionality & Mission Validation Tests

| Caso | Resultado Esperado |
|---|---|
| Crear un `CrewMember` individual | Correcto |
| Crear `SpaceMission` con lista de `CrewMember` validada | Correcto |
| Commander activo + Captain inactivo | Validación correcta según reglas |
| Misión sin rango requerido | Debe fallar |
| `status` omitido | Debe ser `planned` por defecto |
| Misión por encima del presupuesto | Debe fallar |
| Casos límite / edge cases | Gestionados correctamente |

### 🧠 Concepts to check

- Las reglas de validación son coherentes.
- El alumno puede explicar por qué una misión es válida o inválida.
- El alumno puede explicar cómo Pydantic valida los modelos anidados.
- El alumno puede explicar qué ocurre ante datos fuera de rango.

---
---
# 🧹 4. Code Quality & Best Practices

## 🐍 Python

- El código está escrito para **Python 3.10 o superior**.
- El código cumple los estándares de `flake8`.
- No existen errores de linting relevantes.
- Todas las funciones y métodos tienen **type hints** para parámetros y valores de retorno, cumpliendo con el estandar `mypy`.
- No se requieren docstrings para este módulo.
- Se respetan las convenciones de nombres de Python.
- Los outputs de las demostraciones son claros e informativos.

## 🧩 Pydantic

- No se utilizan características obsoletas de Pydantic v1.
- `Field()` se utiliza apropiadamente.
- Las restricciones de los campos tienen sentido.
- `@model_validator` se utiliza correctamente.
- Las validaciones personalizadas están claramente implementadas.
- Los `enum` se utilizan donde aportan claridad o es apropiado.

## 🧠 Understanding & Learning

- Los ejemplos demuestran un uso correcto de Pydantic.
- Las reglas de validación tienen sentido y están bien planteadas.
- Se observa una progresión desde conceptos básicos hasta conceptos avanzados.
- El alumno puede explicar las decisiones principales del código.
- El alumno entiende la diferencia entre validación automática y validación personalizada.
- El alumno entiende el uso de modelos anidados.
- El código podría servir como ejemplo de aprendizaje para otros estudiantes.

---
---
# 🚩 5. Defense

## 💬 Questions

1. ¿Por qué se utiliza `BaseModel`?

2. ¿Qué función cumple `Field()`?

3. ¿Cuándo necesitas `@model_validator`?

4. ¿Qué diferencia hay entre un `enum` y un `str` normal?

5. ¿Qué significa que `SpaceMission` tenga un modelo anidado?

6. ¿Qué ocurre cuando Pydantic recibe datos inválidos?
