# Web scraping
Wed scraping es el proceso de usar bots para extraer contenido y datos de un sitio web.
## ¿Como funciona?

El web scraping extrae el código HTML subyacente y, con él, los datos se transforman y son almacenados en una base de datos. El ususario puede replicar todo el contenido del sitio web en otro lugar.

<img src="./web scraping.png" alt="Alt text" title="Optional title">

##  Bot: ChromeDriver

WebDriver es una herramienta de código abierto para pruebas automatizadas de aplicaciones web en muchos navegadores. Proporciona capacidades para navegar a páginas web, entrada de usuario, ejecución de JavaScript y más. ChromeDriver es un servidor independiente que implementa el estándar W3C WebDriver. ChromeDriver está disponible para Chrome en Android y Chrome en escritorio (Mac, Linux, Windows y ChromeOS).

# Algoritmo


Cada carpeta, cuyo nombre es el sitio web, contine un scrip de python el cual realizara el web scraping. El scrip contiene una clase cuyos metodos son los encargados de la extracion y tranformacion de la informacion de los hoteles. Los datos extraidos son almacenamos en un archivo json con el nombre de cada ciudad y el sitio web posteriormente son enviados a una base de datos postgres. 

Los sitios web y las ciudades son detallados a continuacion:
 
    Sitios web: Airbnb, Booking, Expedia, Tripadvisor.
    Ciudades: Guayaquil, Ambato, Ibarra, Loja, Manta y Quito.


## Comencemos

A continuacion brindamos una guia que nos permitira replicar el proyecto reduciendo la posible incopatibilidad con las verciones de las libretias de python.

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

Cada carpeta contiene un scrip independiende el cual se encargara de recolectar datos des sitio web. A persar de su indepencia todos los scrips contienen los mismos metodos. Para replicar el ejercicio utilizaremos es script de Airbnb.

* El archivo airbnb.py inicia corriendo la clase 
    ```sh
    ciudades=  ['guayaquil','ambato','ibarra','loja','manta','quito']
    for ciudad in ciudades:
        Hotel_Airbnb(ciudad).ingest(ciudad+'v3')
    ```

## Carga de los datos.

Cada carpeta contiene un scrip independiende denominado 'exporter_...' el cual se encargara de recolectar y unir los archivos json de la carpeta basejon. Los scrips unidos se almacenan en la capeta data, finalmente los datos son cargados a una base postgres mediante el scrip 'top_post.py'.



