from flask import Flask, request, jsonify, make_response
from translate import Translator

translator = Translator(from_lang="pt", to_lang="en")

app = Flask(__name__)

# Rota principal com GET
@app.route('/', methods=['GET'])
def index():
    response = make_response('Hello, World!')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# Rota principal com POST
@app.route('/', methods=['POST'])
def home():
    data = request.get_json()

    if not data or 'texto' not in data:
        response = jsonify({"error": "Dados inválidos ou incompletos"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 400

    texto = data['texto']
    translation = translator.translate(texto)

    response = jsonify({"texto": translation})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 201

# Handler para o método OPTIONS (preflight)
@app.route('/', methods=['OPTIONS'])
def options():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    return response

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
