# ⚗️ Python Module 06

## 📌 0. Guidelines

### ⚠️ Rules

- La revisión se realiza **en presencia del alumno evaluado**.
- Se ha comprobado que el repositorio pertenece al alumno y corresponde al proyecto correcto.
- Se trabaja únicamente con el contenido existente en el **repositorio Git del alumno**.
- Se comprueba que el repositorio ha sido clonado en una carpeta vacía.
- No se han utilizado alias/scripts maliciosos para alterar el contenido evaluado.
- El evaluador y el evaluado han revisado los posibles scripts utilizados durante la evaluación.
- Si el evaluador no ha realizado todavía el proyecto, ha leído previamente el subject completo.
- No se modifica ningún archivo salvo que sea estrictamente necesario y, en ese caso, se explica y acuerda previamente con el evaluado.
- Si se detecta un repositorio vacío, trabajo incompleto, programa que no funciona, error de norma, cheating u otra condición que implique una flag, la evaluación termina y la nota final es 0, salvo cheating, que implica -42.
- Durante la defensa no se permite ninguna terminación inesperada, prematura o incontrolada del programa, salvo que esté excepcionalmente permitida por el ejercicio.

### 📁 Structure

- Verifica que la estructura del proyecto coincide con los requisitos del subject.
- Verifica que están presentes los módulos, paquetes y archivos necesarios para los experimentos de:
  - Alembic
  - Distillation
  - Great Transmutation
  - Avoid the Explosion / Circular dependencies

### 🧰 General concepts to check

- El código se ejecuta correctamente con **Python 3.10 o superior**.
- Los scripts de prueba producen los resultados esperados.
- Los imports utilizados corresponden a los métodos solicitados.
- Se comprende la diferencia entre imports directos, imports mediante módulos y imports expuestos desde `__init__.py`.
- Se utilizan correctamente imports absolutos y relativos.
- Se entiende cómo funcionan los paquetes Python y sus archivos `__init__.py`.
- Se comprende el problema de las dependencias circulares y la solución utilizada para evitarlo.

---
---
# 🔥 1. Part I — The Alembic

### ▶️ Execution

Ejecutar:

```bash
python3 ft_alembic_[0-5].py
```

### 🔍 Functionality

- `ft_alembic_0.py` utiliza:

```python
import elements
```

y llama a:

```python
elements.create_fire()
```

- `ft_alembic_1.py` utiliza:

```python
from elements import create_water
```

y llama a:

```python
create_water()
```

- `ft_alembic_2.py` utiliza:

```python
import alchemy.elements
```

y llama a:

```python
alchemy.elements.create_earth()
```

- `ft_alembic_3.py` utiliza:

```python
from alchemy.elements import create_air
```

y llama a:

```python
create_air()
```

- `ft_alembic_4.py` utiliza:

```python
import alchemy
```

y llama a:

```python
alchemy.create_air()
```

Después intenta acceder a:

```python
alchemy.create_earth()
```

y esta operación debe fallar. En este caso se permite una excepción no controlada.

- `ft_alembic_5.py` utiliza:

```python
from alchemy import create_air
```

y llama a:

```python
create_air()
```

- El paquete `alchemy` contiene su archivo `__init__.py`.
- `alchemy/__init__.py` importa `elements`.
- `create_earth` no debe exponerse directamente desde `alchemy`.
- Se aceptan soluciones alternativas siempre que mantengan el comportamiento requerido.

### 🧪 Tests

| Prueba | Esperado |
|---|---|
| `python3 ft_alembic_0.py` | Funciona y demuestra el import requerido |
| `python3 ft_alembic_1.py` | Funciona y demuestra el import requerido |
| `python3 ft_alembic_2.py` | Funciona y accede a `alchemy.elements` |
| `python3 ft_alembic_3.py` | Funciona mediante `from ... import ...` |
| `python3 ft_alembic_4.py` | `create_air()` funciona y `create_earth()` falla |
| `python3 ft_alembic_5.py` | Funciona mediante `from alchemy import create_air` |
| `alchemy/__init__.py` | Expone lo requerido sin exponer `create_earth` |

### 🧠 Understanding

- El alumno puede explicar la diferencia entre:
  - `import elements`
  - `from elements import create_water`
  - `import alchemy.elements`
  - `from alchemy.elements import create_air`
  - `import alchemy`
  - `from alchemy import create_air`
- El alumno entiende qué nombres quedan disponibles después de cada tipo de import.

---
---
# ⚗️ 2. Part II — Distillation

### ▶️ Execution

Ejecutar:

```bash
python3 ft_distillation_[0-1].py
```

### 🔍 Functionality

- `distillation_0` utiliza acceso directo al archivo `potions.py`.
- Se prueban las **healing potions**.
- `distillation_1` utiliza directamente el módulo `alchemy`.
- Se prueban las **strength potions**.
- En `distillation_1`, la healing potion se utiliza mediante el alias:

```python
heal()
```

