from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/precio')
def get_precio():
    return jsonify({"moneda": "Bitcoin", "precio": 65000})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
