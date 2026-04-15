from flask import Flask
import logging
import os

app = Flask(__name__)

# Configurar donde se guardan los mensajes (Logs)
logging.basicConfig(filename='/app/logs/app.log', level=logging.INFO)

@app.route('/')
def hola():
    logging.info("El usuario visito la pagina principal")
    return "Hola! El Tracker de Criptos esta funcionando."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
