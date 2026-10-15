# 🚀 Fly-In

## 🚀 Fly-In Project

## 🚀 Fly-In Project Tests

### 📌 0. Guidelines

**Debes evaluar a 1 estudiante de este equipo.**

## Repositorio Git

### Introducción

- Mantén una actitud educada, cortés, respetuosa y constructiva durante todo el proceso de evaluación. El bienestar de la comunidad depende de ello.
- Identifica con la persona (o el grupo) evaluada las posibles deficiencias del trabajo. Tómate el tiempo necesario para hablar y debatir sobre los problemas que hayas identificado.
- Debes tener en cuenta que puede haber diferencias en la forma en que tus compañeros hayan entendido las instrucciones del proyecto y el alcance de sus funcionalidades. Mantén siempre una mentalidad abierta y evalúa de la forma más honesta posible. La pedagogía solo es válida si la evaluación entre pares se realiza con seriedad.

### Directrices

- Evalúa únicamente el trabajo que se encuentre en el repositorio Git del estudiante o del grupo.
- Comprueba dos veces que el repositorio Git pertenece al estudiante o al grupo. Asegúrate de que el trabajo corresponde al proyecto pertinente y comprueba también que `git clone` se utiliza en una carpeta vacía.
- Comprueba cuidadosamente que no se haya utilizado ningún alias malicioso para engañarte y hacer que evalúes algo distinto del contenido del repositorio oficial.
- Para evitar sorpresas, comprueba cuidadosamente que tanto el estudiante evaluador como los estudiantes evaluados hayan revisado los posibles scripts utilizados para facilitar la evaluación.
- Si el estudiante evaluador todavía no ha completado ese proyecto en particular, es obligatorio que lea el enunciado completo antes de comenzar la defensa.
- Utiliza las opciones disponibles en esta escala para señalar un repositorio vacío, un programa que no funciona, un error de normas, trampas, etc. En estos casos, la evaluación termina y la nota final es 0 (o -42 en caso de trampas). Sin embargo, salvo en el caso de trampas, se recomienda continuar hablando sobre el trabajo (aunque no esté terminado) para identificar cualquier problema que haya podido causar este fallo y evitar repetir el mismo error en el futuro.
- Recuerda que durante la defensa no puede producirse ningún *segfault*, ni ninguna otra terminación inesperada, prematura o incontrolada del programa; de lo contrario, la nota final es 0. Utiliza la opción correspondiente.
- Nunca deberías tener que editar ningún archivo salvo el archivo de configuración, si existe. Si quieres editar un archivo, tómate el tiempo necesario para explicar explícitamente los motivos al estudiante evaluado y asegúrate de que ambos estáis de acuerdo.
- También debes comprobar que no existan fugas de memoria. Cualquier memoria asignada en el *heap* debe liberarse correctamente antes de finalizar la ejecución.

Puedes utilizar cualquiera de las herramientas disponibles en el ordenador, como `leaks`, `valgrind` o `e_fence`. En caso de fugas de memoria, marca la opción correspondiente.

## Adjuntos

- `subject.pdf`
- `maps.tar.gz`

## Preliminares

### Conceptos básicos

La revisión se realiza en presencia de los estudiantes evaluados. Así es como todos progresan: interactuando con los demás.

El/los estudiante(s) debe(n) estar presente(s) durante la defensa.

Si el estudiante no está presente, la revisión no puede continuar.

En cuanto una funcionalidad principal no funcione, la revisión se detiene. Puedes consultar el código o determinadas secciones, pero no se evaluarán.

## Entrega del trabajo

Evalúa únicamente el trabajo que se encuentre en el repositorio Git del estudiante o del grupo.

Comprueba que solo están disponibles en el repositorio Git los archivos solicitados. Si no es así, la evaluación se detiene aquí.

# README.md

## Archivo README.md

¿El repositorio contiene un archivo `README.md` en su raíz y contiene todo lo siguiente?

