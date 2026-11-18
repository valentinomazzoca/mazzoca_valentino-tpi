 Sistema de Gestión de Países
 1. Descripción del proyecto

El presente proyecto consiste en el desarrollo de un sistema de gestión de países utilizando Python y archivos CSV como mecanismo de almacenamiento de información.

El programa funciona mediante un menú interactivo en consola y permite administrar información de diferentes países, incluyendo su nombre, población, superficie y continente.

El objetivo es aplicar los conceptos fundamentales de programación aprendidos en la materia Programación 1, mediante el desarrollo de una aplicación modular que permita almacenar, modificar, buscar, filtrar, ordenar y analizar información.

 2. Tecnologías utilizadas

- **Lenguaje:** Python 3.
- **Almacenamiento:** Archivos CSV.
- **Módulo CSV:** Lectura y escritura de registros.
- **Estructuras de datos:** Listas.
- **Control de flujo:** Condicionales y estructuras de repetición.
- **Organización:** Funciones y módulos independientes.

 3. Funcionalidades

El sistema cuenta con las siguientes funcionalidades:

 Gestión de países
- Agregar un país con nombre, población, superficie y continente.
- Actualizar la población y superficie de un país existente.
- Buscar países por nombre mediante coincidencias parciales o exactas.

 Filtrado
- Filtrar países por continente
- - Filtrar países por rango de población.
- Filtrar países por rango de superficie.

 Ordenamiento
- Ordenar países alfabéticamente por nombre.
- Ordenar por población de manera ascendente y descendente.
- Ordenar por superficie de manera ascendente y descendente.

 Estadísticas
- Identificar el país con mayor población.
- Identificar el país con menor población.
- Calcular el promedio de población.
- Calcular el promedio de superficie.
- Obtener la cantidad de países registrados por continente.

 Validaciones
- Controlar campos obligatorios al agregar y modificar países.
- Validar el formato de los registros del archivo CSV.
- Controlar entradas incorrectas en los filtros.
- Informar cuando una búsqueda o filtro no devuelve resultados.

4. Estructura del proyecto

```text
Sistema-Gestion-Paises/
│
├── main_menu_tpi.py
├── agregar_pais.py
├── busqueda_nombre.py
├── filtrar_tpi.py
├── ordenar_tpi.py
├── estadisticas_tpi.py
├── validaciones.py
├── paises_70.csv
└── README.md
```

 Descripción de los archivos

- `main_menu_tpi.py`: contiene el menú principal y conecta las funcionalidades.
- `agregar_pais.py`: permite agregar y modificar países.
- `busqueda_nombre.py`: contiene la función de búsqueda por nombre.
- `filtrar_tpi.py`: contiene los filtros disponibles.
- `ordenar_tpi.py`: contiene los diferentes criterios de ordenamiento.
- `estadisticas_tpi.py`: realiza los cálculos estadísticos.
- `validaciones.py`: contiene las validaciones del formato de los registros CSV.
- `paises_70.csv`: almacena la información de los países.
- `README.md`: documentación del proyecto.
 5. Requisitos e instalación

Para ejecutar el programa se necesita:

- Tener instalado Python 3.10 o superior.
- Descargar o clonar el repositorio.
- Contar con todos los archivos del proyecto dentro de la misma carpeta.

 Descargar el proyecto

Desde una terminal, ejecutar:

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta del proyecto:

```bash
cd Sistema-Gestion-Paises
```

 Ejecutar el programa

Ejecutar el siguiente comando:

```bash
python main_menu_tpi.py
```

En algunos sistemas puede ser necesario utilizar:

```bash
python3 main_menu_tpi.py
```

 6. Ejemplos de uso

 Ejemplo 1: Agregar un país

**Entrada:**

```text
Nombre: Uruguay
Población: 3426260
Superficie: 176215
Continente: America
```

**Salida esperada:**

```text
Pais agregado correctamente
```

 Ejemplo 2: Buscar un país

**Entrada:**

```text
Ingrese el nombre del país que desea buscar: arg
```

**Salida esperada:**

```text
Nombre: Argentina
Población: 45376763
Superficie: 2780400
Continente: America
```

### Ejemplo 3: Filtrar por continente

**Entrada:**

```text
Ingrese el continente: America
```

**Salida esperada:**

```text
Argentina
Brasil
Chile
Uruguay
...
```

### Ejemplo 4: Filtrar por rango de población

**Entrada:**

```text
Población mínima: 10000000
Población máxima: 50000000
```

**Salida esperada:**

```text
Se muestran los países cuya población se encuentra dentro del rango ingresado.
```

### Ejemplo 5: Mostrar estadísticas

**Salida esperada:**

```text
===== ESTADÍSTICAS =====

País con mayor población: [Resultado calculado]
País con menor población: [Resultado calculado]
Promedio de población: [Resultado calculado]
Promedio de superficie: [Resultado calculado]

Cantidad de países por continente:
América: [Cantidad]
Europa: [Cantidad]
Asia: [Cantidad]
África: [Cantidad]
Oceanía: [Cantidad]
Europa/Asia: [Cantidad]
```

*Los resultados exactos dependen de los registros actuales del archivo CSV.*

## 7. Almacenamiento de información

Los datos se almacenan en el archivo `paises_70.csv`, utilizando el formato CSV.

La estructura del archivo contiene los siguientes campos:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Japon,125800000,377975,Asia
Brasil,213993437,8515767,America
```

El archivo permite conservar los registros y mantener la información entre diferentes ejecuciones del programa.

## 8. Participación de los integrantes

**Integrante único:**

- Valentino Mazzoca.

Responsable del análisis del problema, diseño, desarrollo, implementación de funcionalidades, validaciones, pruebas y documentación del sistema.

## 9. Información académica

- **Institución:** Universidad Tecnológica Nacional – Facultad Regional Mendoza.
- **Carrera:** Tecnicatura Universitaria en Programación.
- **Materia:** Programación 1.
- **Proyecto:** Sistema de Gestión de Países.
- **Estudiante:** Valentino Mazzoca.
