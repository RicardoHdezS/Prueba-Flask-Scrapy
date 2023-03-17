import scrapy
from scrapy.utils.project import get_project_settings
from logging import critical, info
import json

class GetProductsSpider(scrapy.Spider):
    name = "get_products"
    item = {}

    # Obtenemos el parametro desde la peticion en Flask para detectar la URL a extraer
    def __init__(self, start_urls=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = start_urls

    def start_requests(self):
        # Headers necesarios para la peticion
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-User': '?1'
        }

        # Enviamos el flujo a fase 2
        yield scrapy.Request(url=self.start_urls, headers=headers, callback=self.parse)

    def parse(self, response):
        # Extrae los datos de la página web y devuelve un diccionario de ítems
        if response.status == 200:
            self.item['url'] = self.start_urls
            products = []

            # Cond datos en un XPATH obtenemos el contenedor de los datos y sus derivados
            container_product = response.xpath('//div[@class="ui-search-result__content-wrapper shops__result-content-wrapper"]')

            for container in container_product:
                pricing_str = container.xpath('.//div[@class="ui-search-price__second-line shops__price-second-line"]//span[@class="price-tag-fraction"]//text()').get()
                product_name = container.xpath('.//h2[contains(@class, "__title")]/text()').get()
                by = container.xpath('.//p[contains(@class, "search-official-store-label")]/text()').get()

                # Formulamos estructura de datos para agregarlos a la listra principal
                products.append({
                    "coin_type" : "MX",
                    "price_str" : f"$ {pricing_str}",
                    "name" : product_name,
                    "seller" : by
                })

            self.item['products'] = products

            # Imrpimimos resultado final
            print(json.dumps(self.item))