- Una sección «Description» que explique el propósito del proyecto y proporcione una breve descripción general.
- Una sección «Instructions» con detalles sobre cómo ejecutar el proyecto.
- Una sección «Algorithm explanation» que describa el enfoque de búsqueda de caminos y las decisiones de diseño.
- Documentación de las funcionalidades de representación visual y de cómo mejoran la experiencia del usuario.
- Un ejemplo de entrada y salida esperada que demuestre la funcionalidad del programa.

# Estructura y requisitos del proyecto

## OOP

El proyecto está completamente orientado a objetos, con un diseño apropiado de clases, y sigue las buenas prácticas de POO de Python.

Comprueba la correcta separación de clases, la encapsulación y la herencia cuando corresponda.

## Seguridad de tipos

El proyecto es completamente seguro respecto a los tipos y supera la comprobación de tipos de `mypy` sin errores.

Ejecuta:

```bash
mypy .
```

en el directorio del proyecto para verificarlo.

Si `mypy` no está instalado, comprueba que las anotaciones de tipos están presentes en todo el código.

## Implementación del grafo

La implementación del grafo está construida de forma personalizada sin utilizar bibliotecas prohibidas (como `networkx`, `graphlib`, etc.).

El estudiante debe ser capaz de explicar cómo funciona.

# Implementación del parser

## Archivos de entrada

Prueba el parser con archivos de entrada válidos.

El parser gestiona correctamente el nuevo formato de archivo de entrada, incluyendo:

- Número de drones utilizando el formato `nb_drones: <number>`.
- Definiciones de zonas con prefijos de tipo (`start_hub:`, `end_hub:`, `hub:`).
- Definiciones de conexiones utilizando el formato `connection: <zone1>-<zone2>`.
- Metadatos opcionales con valores predeterminados (`zone=normal`, `max_drones=1`).
- Metadatos de conexión con `max_link_capacity=1` como valor predeterminado.
- Los comentarios que comienzan por `#` se ignoran.

Al menos 4 de los 5 requisitos de formato deben funcionar correctamente.

## Gestión de errores

Prueba la gestión de errores del parser.

El parser gestiona correctamente los siguientes errores:

- Probar con archivos malformados (falta el número de drones, formato no válido).
- Probar con tipos de zona no válidos (debe rechazarlos con mensajes de error claros).
- Probar con definiciones de `start_hub` o `end_hub` ausentes.
- Probar con valores de capacidad no válidos (enteros no positivos).
- Probar con nombres de zonas o conexiones duplicados.

Al menos 4 de los 5 casos de error deben gestionarse correctamente con mensajes de error claros.

# Mecánicas de zonas y movimientos

## Reglas de ocupación de las zonas

Prueba las reglas de ocupación de zonas con restricciones de capacidad:

- Las zonas respetan la capacidad máxima de drones (`max_drones`, valor predeterminado: 1).
- Los drones no pueden entrar en zonas cuya capacidad se superaría.
- Varios drones pueden compartir las zonas inicial y final.
- Las restricciones de capacidad se aplican correctamente durante la simulación.

Crea casos de prueba para verificar que estas reglas se cumplen.

## Costes de movimiento

Prueba los costes de movimiento según el tipo de zona:

- zonas normales: 1 turno (predeterminado);
- zonas restringidas: 2 turnos;
- zonas prioritarias: 1 turno (pero se prefieren en la búsqueda de caminos);
- zonas bloqueadas: inaccesibles.

Verifica que la simulación respeta estos costes de movimiento en la salida.

## Capacidad de las conexiones

Prueba las restricciones de capacidad de las conexiones:

- Las conexiones respetan `max_link_capacity`, definido en los metadatos de la conexión (valor predeterminado: 1).
- Varios drones pueden atravesar simultáneamente conexiones con alta capacidad.
- Los límites de capacidad de las conexiones se aplican durante el movimiento.

Verifica que las restricciones de capacidad funcionan correctamente en la simulación.

# Representación visual

## Funcionalidades de visualización

Prueba las funcionalidades de representación visual:

