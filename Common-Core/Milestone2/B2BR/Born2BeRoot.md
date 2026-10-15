# 🚀 Born2beroot

## 🚀 Born2beroot Project

Guia: **https://noreply.gitbook.io/born2beroot**

## 🚀 Born2beroot Tests

## 📌 0. Guidelines

### ⚠️ Rules

- La evaluación debe realizarse de forma respetuosa, constructiva y seria.
- La defensa solo puede realizarse si el alumno evaluado está presente.
- La evaluación se realiza únicamente sobre el contenido entregado en el **repositorio Git del alumno**.
- Verifica que el repositorio pertenece al alumno y que corresponde al proyecto correcto.
- Comprueba que `git clone` se realiza en una carpeta vacía.
- Comprueba que no se han utilizado aliases maliciosos para evaluar contenido distinto al repositorio oficial.
- Si procede, revisa junto al alumno los scripts utilizados para facilitar la evaluación.
- Si el evaluador no ha realizado el proyecto, debe leer previamente el subject completo.
- Si se sospecha cheating, la evaluación se detiene inmediatamente y se utiliza la flag correspondiente.
- Si no existe trabajo, hay archivos/directorios incorrectos o faltan los archivos esperados, la evaluación termina con 0.
- Durante la defensa, el alumno debe ayudar a verificar los puntos cuando sea necesario.
- Si algo no funciona o no puede explicarse claramente en una cuestión obligatoria, la evaluación se detiene en ese punto.

### 🚩 Stop conditions

- **Empty work → El trabajo está vacío**
- **Incomplete work → Trabajo incompleto**
- **Cheat → Uso de cheating**
- **Crash → Error/crash durante la evaluación**
- **Concerning situation → Situación preocupante**
- **Can't support / explain code → El alumno no puede explicar o defender la implementación**

---
# 💻 1. Preliminary Checks

## 📁 Repository

- El repositorio Git pertenece al alumno.
- Es el proyecto Born2beroot correcto.
- `git clone` se ha realizado en una carpeta vacía.
- Los archivos esperados están presentes.
- No se ha utilizado ningún alias malicioso para modificar el contenido evaluado.

## 👤 Student Presence

- El alumno está presente durante toda la defensa.
- El alumno puede ayudar a comprobar y explicar las configuraciones.
- El alumno puede explicar las decisiones tomadas en la máquina virtual.

---
# 🔐 2. Virtual Machine Integrity

## 📄 `signature.txt`

Comprueba que existe `signature.txt` en la raíz del repositorio.

### 🔍 Signature Test

- Compara la firma contenida en `signature.txt` con la firma del disco de la máquina virtual.
- Para VirtualBox, el disco puede tener extensión `.vdi`.
- Si se utiliza otro proveedor como UTM, el disco puede tener otra extensión.
- Utiliza `diff` o un método equivalente.

### 📸 Snapshots

- Comprueba que no existen snapshots.
- Puedes crear un cold snapshot y eliminarlo al terminar, o duplicar el disco y arrancar desde la copia.
- El disco original debe permanecer intacto para conservar su firma.

### ▶️ VM Startup

- La máquina virtual no debe estar ejecutándose antes de la defensa.
- Arranca la máquina durante la evaluación.
- Si algo no funciona o las firmas difieren, la evaluación se detiene.

---
# 📖 3. README.md

**Archivo:** `README.md`

### 🔍 Required Content

Debe existir en la raíz.

La primera línea debe estar en cursiva y seguir el formato:

```text
This project has been created as part of the 42 curriculum by <login...>
```

Debe incluir:

- **Project description**
- **OS choice**, con pros y contras.
- **Main design choices**:
  - Partitioning
  - Security policies
  - User management
  - Services

### Required Comparisons

- Debian vs Rocky Linux
- AppArmor vs SELinux
- UFW vs firewalld
- VirtualBox vs UTM

### 🛑 Stop Condition

Si falta cualquiera de estos elementos obligatorios, la evaluación termina aquí.

---
# 🧠 4. Project Overview & OS

El alumno debe explicar claramente:

