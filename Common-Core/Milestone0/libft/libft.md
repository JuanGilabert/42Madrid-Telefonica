# Instrucciones Generales
- El proyecto deberá estar escrito en C.
- El proyecto debe estar escrito siguiendo la Norma.
    Si tienes archivos o funciones adicionales, estas deberán estar incluidas en la verificación de la Norma y tendrás
    un 0 si hay algún error de norma en cualquiera de ellos.
- Las funciones no deben terminar de forma inesperada (segfault, bus error, double free, etc), excepto en el caso de comportamientos indefinidos.
    Si esto sucede, el proyecto será considerado no funcional y recibirás un 0 durante la evaluación.
- Toda la memoria asignada en la pila (heap) deberá liberarse adecuadamente cuando sea necesario. No se permitirán leaks de memoria.
- Si el enunciado lo requiere, se deberá entregar un Makefile que compilará tus archivos fuente a la salida requerida con las flags -Wall, -Werror y -Wextra.
    También se deberá utilizar cc y, por supuesto, el Makefile no debe hacer relink.
- El Makefile entregado debe contener al menos las normas $(NAME), all, clean, fclean y re.
- Para entregar los bonus del proyecto se deberá incluir una regla bonus en el Makefile,
    en la que se añadirán todos los headers, librerías o funciones que estén prohibidas
    en la parte principal del proyecto. Los bonus deben estar en archivos distintos ×
    _bonus.{c/h}. La parte obligatoria y los bonus se evalúan por separado.
- Si el proyecto permite el uso de la libft, se deberá copiar su fuente y sus Makefile asociados en un directorio libft con su correspondiente Makefile.
    El Makefile del proyecto debe compilar primero la librería utilizando su Makefile, y después compilar el proyecto.
- Es recomendable crear programas de prueba para el proyecto, aunque este trabajo no será entregado ni evaluado.
    Esto ofrece la oportunidad de verificar que el programa funciona correctamente durante las evaluaciones.
    Y sí, está permitido utilizar estas pruebas durante cualquier evaluación.
- Entrega el trabajo en el repositorio Git asignado. Solo el trabajo de tu repositorio Git será evaluado.
    Si el proyecto tiene que ser evaluado por Deepthought, la evaluación se realizará después de las evaluaciones personales.
    Si, durante la evaluación de Deepthought, se encuentra un error se, se interrumpirá su evaluación.

# Consideraciones Tecnicas
- Declarar variables globales está prohibido.
- Si necesitas crear funciones auxiliares para descomponer una función más compleja,
    debes definirlas como static para restringir su alcance al archivo correspondiente.
- Todos los archivos deben colocarse en la raíz de tu repositorio.
- Se prohíbe entregar archivos no utilizados.
- Todos los archivos .c deben compilarse con las opciones (flags) -Wall -Werror -Wextra.
- Debes utilizar el comando ar para generar la librería. El uso de libtool queda prohibido.
- Tu libft.a debe ser creado en la raíz de tu repositorio.

# Funciones de libc
- Para empezar, deberás rehacer algunas funciones de la libc. Tus funciones tendrán
    los mismos prototipos y comportamientos que las funciones originales, siguiendo fielmente
    las definiciones indicadas en la página del man de cada función. La única diferencia será el
    nombre: todas deberán comenzar con el prefijo “ft_”. Por ejemplo, strlen se convertirá en ft_strlen.
- Algunas funciones tienen en sus prototipos la palabra “restrict”.
    Esta palabra forma parte del estándar de c99. Por lo tanto, está
    prohibido incluirla en tus propios prototipos, así como compilar tu código con la opción -std=c99.
- Deberás escribir tus propias versiones de las siguientes funciones originales. No deben depender de ninguna función externa.
- Algunas de las funciones que debes rehacer, como strlcpy, strlcat y bzero, no están incluidas por defecto en la biblioteca GNU C (glibc).
    Para compararlas con la versión estándar del sistema, puede ser necesario incluir <bsd/string.h> y compilar con la opción -lbsd.
    Este comportamiento es propio de los sistemas basados en glibc.
    Si tienes interés, vale la pena aprovechar la ocasión para explorar las diferencias entre glibc y la biblioteca libc de BSD.
- Para implementar estas otras dos funciones, tendrás que utilizar malloc(): calloc y strdup.

# Parte obligatoria de libc
## Ejercicio principal: libft
### Indicaciones
- **`Nombre programa`**: libft.a
- **`Archivos a entregrar`**: Makefile, libft.h, ft_*.c
- **`Makefile`**: NAME, all, clean, fclean, re
- **`Funciones autorizadas`**: Se detallan debajo.
- **`Se permite usar libft`**: Todavía no disponible.
### Descripcion
- **`libft.a`**: Escribe tu propia librería: un conjunto de funciones que será una herramienta muy útil a lo largo del cursus.