- El programa proporciona una retroalimentación visual clara (salida coloreada en el terminal y/o interfaz gráfica).
- Los colores especificados en los metadatos de las zonas se utilizan para la visualización.
- La representación visual mejora la comprensión de la simulación.
- El sistema visual muestra claramente las posiciones y movimientos de los drones.
- La implementación debe demostrar una retroalimentación visual significativa.

# Pruebas de funcionalidad básica

## Escenarios sencillos

Prueba con escenarios sencillos:

- Probar con un único dron en un camino lineal.
- Probar con varios drones utilizando diferentes caminos.
- Probar con los mapas de ejemplo proporcionados en `attachments/`.
- Verificar el formato de salida: cada línea representa un turno, con el formato `D<ID>-<zone>` o `D<ID>-<connection>`.
- Verificar que los drones que permanecen estacionarios se omiten de la salida.

Al menos 4 de las 5 pruebas básicas deben superarse correctamente.

## La simulación termina correctamente

Comprueba que la simulación termina correctamente cuando todos los drones llegan a la zona final.

El programa debe dejar de producir salida una vez que todos los drones han llegado.

# Algoritmo de búsqueda de caminos

## Camino válido

El algoritmo de búsqueda de caminos encuentra correctamente caminos válidos desde la zona inicial hasta la zona final para diversos casos de prueba.

Prueba con:

- mapas lineales sencillos;
- mapas con múltiples caminos posibles;
- mapas con cuellos de botella y restricciones de capacidad;
- mapas que utilizan diferentes tipos de zona.

El algoritmo debería encontrar soluciones válidas para la mayoría de los casos de prueba.

## Resolución de conflictos

Prueba la resolución de conflictos y la gestión de capacidades:

- Probar escenarios en los que los drones compiten por una capacidad limitada.
- Verificar que el algoritmo gestiona varios drones simultáneamente.
- Comprobar que las restricciones de capacidad evitan conflictos.
- Probar movimientos por turnos con zonas que requieren varios turnos (restringidas).

El algoritmo debe demostrar una resolución de conflictos adecuada y consciente de las capacidades.

# Rendimiento y optimización

## Eficiencia

Prueba escenarios más complejos para evaluar el rendimiento:

- Probar con un número mayor de drones (10 o más).
- Probar con topologías de mapas complejas y restricciones de capacidad.
- Verificar que la solución minimiza el número total de turnos de la simulación.
- Probar el rendimiento con grafos grandes.

**Nota:** esto no es un requisito cuyo incumplimiento implique suspender, pero debe mostrar un rendimiento razonable.

## Explicación del algoritmo

El estudiante puede explicar la complejidad de su algoritmo, las decisiones de diseño y las ventajas y desventajas (*trade-offs*) consideradas en su implementación.

Debe ser capaz de explicar su enfoque de búsqueda de caminos, la gestión de capacidades y las estrategias de optimización.

# Pruebas de rendimiento

## Mapas fáciles

Prueba el rendimiento comparándolo con los valores de referencia proporcionados utilizando los mapas disponibles:

¿El algoritmo resuelve los mapas fáciles en menos de 10 turnos de media?

### Objetivos de referencia (solo informativos)

- Camino lineal (2 drones): ≤ 6 turnos.
- Bifurcación simple (4 drones): ≤ 8 turnos.
- Capacidad básica (4 drones): ≤ 6 turnos.

Estos valores de referencia se proporcionan como objetivos de optimización para ayudar a los estudiantes a evaluar y ajustar sus algoritmos.

## Mapas medios

Prueba el rendimiento comparándolo con los valores de referencia proporcionados utilizando los mapas disponibles:

¿El algoritmo resuelve los mapas medios en 10–30 turnos de media?

### Objetivos de referencia (solo informativos)

- Trampa de callejón sin salida (5 drones): ≤ 12 turnos.
- Bucle circular (6 drones): ≤ 15 turnos.
- Rompecabezas de prioridad (5 drones): ≤ 12 turnos.

