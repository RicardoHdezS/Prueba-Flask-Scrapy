from flask import Flask, request, jsonify
import json
import subprocess


app = Flask(__name__)


@app.route('/scrape_data')
def scrapy():  # put application's code here
    url = request.args.get('url')
    if not url:
        return 'Error: se requiere una URL'

    # Ejecutamos proceso directo desde CMD
    command = f'scrapy crawl get_products -a start_urls="{url}"'
    output = subprocess.check_output(command, shell=True)

    # Convertimos la salida de informacion dentro del Scraper
    output = json.loads(output)

    # Retornamo la respuesta
    return jsonify(output)


if __name__ == '__main__':
    app.run()