## Ejercicio: ft_isalpha
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_isalpha.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_isalpha`**: Crea una función que determine si un string dado contiene solo letras.
### Prototipo
- **`int isalpha(char *str);`**:
    El prototipo de la función deberá ser el siguiente: `int ft_isalpha(char *str)`.
### Valor de retorno
- Devuelve 1 si el string usado como parámetro contiene únicamente caracteres alfabéticos o si es un string vacío.
- Devuelve 0 si contiene otro tipo de caracteres que no sean alfabéticos.


## Ejercicio: ft_isdigit
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_isdigit.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_isdigit`**: Crea una función que determine si un string dado contiene solo dígitos.
### Prototipo
- **`int isdigit(char *str);`**:
    El prototipo de la función deberá ser el siguiente: `int ft_isdigit(char *str)`.
### Valor de retorno
- Devuelve 1 si el string usado como parámetro contiene únicamente dígitos o si es un string vacío.
- Devuelve 0 si contiene otro tipo de caracteres que no sean digitos.


## Ejercicio: ft_isalnum
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_isalnum.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_isalnum`**: Crea una función que determine si un carácter dado es alfanumérico.
### Prototipo
- **`int isalnum(int c);`**:
    El prototipo de la función deberá ser el siguiente: `int ft_isalnum(int c)`.
### Valor de retorno
- Devuelve un valor distinto de cero si el carácter es alfanumérico.
- Devuelve 0 si no es alfanumérico.


## Ejercicio: ft_isascii
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_isascii.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_isascii`**: Crea una función que determine si un carácter dado tiene un valor ASCII válido.
### Prototipo
- **`int isascii(int c);`**:
    El prototipo de la función deberá ser el siguiente: `int ft_isascii(int c)`.
### Valor de retorno
- Devuelve un valor distinto de cero si el carácter es un valor ASCII válido.
- Devuelve 0 si el carácter no es un valor ASCII válido.


## Ejercicio: ft_isprint
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_isprint.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_isprint`**: Crea una función que determine si un carácter dado es un carácter imprimible en el conjunto de caracteres ASCII estándar.
    Un carácter es imprimible si es visible y puede ser impreso en pantalla.
### Prototipo
- **`int isprint(int c);`**:
    El prototipo de la función deberá ser el siguiente: `int ft_isprint(int c)`.
### Valor de retorno
- Devuelve un valor distinto de cero si el carácter es imprimible.
- Devuelve 0 si el carácter no es imprimible.


## Ejercicio: ft_toupper
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_toupper.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_toupper`**: Crea una función que ponga cada letra en mayúscula. (version de ft_strupcase en ex07_C02)
### Prototipo
- **`int toupper(int c);`**:
    El prototipo de la función deberá ser el siguiente: `int ft_toupper(int c)`.
### Valor de retorno
- Devuelve str por convencion.

## Ejercicio: ft_tolower
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_tolower.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_tolower`**: Crea una función que ponga cada letra en minúscula(version de ft_strlowcase en ex08_C02).
### Prototipo
- **`int tolower(int c);`**:
    El prototipo de la función deberá ser el siguiente: `int ft_tolower(int c)`.
### Valor de retorno
- Devuelve str por convencion.

## Ejercicio: ft_strlen (COMPROBAR SI EN PISCINA DEVUELVE INT O SIZE_T)
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_strlen.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_strlen`**: Reproduce el comportamiento de la funcion strlen (man strlen).
    Escribe una función que cuente el número de caracteres de un string.
### Prototipo
- **`size_t strlen(const char *s);`**: El prototipo de la función deberá ser el siguiente: `size_t ft_strlen(const char *s)`.
### Valor de retorno
-  Devuelve el numero de caracteres del string.
- returns the number of bytes in the string pointed to by s.

## Ejercicio: ft_strlcpy
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_strlcpy.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_strlcpy`**: Reproduce el comportamiento de la función strlcpy (man strlcpy)(equivalente a strncpy).
    La funcion `strlcpy` sirve para copiar cadenas de texto de forma más segura que `strcpy`, evitando desbordamientos de búfer (buffer overflow).
### Prototipo
- **`size_t	ft_strlcpy(char *dst, const char *src, size_t size);`**:
    El prototipo de la función deberá ser el siguiente: `size_t	ft_strlcpy(char *dst, const char *src, size_t size)`.
### Valor de retorno
- Devuelve la longitud total de src.

## Ejercicio: ft_strncmp
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_strncmp.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_strncmp`**: Reproduce el comportamiento de la función strncmp (man strncmp).
    Sirve para comparar dos cadenas de caracteres hasta un número máximo de caracteres.
