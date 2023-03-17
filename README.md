# Prueba Tecnica 2

Crea un servicio que reciba como parámetro una URL y obtenga los productos de
la página. Incluir Dockerfile

## Instalación

Instalar librerias que estan dentro del archivo requirements.txt

## Uso

Una vez instalados los requerimientos, entrar al directorio en donde
se encuentra nuestro servicio en Flask 
(Scraping/Scraping/spiders/app.py)

Una vez que nos ubicamos dentro de la carpeta, ejecutar el comando:

```cmd
python app.py
```

Realizado esto, podremos observar el funcionamiento completo del Servicio
Para poder ejecutar el servicio puede ser desde un navegador o desde postman con los siguientes parametros:

- Method: "GET"
- URL: http://127.0.0.1:5000/
- Endpoint: scrape_data
- Argumento: url=<<url-necesaria>>

## Notas importantes / Observaciones
#### El servicio esta realizado para funcionar con la pagina de MercadoLibre

Algunas URL de prueba fueron:
1. https://listado.mercadolibre.com.mx/_Deal_pernod-multimarca-supermercado
2. https://autos.mercadolibre.com.mx/_PublishedToday_YES

#### Rotacion de Agentes de Usuario

Se optó por usar la libreria 

```cmd
random_user_agent
```

debido a que podemos usar diferentes tipos de
agentes de usuario que se pueden utilizar para evitar
una deteccion temprana del bot, con esta libreria
podemos seleccionar el tipo de navegador, sistema operativo
y el numero total de agentes de usuario que queremos obtener, de los cuales
solo uno de forma aleatoria se va a elegir cada que inicie un nuevo flujo.

Como nota extra, para evitar una deteccion temprana del bot o baneo,
se puede realizar una rotacion de proxys.

# Librerias utilizadas

- Scrapy
- random-user-agent
- Flask