Estos valores de referencia se proporcionan como objetivos de optimización para ayudar a los estudiantes a evaluar y ajustar sus algoritmos.

## Mapas difíciles

Prueba el rendimiento comparándolo con los valores de referencia proporcionados utilizando los mapas disponibles:

¿El algoritmo resuelve los mapas difíciles en menos de 60 turnos de media?

### Objetivos de referencia (solo informativos)

- Pesadilla del laberinto (8 drones): ≤ 30 turnos.
- Infierno de capacidad (12 drones): ≤ 35 turnos.
- Desafío definitivo (15 drones): ≤ 45 turnos.

Estos valores de referencia se proporcionan como objetivos de optimización para ayudar a los estudiantes a evaluar y ajustar sus algoritmos.

# Casos límite y gestión de errores

## Casos límite

Prueba casos límite:

- escenarios con un único dron;
- mapas con cuellos de botella o capacidad limitada;
- grafos desconectados (deben gestionarse correctamente);
- conexiones no válidas entre zonas;
- valores de capacidad cero o muy altos.

Al menos 4 de los 5 casos límite deben gestionarse correctamente.

## Gestión de errores

El programa proporciona una gestión de errores adecuada para entradas no válidas:

- archivos malformados con los nuevos requisitos de formato;
- ausencia de zonas `start_hub` o `end_hub`;
- valores de capacidad no válidos;
- grafos desconectados;
- tipos de zona o conexiones no válidos.

Los mensajes de error deben ser claros e informativos.

# Calidad del código y documentación

## Calidad del código

Evaluación de la calidad del código:

- El código está bien estructurado y es legible.
- Se utilizan correctamente los principios de orientación a objetos.
- Los comentarios y la documentación son adecuados.
- El estilo de codificación es coherente.
- El código de representación visual está bien integrado.

**Nota:** esto no es un requisito cuyo incumplimiento implique suspender, pero contribuye a la calidad general.

# Modificaciones rápidas mediante programación en directo

## Programación en directo

Pide al estudiante evaluado que añada una modificación sencilla a su programa de simulación de drones.

Pídele que añada un indicador `--capacity-info` que muestre información sobre las capacidades durante la simulación, por ejemplo:

```text
Zone X: Y/Z drones, Connection A-B: Y/Z capacity used
```

para cada turno.

Por ejemplo:

```bash
./main.py --capacity-info map.txt
```

debería mostrar la simulación normal junto con la información sobre el uso de las capacidades.

El estudiante evaluado debería ser capaz de localizar el código relevante de análisis y de salida, realizar las modificaciones necesarias y demostrar que funcionan con un caso de prueba.

La tarea completa, incluida la demostración, no debería llevar más de 10 minutos.

**¿Se siguió este procedimiento y funcionó todo correctamente?**

# Funcionalidades adicionales

## Rendimiento excepcional

# Finalizar la evaluación

El rendimiento cumple «perfectamente» los objetivos de referencia de rendimiento para todos los mapas proporcionados.

«Perfectamente» significa que el algoritmo alcanza exactamente o mejora el número de turnos especificado en los objetivos de referencia para cada categoría de mapa.

### Objetivos

#### Mapas fáciles

- Camino lineal (2 drones): ≤ 6 turnos.
- Bifurcación simple (4 drones): ≤ 8 turnos.
- Capacidad básica (4 drones): ≤ 6 turnos.

#### Mapas medios

- Trampa de callejón sin salida (5 drones): ≤ 12 turnos.
- Bucle circular (6 drones): ≤ 15 turnos.
- Rompecabezas de prioridad (5 drones): ≤ 12 turnos.

#### Mapas difíciles

- Pesadilla del laberinto (8 drones): ≤ 30 turnos.
- Infierno de capacidad (12 drones): ≤ 35 turnos.
- Desafío definitivo (15 drones): ≤ 45 turnos.

## Mapa Challenger

El mapa «The Impossible Dream» se resuelve y supera el récord de referencia de 45 turnos.