### Prototipo
- **`int strncmp(char *s1, char *s2, unsigned int n);`**:
    El prototipo de la función deberá ser el siguiente: `int ft_strncmp(char *s1, char *s2, unsigned int n)`.
### Valor de retorno
- Devuelve 0 → si son iguales en los primeros n caracteres.
- Devuelve <0 → si s1 es menor que s2.
- Devuelve >0 → si s1 es mayor que s2.

## Ejercicio: ft_strlcat
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_strlcat.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_strlcat`**: Reproduce el comportamiento de la función strlcat (man strlcat).
    La funcion `strlcat` sirve para concatenar cadenas de forma más segura que `strcat`, evitando desbordamientos de buffer.
    Añade src al final de dst. Siempre intenta terminar la cadena con '\0' (si size > 0).
### Prototipo
- **`size_t strlcat(char *dst, const char *src, size_t size);`**:
    El prototipo de la función deberá ser el siguiente: `size_t ft_strlcat(char *dst, const char *src, size_t size)`.
### Valor de retorno
- Devuelve la longitud total que intentó crear: longitud_inicial(dst) + longitud(src)

## Ejercicio: ft_strnstr
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_strnstr.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_strstr`**: Reproduce el comportamiento de la función strstr (man strnstr).
    Sirve para localizar la primera aparición de la cadena `little` dentro de la cadena `big`, donde no se buscan más de `len` caracteres.
    Si little es una cadena vacía, big se devuelve directamente.
### Prototipo
- **`char *strnstr(const char *big, const char *little, size_t len);`**:
    El prototipo de la función deberá ser el siguiente: `char *ft_strnstr(const char *big, const char *little, size_t len)`.
### Valor de retorno
- Devuelve un puntero al inicio de la subcadena encontrada si `little` se encuentra dentro de los primeros `len` caracteres de `big`.
- Si no se encuentra, devuelve `NULL`.
- Variante del strstr, el cual da KO de Moulinette debido a un error en la firma de la funcion creo.

## Ejercicio: ft_atoi (AJUSTAR ENUNCIADO)
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_atoi.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_atoi`**: Escribe una función que convierta el principio del string apuntado por str en un entero de tipo int.
    str puede empezar con un número arbitrario de espacios (tal y como lo define isspace(3)).
    str puede ir seguido de un número arbitrario de signos + y de signos -.(ESTO ES LO QUE PUEDE HABER CAMBIADO CONRESPECTO A LA PISCINA, AJUSTAR EL ENUNCIADO).
    El signo - hará cambiar el signo del entero devuelto en función del número de signos - y si este es par o impar.
    str puede ir seguido de cualquier cantidad de números de dígitos en base 10.
    La función tendrá que leer los caracteres de str, siempre que estos cumplan con las reglas
    mencionadas anteriormente, y tendrá que devolver el número encontrado hasta entonces.
    No deberías tener en cuenta los desbordamientos (overflows y underflows), en estos casos el resultado se considera indefinido.
    Puedes comparar tu función con la verdadera función atoi, quitando la parte de los signos y del overflow.
### Prototipo
- **`int atoi(const char *nptr);`**: El prototipo de la función deberá ser el siguiente: `int ft_atoi(const char *nptr)`.
### Ejemplo
- **`Entrada`**: ft_atoi("-1234ab567")
- **`Salida`**: -1234

## Ejercicio: ft_strdup (COMPROBAR FIRMA FUNCION EN LA PISCINA Y VERIFICAR SI TIENE QUE SER ESTE O EL DEL MODULO C07)
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_strdup.c
- **`Funciones autorizadas`**: malloc
### Descripcion
- **`ft_strdup`**: Reproduce el comportamiento de la función strdup (man strdup).
    La funcion `strdup` sirve para duplicar una cadena de caracteres. Crea una copia nueva del string `src`.
### Prototipo
- **`char *strdup(const char *s);`**:
    El prototipo de la función deberá ser el siguiente: `char *ft_strdup(const char *s)`.
### Valor de retorno
- Devuelve un puntero a la nueva cadena creada.
- Devuelve `NULL` en caso de error.
- returns a pointer to a new string which is a duplicate of the string s.  Memory for the new string is obtained with malloc(3), and can be freed with free(3).

## Ejercicio: ft_strchr
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_strchr.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_strchr`**: Reproduce el comportamiento de la función strchr (man strchr).
    La función `strchr` se usa para buscar la primera aparición de un carácter dentro de una cadena de texto (string).
