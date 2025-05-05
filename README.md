# Validador-gestor-correos
Validador y Gestor de Correos Electrónicos para Biblioteca Universitaria

## Contexto:
La biblioteca de la Universidad Tecnológica del Valle ha decidido mejorar el manejo de la comunicación con sus usuarios. Para ello, necesita una aplicación sencilla de consola que permita registrar, validar y administrar direcciones de correo electrónico de estudiantes y docentes.

## Descripción del Ejercicio:
En equipos de 2 a 3 personas, desarrollarán una aplicación de consola en Python que cumpla con los siguientes requisitos:

## 📌 Requisitos de la Aplicación:
Menú principal:

- Registrar un nuevo correo electrónico.
- Ver correos registrados.
- Buscar un correo específico.
- Salir de la aplicación.


## Registro de correos electrónicos:

- Solicitar al usuario que ingrese una dirección de correo electrónico.
- Validar la dirección usando una expresión regular sencilla.
- Clasificar automáticamente el correo como 'estudiante' o 'docente', basándose en la estructura del correo:
   • Estudiantes: terminan con "@estudiante.utv.edu.co"
   • Docentes: terminan con "@utv.edu.co"
- Almacenar los correos válidos junto con su clasificación en una colección adecuada.


## Visualización de correos registrados:

- Mostrar todos los correos registrados, indicando claramente si pertenecen a un estudiante o a un docente.


## Búsqueda de correos específicos:

- Permitir que el usuario ingrese parte o la totalidad de un correo.
- Utilizar ciclos y condicionales para buscar coincidencias dentro de la colección de correos registrados.
- Mostrar todas las coincidencias encontradas.


## 🔧 Aspectos técnicos obligatorios:
- ✅ Uso correcto de tipos de datos (strings, booleanos, etc.).
- ✅ Manejo de condicionales (if-elif-else).
- ✅ Implementación de ciclos (for o while).
- ✅ Uso de colecciones (listas o diccionarios).
- ✅ Manipulación y búsqueda de strings.
- ✅ Validación mediante expresiones regulares (regex).

## 📍 Consideraciones adicionales:
La interfaz de consola debe ser amigable y clara.
Manejar adecuadamente los errores y casos especiales (por ejemplo, correo no válido).
Documentar brevemente el código indicando claramente la función de cada sección.

## 📦 Entregable:
Código fuente de la aplicación (.py).
Una breve explicación (comentarios en el código) sobre cómo resolvieron los puntos solicitados.