- El archivo `__init__.py` del módulo `alchemy` se actualiza para exponer las potions.
- `potions.py` importa correctamente:
  - `elements.py`
  - `alchemy/elements.py`
- El código demuestra que el alumno comprende las diferentes formas de acceder a los módulos y objetos.

### 🧪 Tests

| Prueba | Esperado |
|---|---|
| `python3 ft_distillation_0.py` | Acceso directo a `potions.py` funciona |
| Healing potion | Se prueba correctamente |
| `python3 ft_distillation_1.py` | Acceso mediante `alchemy` funciona |
| Strength potion | Se prueba correctamente |
| `heal()` | Se utiliza como alias para la healing potion |
| `alchemy/__init__.py` | Expone las potions correctamente |
| Imports de `potions.py` | `elements.py` y `alchemy/elements.py` se importan correctamente |

### 🧠 Concepts to check

- Diferencia entre importar un archivo directamente y acceder a él mediante un paquete.
- Uso de aliases mediante `as`.
- Exposición de objetos desde `__init__.py`.
- El alumno puede explicar por qué una misma funcionalidad puede ser accesible mediante diferentes rutas de import.

---
---
# 🪙 3. Part III — The Great Transmutation

### ▶️ Execution

Ejecutar:

```bash
python3 ft_transmutation_[0-2].py
```

### 🔍 Functionality

Debe comprobarse el acceso a la receta `lead_to_gold` mediante las tres formas requeridas:

- Acceso directo al archivo:

```text
alchemy/transmutation/recipes.py
```

- Acceso mediante el módulo `transmutation`.
- Acceso mediante el módulo `alchemy`.

### 📁 Package structure

- El módulo `transmutation` contiene su propio archivo `__init__.py`.
- El archivo `__init__.py` de `alchemy` se actualiza para exponer `lead_to_gold`.
- `recipes.py` contiene al menos:
  - un **absolute import**
  - un **relative import**

### 🧪 Tests

| Prueba | Esperado |
|---|---|
| Acceso directo a `recipes.py` | `lead_to_gold` funciona |
| Acceso mediante `transmutation` | `lead_to_gold` funciona |
| Acceso mediante `alchemy` | `lead_to_gold` funciona |
| `transmutation/__init__.py` | Existe y funciona correctamente |
| `alchemy/__init__.py` | Expone `lead_to_gold` |
| Absolute import | Está presente y funciona |
| Relative import | Está presente y funciona |

### 🧠 Understanding

- El alumno puede explicar cuándo utilizar un import absoluto.
- El alumno puede explicar cuándo utilizar un import relativo.
- El alumno comprende cómo `__init__.py` puede utilizarse para exponer funcionalidades de un paquete.
- El alumno puede explicar las diferencias entre acceder a una funcionalidad desde el archivo, desde el submódulo y desde el paquete principal.

---
---
# 💥 4. Part IV — Avoid the Explosion

## 🔄 Circular experiment

### ▶️ Execution

Ejecutar:

```bash
python3 ft_kaboom_[0-1].py
```

### 🔍 Functionality

- Los dos scripts deben demostrar:
  - un import que funciona correctamente
  - un import que falla
- Las excepciones no controladas están permitidas cuando forman parte de la demostración requerida.
- El módulo:

```text
alchemy/grimoire
```

contiene los archivos esperados.
- Deben existir los archivos correspondientes a los hechizos `light_*` y `dark_*`.
- El módulo contiene su archivo `__init__.py`.
- Los ingredientes están definidos en el **spellbook** y no en el **validator**.
- Se comprueba la organización correcta de los archivos implicados en la dependencia circular.
- `Earth, Wind & Fire` puede registrar el hechizo `Fantasy`.
- El alumno debe comprender y poder explicar el problema de las dependencias circulares.
- El alumno debe explicar qué solución ha utilizado para evitar las dependencias circulares.

### 🧪 Circular Dependency Tests

| Prueba | Resultado esperado |
|---|---|
| `python3 ft_kaboom_0.py` | Import funcional + import fallido según el experimento |
| `python3 ft_kaboom_1.py` | Import funcional + import fallido según el experimento |
| `alchemy/grimoire` | Contiene los archivos esperados |
| `light_*` y `dark_*` | Están correctamente definidos |
| `__init__.py` | Existe en el módulo correspondiente |
| Ingredientes | Definidos en el spellbook, no en el validator |
| `Earth, Wind & Fire` | Puede registrar `Fantasy` |
| Dependencia circular | El alumno puede explicar el problema |
| Solución | El alumno puede explicar cómo evitó la dependencia circular |

### 🧠 Defense Questions

1. ¿Qué es una dependencia circular?
2. ¿Por qué puede provocar problemas durante la importación de módulos?
3. ¿Qué solución has utilizado para evitarla?
4. ¿Por qué los ingredientes deben estar definidos en el spellbook y no en el validator?
5. ¿Qué ocurre cuando Python intenta importar dos módulos que dependen circularmente uno del otro?