### Prototipo
- **`char *strchr(const char *str, int c);`**:
    El prototipo de la función deberá ser el siguiente: `char *ft_strchr(const char *str, int c)`.
### Valor de retorno
- Devuelve un puntero a la primera aparición del carácter en `str`.
- Devuelve `NULL` si no existe el caracter a buscar en `str`.
-  return a pointer to the matched character or NULL if the character is not found.  The terminating null byte is considered part of the string, so that if c is specified as '\0', these functions return a pointer to the terminator.

## Ejercicio: ft_strrchr
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_strrchr.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_strrchr`**: Reproduce el comportamiento de la función strrchr (man strrchr).
    La función `strrchr` se usa para buscar la ultima aparición de un carácter dentro de una cadena de texto (string).
### Prototipo
- **`char *strrchr(const char *str, int c);`**: El prototipo de la función deberá ser el siguiente: `char *ft_strrchr(const char *str, int c)`.
### Valor de retorno
- Devuelve un puntero a la ultima aparición del carácter en `str`.
- Devuelve `NULL` si no existe el caracter a buscar en `str`.
- return a pointer to the matched character or NULL if the character is not found.  The terminating null byte is considered part of the string, so that if c is specified as '\0', these functions return a pointer to the terminator.

## Ejercicio: ft_bzero
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_bzero.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_bzero`**: Reproduce el comportamiento de la función bzero (man bzero).
    La función bzero en C sirve para poner a cero (0) una zona de memoria.
    Llena los primeros `n` bytes de la memoria apuntada por `s` con ceros.
    Pertenece a las funciones clásicas de BSD y hoy se considera obsoleta en favor de memset(equivalente a memset(s, 0, n)).
### Prototipo
- **`void bzero(void *s, size_t n);`**: El prototipo de la función deberá ser el siguiente: `void ft_bzero(void *s, size_t n)`.
### Valor de retorno
- No devuelve nada (void).

## Ejercicio: ft_memset
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_memset.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_memset`**: Reproduce el comportamiento de la función memset (man memset).
    La función `memset` sirve para rellenar una zona de memoria con un mismo byte.
### Prototipo
- **`void *memset(void *s, int c, size_t n);`**:
    El prototipo de la función deberá ser el siguiente: `void *ft_memset(void *s, int c, size_t n)`.
### Valor de retorno
- Devuelve el puntero `s` por convencion.

## Ejercicio: ft_memcpy
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_memcpy.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_memcpy`**: Reproduce el comportamiento de la función memcpy (man memcpy).
    La función memcpy copia bloques de memoria byte a byte.
    Copia `n` bytes desde `src` hacia `dest`.
### Prototipo
- **`void *memcpy(void *dest, const void *src, size_t n);`**:
    El prototipo de la función deberá ser el siguiente: `void *ft_memcpy(void *dest, const void *src, size_t n)`.
### Valor de retorno
- Devuelve el puntero `dest` por convencion.

## Ejercicio: ft_memcmp
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_memcmp.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_memcmp`**: Reproduce el comportamiento de la función memcmp (man memcmp).
    La funcion memcmp se usa para comparar dos bloques de memoria byte a byte.
    Compara los primeros n bytes de las áreas de memoria apuntadas por s1 y s2.
### Prototipo
- **`int memcmp(const void *s1, const void *s2, size_t n);`**:
    El prototipo de la función deberá ser el siguiente: `int ft_memcmp(const void *s1, const void *s2, size_t n)`.
### Valor de retorno
- Devuelve 0 → los bloques son iguales en los primeros n bytes
- Devuelve <0 → el primer byte diferente en s1 es menor que el de s2
- Devuelve >0 → el primer byte diferente en s1 es mayor que el de s2

## Ejercicio: ft_memchr
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_memchr.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_memchr`**: Reproduce el comportamiento de la función memchr (man memchr).
    La funcion `memchr` sirve para buscar un byte concreto dentro de un bloque de memoria.
    Recorre los primeros n bytes del bloque de memoria apuntado por s y busca la primera aparición del byte c.
### Prototipo
- **`void *memchr(const void *s, int c, size_t n);`**:
    El prototipo de la función deberá ser el siguiente: `void *ft_memchr(const void *s, int c, size_t n)`.
### Valor de retorno
- Devuelve un puntero al primer byte coincidente dentro de s en caso de encontrarlo.
- Devuelve `NULL` en caso de no encontrarlo.

