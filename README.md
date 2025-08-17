# Urban Routes App - QA Project

Este proyecto es una aplicación diseñada para realizar pruebas de calidad (QA) y asegurar el correcto funcionamiento de un sistema relacionado con "Urban Routes", aplicación de movilidad.

![](https://i.postimg.cc/Y96XHZ22/Urban-Routes.png)

## Estructura del Proyecto

### Archivos y Directorios Principales

-   **.idea**: Archivos de configuración del IDE (por ejemplo, PyCharm).
-   **.pytest_cache**: Caché generada por pytest para mejorar el rendimiento en las pruebas.
-   **.venv**: Entorno virtual de Python que contiene las dependencias del proyecto.
-   **data.py**: Archivo que gestiona configuraciones clave del proyecto.
-   **UrbanRoutesLocators.py**: Archivo con los localizadores necesarios de la aplicación.
-   **UrbanRoutesMethods.py**: Archivo con los métodos para realizar las pruebas automatizadas solicitadas.
-   **UrbanRoutesTestcases.py**: Archivo para correr cada una de las pruebas automatizadas.
-   ****pycache****: Archivos compilados de Python generados automáticamente.

### Tecnologías Utilizadas

-   **Python**: Lenguaje de programación principal del proyecto.
-   **pytest**: Framework de pruebas utilizado para automatizar y gestionar las pruebas.
-   **Selenium**: Herramienta de código abierto utilizada para automatizar pruebas de aplicaciones web en diferentes navegadores.

### Instrucciones de Instalación

1.  Clonar el repositorio del proyecto:
    
    ` git clone git@github.com:username/qa-project-Urban-Routes-es.git`
    
2.  Navegar al directorio del proyecto:
    
    `cd qa-project-Urban-Routes-es`
    
3.  Crear un entorno virtual y activarlo:
    
    `python -m venv .venv` `source .venv/bin/activate # En Windows: venv\Scripts\activate`
    
4.  Instalar las dependencias del proyecto:
    
    `pip install pytest`
    `pip install selenium`

### Cómo Ejecutar el Proyecto

1.  Asegúrate de estar en el entorno virtual (`.venv`).
    
2.  Ejecutar las pruebas con pytest:
    
    `pytest`

3.  Modifica el archivo data.py para personalizar las pruebas según sea necesario.

### Demo

https://drive.google.com/file/d/1kupjl4r3My6xO3UG_ppHsjA13V6b5eie/view?usp=sharing

Jorge Luis Ramirez Morales
Cohort 26