---
---
# 🧹 5. Code Quality & Best Practices

## 🐍 Python

- El código está escrito para **Python 3.10 o superior**.
- El código cumple los estándares de **flake8**.
- No existen errores relevantes de linting.
- Se utilizan **type hints** de forma completa.
- Las funciones tienen anotaciones para parámetros y valores de retorno.
- El código es compatible con las comprobaciones de **mypy**.
- Se admite la excepción de `ft_alembic_4.py`, indicada específicamente en el subject.
- No se requieren docstrings para este módulo.
- La organización general del código es limpia y profesional.
- Los nombres de módulos, funciones y variables son claros.
- Los imports están organizados de forma coherente.

## 📦 Packages & Imports

- Los paquetes contienen los `__init__.py` necesarios.
- Los imports absolutos están correctamente utilizados.
- Los imports relativos están correctamente utilizados.
- Los objetos se exponen mediante `__init__.py` cuando corresponde.
- No se exponen accidentalmente objetos que no deberían estar disponibles.
- El alumno comprende la diferencia entre importar un módulo y acceder a un objeto concreto.
- El alumno comprende cómo Python resuelve los imports dentro de paquetes.

## 🔄 Circular Dependencies

- Las dependencias entre módulos están correctamente organizadas.
- Se evita la dependencia circular problemática.
- La solución utilizada es comprensible y coherente.
- El alumno puede explicar qué causaba la dependencia circular.
- El alumno puede justificar la solución implementada.

## 🧠 Understanding & Learning

- Los experimentos demuestran realmente los conceptos solicitados.
- El comportamiento no está simulado mediante `print()` o resultados hardcodeados.
- El alumno puede explicar los diferentes estilos de import.
- El alumno entiende el papel de `__init__.py`.
- El alumno entiende la diferencia entre imports absolutos y relativos.
- El alumno entiende cómo se estructuran los paquetes Python.
- El alumno comprende las dependencias circulares y cómo evitarlas.
- El código podría servir como ejemplo de aprendizaje para otros estudiantes.

---
---
# 🚩 6. Defense

## 💬 Questions

### Imports

1. ¿Cuál es la diferencia entre `import module` y `from module import function`?

2. ¿Qué diferencia hay entre `import alchemy.elements` y `from alchemy.elements import create_air`?

3. ¿Qué ocurre cuando haces `import alchemy`?

4. ¿Qué papel cumple `__init__.py`?

5. ¿Cómo puede `__init__.py` hacer que una función sea accesible directamente desde el paquete?

### Absolute & Relative Imports

6. ¿Qué es un import absoluto?

7. ¿Qué es un import relativo?

8. ¿Cuál es la diferencia entre ambos?

9. ¿Por qué `recipes.py` utiliza tanto un import absoluto como uno relativo?

### Packages

10. ¿Qué diferencia hay entre un archivo `.py` y un paquete Python?

11. ¿Cómo organiza Python los módulos dentro de un paquete?

12. ¿Qué sucede si intentas acceder desde `alchemy` a una función que no ha sido expuesta en `__init__.py`?

### Circular Dependencies

13. ¿Qué es una dependencia circular?

14. ¿Qué problema puede provocar durante la importación?

15. ¿Cómo has solucionado la dependencia circular en este proyecto?

16. ¿Por qué mover una definición a otro módulo puede resolver una dependencia circular?

### Code Understanding

17. Explica qué sucede internamente cuando ejecutas uno de los `ft_alembic_*`.

18. ¿Qué diferencias hay entre los diferentes métodos de import utilizados en los ejercicios?

19. ¿Por qué en `ft_alembic_4.py` se espera que una llamada falle?

20. ¿Qué parte de tu código se encarga de exponer `lead_to_gold` desde `alchemy`?

---
---
# ⚠️ 7. Stop Conditions & Flags

Si se detecta una condición que obliga a finalizar la evaluación, debe utilizarse la flag correspondiente.

- **Empty work →** El repositorio está vacío.
- **Incomplete work →** El trabajo está incompleto.
- **Invalid compilation →** El código/programa no funciona correctamente.
- **Norme →** Error de norma.
- **Cheat →** Uso de cheats, alias maliciosos o elementos no autorizados.
- **Concerning situation →** Situación preocupante durante la defensa.
- **Leaks →** Fugas de memoria, cuando corresponda.
- **Forbidden function →** Uso de una función no autorizada.
- **Can't support / explain code →** El alumno no puede justificar o explicar adecuadamente el código.

### 🛑 Important

- Si se detecta una condición que implica la finalización de la evaluación, se utiliza la flag correspondiente y se detiene la calificación.
- Una excepción únicamente debe considerarse un fallo cuando contradiga el comportamiento esperado por el subject. Las excepciones no controladas están expresamente permitidas en los experimentos donde el subject las contempla.
- La evaluación debe realizarse exclusivamente sobre el contenido existente en el repositorio del alumno.
