# Web scraping
Web scraping es el proceso de usar bots para extraer contenido y datos de un sitio web.
## ¿Como funciona?

El web scraping extrae el código HTML subyacente y, con él, los datos se transforman y son almacenados en una base de datos. El ususario puede replicar todo el contenido del sitio web en otro lugar.

<img src="./web scraping.png" alt="Alt text" title="Optional title">

##  Bot: ChromeDriver

WebDriver es una herramienta de código abierto para pruebas automatizadas de aplicaciones web en muchos navegadores. Proporciona capacidades para navegar a páginas web, entrada de usuario, ejecución de JavaScript y más. ChromeDriver es un servidor independiente que implementa el estándar W3C WebDriver. ChromeDriver está disponible para Chrome en Android y Chrome en escritorio (Mac, Linux, Windows y ChromeOS).

# Algoritmo


Cada carpeta, cuyo nombre es el sitio web, contiene un script de python el cual realizará el web scraping. El script contiene una clase cuyos métodos son los encargados de la extracción y transformación de la información de los hoteles. Los datos extraídos son almacenamos en un archivo json con el nombre de cada ciudad y el sitio web posteriormente son enviados a una base de datos postgres.

Los sitios web y las ciudades son detallados a continuacion:
 
    Sitios web: Airbnb, Booking, Expedia, Tripadvisor.
    Ciudades: Guayaquil, Ambato, Ibarra, Loja, Manta y Quito.


## Comencemos

A continuación brindamos una guía que nos permitirá replicar el proyecto reduciendo la posible incompatibilidad con las versiones de las librerías de python.

### Prerequisites

Como una recomendacios utilizaremos un entorno virtual.

1. virtual env
  ```sh
  python3 -m pip install 
  ```
2. Creamos un ambiente virtual.
    ```sh
    python3 -m venv env
    ```
3. Activamos env
    ```sh
    source env/bin/activate.
    ```
4.  Instalamos los requisitos
    ```sh
    python3 -m pip install requirements.txt
    ```



## Extracion y transformacion de datos.

Cada carpeta contiene un script independiente el cual se encargará de recolectar datos del sitio web. A pesar de su independencia todos los scripts contienen los mismos métodos. Para replicar el ejercicio utilizaremos el script de Airbnb.

* El archivo airbnb.py inicia corriendo la clase 
    ```sh
    ciudades=  ['guayaquil','ambato','ibarra','loja','manta','quito']
    for ciudad in ciudades:
        Hotel_Airbnb(ciudad).ingest(ciudad+'v3')
    ```

## Carga de los datos.

Cada carpeta contiene un script independiente denominado 'exporter_...' el cual se encargará de recolectar y unir los archivos json de la carpeta base json. Los scripts unidos se almacenan en la carpeta data, finalmente los datos son cargados a una base postgres mediante el script 'top_post.py'.


