from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simulación de un endpoint que retorna el consumo del usuario
@app.route('/api/consumo', methods=['GET'])
def get_consumo():
    data = [
        {
            'nombre': 'Usuario 1',
            'saldo': 150.75,
            'consumoDatos': '2GB',
            'consumoMinutos': 120
        },
        {
            'nombre': 'Usuario 2',
            'saldo': 50.00,
            'consumoDatos': '500MB',
            'consumoMinutos': 45
        },        
        {
            'nombre': 'Usuario 3',
            'saldo': 70.00,
            'consumoDatos': '200MB',
            'consumoMinutos': 40
        },
        {
            'nombre': 'Usuario 4',
            'saldo': 80.00,
            'consumoDatos': '800MB',
            'consumoMinutos': 25
        },
        {
            'nombre': 'Usuario 5',
            'saldo': 60.00,
            'consumoDatos': '200MB',
            'consumoMinutos': 15
        },
    ]
    return jsonify(data)

@app.route('/')
def index():
    return "Hola jerry"

if __name__ == '__main__':
    app.run(debug=True)