## Ejercicio: ft_calloc
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_calloc.c
- **`Funciones autorizadas`**: malloc
### Descripcion
- **`ft_calloc`**: Reproduce el comportamiento de la función calloc (man calloc).
    La funcion `calloc` sirve para reservar memoria dinámica para un bloque de elementos y además inicializar esa memoria a cero.
    Reserva memoria para un array de `nmemb` elementos.
    Cada elemento ocupa `size` bytes.
    Inicializa toda la memoria reservada a 0 (bytes en cero).
### Prototipo
- **`void *calloc(size_t nmemb, size_t size);`**:
    El prototipo de la función deberá ser el siguiente: `void *ft_calloc(size_t nmemb, size_t size)`.
### Valor de retorno
- Devuelve un puntero a la zona de memoria reservada.
- Devuelve `NULL` en caso de fallo.
### Notas
- Dependiendo de tu sistema operativo actual, el comportamiento de la función calloc puede diferir de lo descrito en su página del manual.
- Si nmemb o size es 0, entonces calloc() debe devolver un puntero único que pueda pasarse con éxito a free().

## Ejercicio: ft_memmove
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_memmove.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_memmove`**: Reproduce el comportamiento de la función memmove (man memmove).
    La funcion `memmove` sirve para copiar un bloque de memoria de un lugar a otro de forma segura, incluso si las regiones se solapan.
    Copia `n` bytes desde la dirección `src` hacia `dest`.
### Prototipo
- **`void *memmove(void *dest, const void *src, size_t n);`**:
    El prototipo de la función deberá ser el siguiente: `void *ft_memmove(void *dest, const void *src, size_t n)`.
### Valor de retorno
- Devuelve el puntero `dest` por convencion.

# Parte adicional de libc
- En esta segunda parte, deberás desarrollar un conjunto de funciones que, o no son de la librería libc, o lo son pero de una forma distinta.

## Ejercicio: ft_substr
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_substr.c
- **`Funciones autorizadas`**: malloc
### Descripcion
- **`ft_substr`**: Reserva memoria (con malloc(3)) y devuelve una subcadena de caracteres de la cadena `s`.
    La subcadena comienza en el índice `start` y tiene una longitud máxima `len`.
### Prototipo
- **`char *ft_substr(char const *s, unsigned int start, size_t len);`**:
    El prototipo de la función deberá ser el siguiente: `char *ft_substr(char const *s, unsigned int start, size_t len)`.
### Parametros
- **`s`**: La cadena original desde la que se crea la subcadena.
- **`start`**: El índice del carácter en ‘s’ desde el que empieza la subcadena.
- **`len`**: La longitud máxima de la subcadena.
### Valor de retorno
- Devuelve la subcadena de caracteres resultante de la operacion.
- Devuelve `NULL` si falla la reserva de memoria.

## Ejercicio: ft_strjoin
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_strjoin.c
- **`Funciones autorizadas`**: malloc
### Descripcion
- **`ft_substr`**: Reserva memoria (con malloc(3)) y devuelve una nueva cadena de caracteres, formada por la concatenación de `s1` y `s2`.
### Prototipo
- **`char *ft_strjoin(char const *s1, char const *s2);`**:
    El prototipo de la función deberá ser el siguiente: `char *ft_strjoin(char const *s1, char const *s2)`.
### Parametros
- **`s1`**: La primera cadena.
- **`s2`**: La cadena a añadir a `s1`.
### Valor de retorno
- La nueva cadena de caracteres.
- `NULL` si falla la reserva de memoria.

## Ejercicio: ft_strtrim
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_strtrim.c
- **`Funciones autorizadas`**: malloc
### Descripcion
- **`ft_strtrim`**: Reserva memoria (con malloc(3)) y devuelve una copia de ‘s1’ con los caracteres de ‘set ’ eliminados al principio y al final.
### Prototipo
- **`char *ft_strtrim(char const *s1, char const *set);`**:
    El prototipo de la función deberá ser el siguiente: `char *ft_strtrim(char const *s1, char const *set)`.
### Parametros
- **`s1`**: La cadena de caracteres que debe ser recortada.
- **`set`**: Los caracteres a eliminar de la cadena en cuestión.
### Valor de retorno
- La cadena recortada resultante.
- `NULL` si falla la reserva de memoria.

## Ejercicio: ft_split (TRASPASAR ESTE AL DE LA PISCINA)
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_split.c
- **`Funciones autorizadas`**: malloc, free
### Descripcion
- **`ft_split`**: Reserva memoria (utilizando malloc(3)) y devuelve un arreglo (array) de cadenas obtenido al dividir la cadena `s`
    en subcadenas utilizando el carácter `c` como delimitador.
    Cada cadena del arreglo devuelto se reserva de manera independiente.
    El arreglo de punteros también se reserva dinámicamente.
    El arreglo devuelto debe terminar con un puntero a `NULL`.
### Prototipo
- **`char **ft_split(char const *s, char c);`**:
    El prototipo de la función deberá ser el siguiente: `char **ft_split(char const *s, char c)`.
### Parametros
- **`s`**: La cadena que se va a dividir.
- **`c`**: El carácter delimitador.
### Valor de retorno
- El arreglo de nuevas cadenas resultante de la división.
- `NULL` si falla cualquier reserva de memoria.
- La estructura devuelta debe liberarse utilizando:
    1) free() sobre cada cadena del arreglo;
    2) free() sobre el arreglo.

## Ejercicio: ft_itoa
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_itoa.c
- **`Funciones autorizadas`**: malloc
### Descripcion
- **`ft_itoa`**: Reserva memoria (utilizando malloc(3)) y devuelve una cadena que represente el valor del número entero recibido como argumento.
    Debe ser capaz de manejar números negativos.
### Prototipo
- **`char *ft_itoa(int n);`**:
    El prototipo de la función deberá ser el siguiente: `char *ft_itoa(int n)`.
### Parametros
- **`n`**: el entero a convertir.
### Valor de retorno
- La cadena que represente el número.
- `NULL` si falla la reserva de memoria.

## Ejercicio: ft_strmapi (FUNCIONA PERO PROBAR DE NUEVO, NO ME MOLA LA FUNCION AUXILIAR)
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_strmapi.c
- **`Funciones autorizadas`**: malloc
### Descripcion
- **`ft_strmapi`**: Aplica la función `f` a cada carácter de la cadena `s`, pasando su índice como primer argumento y el propio carácter como segundo argumento.
    Se crea una nueva cadena (utilizando `malloc(3)`) para almacenar los resultados de las sucesivas aplicaciones de `f`.
### Prototipo
- **`char *ft_strmapi(char const *s, char (*f)(unsigned int, char));`**:
    El prototipo de la función deberá ser el siguiente: `char *ft_strmapi(char const *s, char (*f)(unsigned int, char))`.
### Parametros
- **`s`**: La cadena sobre la que iterar.
- **`f`**: La función a aplicar sobre cada carácter.
### Valor de retorno
- Devuelve la cadena creada tras el correcto uso de `f` sobre cada carácter.
- Devuelve `NULL` si falla la reserva de memoria.

## Ejercicio: ft_striteri (REVISAR PORQUE SE FUMA VALORES DEL ARRAY DE CHARS UNO SI Y UNO NO)
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_striteri.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_striteri`**: Aplica la función `f` a cada carácter de la cadena `s`,
    pasando como parámetros el índice de cada carácter dentro de `s` y la dirección del propio carácter, que puede modificarse si es necesario.