- Cómo funciona una máquina virtual.
- Para qué sirven las máquinas virtuales.
- Qué sistema operativo ha elegido y por qué.
- Diferencias básicas entre Debian y Rocky Linux.

### Si utiliza Rocky Linux

Debe explicar:

- Qué es **SELinux**.
- Qué es **DNF**.

### Si utiliza Debian

Debe explicar:

- Diferencia entre `aptitude` y `apt`.
- Qué es **AppArmor**.

Si las explicaciones no son claras, la evaluación se detiene.

---
# ⚙️ 5. Simple Setup

## 🖥️ Graphical Environment

Comprueba que:

- La máquina no arranca con un entorno gráfico.
- Se solicita contraseña.
- Se puede iniciar sesión con un usuario normal.
- El usuario no es root.
- La contraseña respeta las reglas del subject.

## 🔥 Firewall

- UFW está iniciado en Debian.
- Firewalld está iniciado en Rocky.

## 🔑 SSH

- SSH está iniciado.
- El servicio funciona correctamente.

## 🐧 Operating System

- El sistema es Debian o Rocky.
- La configuración corresponde a la elección declarada.

Si algo no funciona o no puede explicarse claramente, la evaluación se detiene.

---
# 👤 6. User Step 1 — Student User

Debe existir un usuario con el login del alumno.

### 🔍 Groups

Comprueba que pertenece a:

```text
sudo
user42
```

### 🔐 Password Policy

Crea un nuevo usuario durante la defensa.

- Asigna una contraseña que respete las reglas del subject.
- El alumno debe explicar cómo configuró las reglas en la VM.
- Normalmente debe haber uno o dos archivos modificados para implementar la política.

Si algo no funciona, la evaluación se detiene.

---
# 👥 7. User Step 2 — Evaluating Group

Durante la defensa, pide al alumno:

1. Crear un grupo llamado `evaluating`.
2. Asignar el nuevo usuario a dicho grupo.
3. Comprobar que el usuario pertenece a `evaluating`.

### 🧠 Password Policy Explanation

El alumno debe explicar:

- Ventajas de la política de contraseñas.
- Ventajas de su implementación.
- Desventajas de su implementación.
- Motivo técnico de las decisiones.

Responder únicamente “porque lo pide el subject” no cuenta como explicación válida.

---
# 🏷️ 8. Hostname

El hostname debe tener el formato:

```text
login42
```

donde `login` es el login del alumno.

### 🧪 Hostname Test

1. Comprueba el hostname actual.
2. Sustituye el login del alumno por el del evaluador.
3. Reinicia la máquina.
4. Comprueba que el hostname se ha actualizado.
5. Restaura el hostname original.

Si después del reinicio no se actualiza correctamente, la evaluación se detiene.

---
# 💾 9. Partitions & LVM

### 🔍 Partition Check

- Pide al alumno que muestre las particiones.
- Compara la salida con el ejemplo del subject.
- Si existen bonuses de particiones, utiliza también el ejemplo correspondiente.

### 🧠 LVM Explanation

El alumno debe explicar:

- Qué es LVM.
- Cómo funciona.
- Para qué sirve.
- Cómo se utiliza en su configuración.

Si algo no funciona o no puede explicarse claramente, la evaluación se detiene.

---
# 🔑 10. SUDO

## 📦 Installation

Comprueba que `sudo` está instalado.

## 👤 User Assignment

El alumno debe mostrar cómo asignar el nuevo usuario al grupo `sudo`.

## 🧠 Explanation

Debe explicar:

- Qué es `sudo`.
- Para qué sirve.
- Cómo funciona.
- Ejemplos de uso.

## 🔒 SUDO Rules

Debe mostrar la implementación de las reglas impuestas por el subject.

## 📝 SUDO Logs

Debe existir:

```text
/var/log/sudo/
```

y contener al menos un archivo.

Comprueba:

- Existencia del directorio.
- Existencia de logs.
- Contenido.
- Historial de comandos usados con sudo.

### 🧪 Dynamic Log Test

Ejecuta un comando mediante `sudo` y comprueba que los logs se actualizan.

