from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)
# Permitimos CORS para que el Frontend (puerto 80) pueda hablar con este Backend (8080)
CORS(app)

# Configuración de MongoDB
# 'mongodb' es el nombre del servicio en tu docker-compose.yml
client = MongoClient('mongodb://mongodb:27017/')
db = client.crypto_db
collection = db.precios

@app.route('/precio', methods=['GET'])
def get_precio():
    try:
        # 1. Definimos el dato (Simulando una consulta a una API)
        precio_actual = 65000.50 
        nueva_consulta = {
            "moneda": "Bitcoin",
            "precio": precio_actual,
            "timestamp": datetime.now(),
            "status": "success"
        }

        # 2. GUARDADO AUTOMÁTICO: Insertamos el registro en la base de datos
        collection.insert_one(nueva_consulta)

        # 3. Limpiamos el ID de Mongo para que no de error al enviar el JSON
        nueva_consulta.pop('_id')

        return jsonify(nueva_consulta), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Escuchamos en el puerto 8080 que es el que abrimos en AWS
    app.run(host='0.0.0.0', port=8080)