### Prototipo
- **`void ft_striteri(char *s, void (*f)(unsigned int, char*));`**:
    El prototipo de la función deberá ser el siguiente: `void ft_striteri(char *s, void (*f)(unsigned int, char*))`.
### Parametros
- **`s`**: La cadena sobre la que iterar.
- **`f`**: La función a aplicar sobre cada carácter.
### Valor de retorno
- Nada

## Ejercicio: ft_putchar_fd
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_putchar_fd.c
- **`Funciones autorizadas`**: write
### Descripcion
- **`ft_putchar_fd`**: Envía el carácter `c` al descriptor de archivo (file descriptor) especificado.
### Prototipo
- **`void ft_putchar_fd(char c, int fd);`**:
    El prototipo de la función deberá ser el siguiente: `void ft_putchar_fd(char c, int fd)`.
### Parametros
- **`c`**: El carácter a enviar.
- **`fd`**: El descriptor de archivo sobre el que escribir.
### Valor de retorno
- Nada

## Ejercicio: ft_putstr_fd
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_putstr_fd.c
- **`Funciones autorizadas`**: write
### Descripcion
- **`ft_putstr_fd`**:  Envía la cadena `s` al descriptor de archivo especificado.
### Prototipo
- **`void ft_putstr_fd(char *s, int fd);`**:
    El prototipo de la función deberá ser el siguiente: `void ft_putstr_fd(char *s, int fd)`.
### Parametros
- **`c`**: El carácter a enviar.
- **`fd`**: El descriptor de archivo sobre el que escribir.
### Valor de retorno
- Nada