---
# 🧱 11. UFW / Firewalld

## 📦 Installation

Comprueba:

- `UFW` para Debian.
- `Firewalld` para Rocky.

## ▶️ Service

Comprueba que funciona correctamente.

## 🧠 Explanation

El alumno debe explicar qué es y para qué sirve.

## 🔍 Active Rules

Lista las reglas activas.

Debe existir una regla para:

```text
port 4242
```

## 🧪 Rule Management Test

1. Lista las reglas.
2. Añade una regla para abrir `8080`.
3. Comprueba que aparece.
4. Elimina la regla de `8080`.

Si algo no funciona o no puede explicarse claramente, la evaluación se detiene.

---
# 🔑 12. SSH

## 📦 Installation

Comprueba que SSH está instalado y funcionando.

## 🧠 Explanation

El alumno debe explicar:

- Qué es SSH.
- Para qué sirve.
- Ventajas de utilizarlo.

## 🔌 Port

SSH debe utilizar únicamente:

```text
port 4242
```

## 👤 User Login

Utiliza SSH para iniciar sesión con el nuevo usuario, mediante clave o contraseña según la configuración.

### 🚫 Root Login

Comprueba que no se puede iniciar sesión mediante SSH con `root`.

---
# 📊 13. Monitoring Script

Durante la defensa, el script debe mostrar información cada **10 minutos**.

## 🧠 Script Explanation

El alumno debe explicar:

- Cómo funciona.
- Mostrar el código.
- Qué es `cron`.
- Cómo configuró el script para ejecutarse cada 10 minutos desde el arranque.

## ⏱️ Dynamic Frequency Test

Una vez verificado:

- Configura temporalmente el script para ejecutarse cada minuto.
- Comprueba que funciona con valores dinámicos.

## 🛑 Stop Script Without Modification

Finalmente:

- El alumno debe hacer que el script deje de ejecutarse cuando el servidor haya arrancado.
- No puede modificar el script.

### 🔄 Final Restart

Reinicia el servidor y comprueba:

- El script sigue en la misma ubicación.
- Los permisos no han cambiado.
- El script no ha sido modificado.

Si algo no funciona o no puede explicarse claramente, la evaluación se detiene.

---
# ⭐ 14. Bonuses

> Los bonuses solo se evalúan si toda la parte obligatoria ha sido completada perfectamente y la gestión de errores funciona ante usos inesperados o incorrectos.

Si no se han superado todos los puntos obligatorios, los bonuses se ignoran.

## 💾 Bonus — Partitions

**Valor: 2 puntos**

- Comprueba la configuración adicional de particiones.
- Compara con el subject.
- Verifica que funciona correctamente.

## 🌐 Bonus — WordPress

**Valor: 2 puntos**

- Comprueba la instalación de WordPress.
- Utiliza únicamente los servicios requeridos por el subject.
- Verifica funcionamiento e implementación.

## 🛠️ Bonus — Free Choice Service

**Valor: 1 punto**

- Comprueba el servicio elegido.
- Verifica instalación, funcionamiento e implementación.
- El alumno explica cómo funciona y por qué es útil.

### 🚫 Prohibited

Para el free choice service:

- `NGINX` está prohibido.
- `Apache2` está prohibido.

### 📊 Bonus Rating

Valora la parte bonus de `0 → 5`.

---
# 🧹 15. Configuration & Security Quality

## 🖥️ System

- Debian o Rocky correctamente configurado.
- Servicios funcionando.
- Configuraciones explicables.

## 🔐 Security

- Password policy configurada.
- `sudo` correctamente configurado.
- Logs de sudo funcionando.
- Firewall activo.
- Port `4242` configurado.
- Port `8080` puede abrirse y eliminarse.
- SSH funcionando.
- Root bloqueado en SSH.

## 👤 User Management

- Usuario del alumno presente.
- Pertenece a `sudo`.
- Pertenece a `user42`.
- Puede crearse y utilizarse `evaluating`.
- Política de contraseñas implementada.

## 🧠 Understanding

- El alumno entiende VM.
- Entiende LVM.
- Entiende sudo.
- Entiende firewall.
- Entiende SSH.
- Entiende cron.
- Puede explicar sus decisiones.

---
# 🚩 16. Defense

## 💬 Questions

1. ¿Qué es una máquina virtual y cómo funciona?
2. ¿Por qué elegiste Debian/Rocky?
3. ¿Cuáles son las diferencias principales entre Debian y Rocky?
4. Si utilizas Debian, ¿cuál es la diferencia entre `apt` y `aptitude`?
5. Si utilizas Debian, ¿qué es AppArmor?
6. Si utilizas Rocky, ¿qué es SELinux?
7. Si utilizas Rocky, ¿qué es DNF?
8. ¿Qué es LVM y cómo funciona?
9. ¿Por qué elegiste esta estructura de particiones?
10. ¿Qué ventajas tiene la política de contraseñas?
11. ¿Qué desventajas tiene?
12. ¿Qué es `sudo`?
13. ¿Cómo funciona `sudo`?
14. ¿Por qué se registran los comandos ejecutados mediante sudo?
15. ¿Qué es UFW/Firewalld?
16. ¿Por qué está abierto el puerto `4242`?
17. ¿Cómo añadirías y eliminarías una regla para `8080`?
18. ¿Qué es SSH?
19. ¿Por qué SSH utiliza `4242`?
20. ¿Por qué no se permite SSH con `root`?
21. ¿Qué es `cron`?
22. ¿Cómo configuraste el script para ejecutarse cada 10 minutos desde el arranque?
23. ¿Cómo puedes cambiar temporalmente la frecuencia a un minuto sin modificar el script?
24. ¿Cómo puedes hacer que el script deje de ejecutarse al arrancar sin modificarlo?
25. ¿Qué información muestra el script de monitoring?
26. ¿Cómo se obtienen sus valores dinámicos?
27. ¿Qué diferencia hay entre AppArmor y SELinux?
28. ¿Qué diferencia hay entre UFW y Firewalld?
29. ¿Qué diferencia hay entre VirtualBox y UTM?
30. ¿Por qué una máquina virtual es útil para este proyecto?

---
# 📝 17. Final Evaluation

### Checklist

- Alumno presente
- Repositorio correcto
- Repositorio no vacío
- VM correcta
- `signature.txt` presente
- Signature coincide con el disco
- No existen snapshots
- VM no estaba ejecutándose antes de la defensa
- VM arranca correctamente
- `README.md` presente
- Primera línea correcta
- Project description
- OS choice
- Main design choices
- Debian vs Rocky
- AppArmor vs SELinux
- UFW vs Firewalld
- Virtualización explicada
- Sistema operativo correcto
- Sin entorno gráfico al arrancar
- Usuario no-root
- Password policy
- Usuario del alumno
- Grupo `sudo`
- Grupo `user42`
- Grupo `evaluating`
- Password policy explicada
- Hostname correcto
- Hostname persiste tras reboot
- Particiones correctas
- LVM explicado
- Sudo instalado
- Sudo explicado
- Reglas sudo implementadas
- `/var/log/sudo/` existe
- Logs sudo presentes
- Logs sudo se actualizan
- UFW/Firewalld instalado
- Firewall funcionando
- Port `4242`
- Port `8080` añadido
- Port `8080` eliminado
- SSH instalado
- SSH funcionando
- SSH solo en `4242`
- Login SSH con nuevo usuario
- Root SSH bloqueado
- Monitoring script
- Cron explicado
- Script cada 10 minutos
- Script cada minuto durante la prueba
- Valores dinámicos correctos
- Script detenido al startup sin modificarlo
- Script intacto después del reboot
- Bonuses evaluados, si procede
- Defense completada
- Alumno puede explicar la configuración

### 🚩 Flags

- Ok
- Outstanding project
- Empty work
- Incomplete work
- Cheat
- Crash
- Concerning situation
- Can't support / explain code

### 📊 Result

**Rating:** `0 → 5`

### 💬 Conclusion

> Escribe aquí los comentarios finales de la evaluación, indicando los puntos relevantes observados durante la defensa.