## Ejercicio: ft_putendl_fd
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_putendl_fd.c
- **`Funciones autorizadas`**: write
### Descripcion
- **`ft_putendl_fd`**: Envía la cadena `s` al descriptor de archivo dado, seguido de un salto de línea.
### Prototipo
- **`void ft_putendl_fd(char *s, int fd);`**:
    El prototipo de la función deberá ser el siguiente: `void ft_putendl_fd(char *s, int fd)`.
### Parametros
- **`s`**: La cadena a enviar.
- **`fd`**: El descriptor de archivo sobre el que escribir.
### Valor de retorno
- Nada

## Ejercicio: ft_putnbr_fd
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_putnbr_fd.c
- **`Funciones autorizadas`**: write
### Descripcion
- **`ft_putnbr_fd`**: Escribe el número entero ‘n’ en el descriptor de archivo dado.
### Prototipo
- **`void ft_putnbr_fd(int n, int fd);`**:
    El prototipo de la función deberá ser el siguiente: `void ft_putnbr_fd(int n, int fd)`.
### Parametros
- **`n`**: El número entero que se envía.
- **`fd`**: El descriptor de archivo sobre el que escribir.
### Valor de retorno
- Nada

# Parte de listas de libc
## Indicaciones
- Las funciones para manejar memoria y cadenas son muy útiles, pero pronto descubrirás que trabajar con listas puede serlo aún más.
- En esta tercera parte deberás implementar funciones que utilicen una estructura para manejar listas enlazadas.
- Para ello, añade la siguiente declaración de estructura a tu archivo libft.h:
    typedef struct s_list
    {
    void *content;
    struct s_list *next;
    } t_list;
- Las variables de la estructura t_list son:
    • content: los datos contenidos en el nodo. Usar `void *` permite almacenar cualquier tipo de dato.
    • next: la dirección del siguiente nodo, o `NULL` si el nodo actual es el último de la lista.

## Ejercicio: ft_lstnew
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_lstnew.c
- **`Funciones autorizadas`**: malloc
### Descripcion
- **`ft_lstnew`**:  Reserva memoria (usando malloc(3)) y devuelve un nuevo nodo.
    La variable `content` se inicializa con el contenido del parámetro `content`.
    Mientras que la variable `next` se inicializa con `NULL`.
### Prototipo
- **`t_list *ft_lstnew(void *content);`**:
    El prototipo de la función deberá ser el siguiente: `t_list *ft_lstnew(void *content)`.
### Parametros
- **`content`**: el contenido con el que se crea el nodo.
### Valor de retorno
- Devuelve un puntero al nuevo nodo.

## Ejercicio: ft_lstadd_front
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_lstadd_front.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_lstadd_front`**: Añade el nodo `new` al principio de la lista `lst`.
### Prototipo
- **`void ft_lstadd_front(t_list **lst, t_list *new);`**:
    El prototipo de la función deberá ser el siguiente: `void ft_lstadd_front(t_list **lst, t_list *new)`.
### Parametros
- **`lst`**: La dirección de memoria de un puntero al primer nodo de una lista.
- **`new`**:: Un puntero al nodo que se añade al principio de la lista.
### Valor de retorno
- No devuelve nada

## Ejercicio: ft_lstsize
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_lstsize.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_lstsize`**: Cuenta el número de nodos de una lista.
### Prototipo
- **`int ft_lstsize(t_list *lst);`**:
    El prototipo de la función deberá ser el siguiente: `int ft_lstsize(t_list *lst)`.
### Parametros
- **`lst`**: el principio de la lista.
### Valor de retorno
- Devuelve la longitud/tamaño de la lista.

## Ejercicio: ft_lstlast
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_lstlast.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_lstlast`**: Devuelve el último nodo de la lista.
### Prototipo
- **`t_list *ft_lstlast(t_list *lst);`**:
    El prototipo de la función deberá ser el siguiente: `t_list *ft_lstlast(t_list *lst)`.
### Parametros
- **`lst`**: el principio de la lista.
### Valor de retorno
- Devuelve el último nodo de la lista.

## Ejercicio: ft_lstadd_back
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_lstadd_back.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_lstadd_back`**: Añade el nodo ‘new’ al final de la lista `lst`.
### Prototipo
- **`void ft_lstadd_back(t_list **lst, t_list *new);`**:
    El prototipo de la función deberá ser el siguiente: `void ft_lstadd_back(t_list **lst, t_list *new)`.
### Parametros
- **`lst`**: el puntero al primer nodo de una lista.
- **`new`**: el puntero a un nodo que se añade a la lista.
### Valor de retorno
- No devuelve nada

## Ejercicio: ft_lstdelone
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_lstdelone.c
- **`Funciones autorizadas`**: free
### Descripcion
- **`ft_lstdelone`**: Recibe como parámetro un nodo `lst` y libera la memoria del contenido utilizando la función `del` dada como parámetro.
    También libera el `nodo` en sí mismo, pero no libera el siguiente `nodo`.
### Prototipo
- **`void ft_lstdelone(t_list *lst, void (*del)(void*));`**:
    El prototipo de la función deberá ser el siguiente: `void ft_lstdelone(t_list *lst, void (*del)(void*))`.
### Parametros
- **`lst`**: el nodo a liberar.
- **`del`**: un puntero a la función utilizada para liberar el contenido del nodo.
### Valor de retorno
- No devuelve nada

## Ejercicio: ft_lstclear (AJUSTAR ft_list_clear EN C12 EN CASO DE SER NECESARIO. REVISAR FIRMA FUNCION ft_list_clear)
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_lstclear.c
- **`Funciones autorizadas`**: free
### Descripcion
- **`ft_lstclear`**: Elimina y libera el nodo `lst` dado y todos los consecutivos del mismo, utilizando la función `del` y `free(3)`.
    Al final, el puntero a la lista debe ser `NULL`.
### Prototipo
- **`void ft_lstclear(t_list **lst, void (*del)(void*));`**:
    El prototipo de la función deberá ser el siguiente: `void ft_lstclear(t_list **lst, void (*del)(void*))`.
### Parametros
- **`lst`**: la dirección de un puntero a un nodo.
- **`del`**: un puntero a la función utilizado para eliminar el contenido de un nodo.
### Valor de retorno
- No devuelve nada

## Ejercicio: ft_lstiter
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_lstiter.c
- **`Funciones autorizadas`**: Ninguna
### Descripcion
- **`ft_lstiter`**: Itera la lista `lst` y aplica la función `f` en el contenido de cada nodo.
### Prototipo
- **`void ft_lstiter(t_list *lst, void (*f)(void *));`**:
    El prototipo de la función deberá ser el siguiente: `void ft_lstiter(t_list *lst, void (*f)(void *))`.
### Parametros
- **`lst`**:un puntero al primer nodo.
- **`f`**: un puntero a la función que utilizará cada nodo.
### Valor de retorno
- No devuelve nada

## Ejercicio: ft_lstmap
### Indicaciones
- **`Directorio entrega`**: libft
- **`Archivos a entregrar`**: ft_lstmap.c
- **`Funciones autorizadas`**: malloc, free
### Descripcion
- **`ft_lstmap`**: Itera la lista `lst` y aplica la función `f` al contenido de cada nodo.
    Crea una lista resultante de aplicar sucesivamente la función `f` a cada nodo.
    La función `del` se utiliza para eliminar el contenido de un nodo si es necesario.
### Prototipo
- **`t_list *ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *));`**:
    El prototipo de la función deberá ser el siguiente: `t_list *ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))`.
### Parametros
- **`lst`**: un puntero a un nodo.
- **`f`**: la dirección de un puntero a una función usada en la iteración de cada elemento de la lista.
- **`del`**: un puntero a función utilizado para eliminar el contenido de un nodo, si es necesario.
### Valor de retorno
- Devuelve la nueva lista.
- Devuelve `NULL` si falla la reserva de memoria.


# Requisitos del Readme
- Debe incluirse un archivo README.md en la raíz del repositorio Git.
    Su propósito es permitir que cualquier persona que no esté familiarizada con el proyecto (pares, personal,
    responsables de selección, etc.) pueda entender rápidamente de qué trata el proyecto,
    cómo ejecutarlo y dónde encontrar más información sobre el tema.

- El README.md debe incluir, como mínimo:
    • La primera línea debe estar en cursiva y decir: Este proyecto ha sido creado como parte del currículo de 42 por <login1>[, <login2>[, <login3>[...]]].
    • Una sección de "Descripción"que presente claramente el proyecto, incluyendo su objetivo y una breve visión general.
    • Una sección de "Instrucciones"que contenga cualquier información relevante sobre compilación, instalación y/o ejecución.
    • Una sección de "Recursos"que enumere referencias clásicas relacionadas con el tema (documentación, artículos, tutoriales, etc.),
        así como una descripción del uso de IA, especificando para qué tareas y en qué partes del proyecto se ha utilizado.
- ➠ Podrían requerirse secciones adicionales dependiendo del proyecto (por ejemplo, ejemplos de uso, lista de características, decisiones técnicas, etc.).
- También debe incluirse una descripción detallada de la librería creada para este proyecto.
    La elección del idioma queda a tu criterio. Se recomienda escribir en inglés, pero no es obligatorio.