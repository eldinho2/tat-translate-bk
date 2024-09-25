from flask import Flask, request, jsonify, make_response
from translate import Translator


app = Flask(__name__)

# Rota para GET
@app.route('/', methods=['GET'])
def index():
    response = make_response('Hello, World!')
    response.headers.add("Access-Control-Allow-Origin", "*")  # Permitir todas as origens
    return response

# Rota para POST
@app.route('/', methods=['POST'])
def home():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "No data provided"}), 400
    
    if 'text' not in data:
        return jsonify({"error": "No 'text' provided"}), 400
    
    if 'languageInput' not in data:
        return jsonify({"error": "No 'languageInput' provided"}), 400
    
    if 'languageOutput' not in data:
        return jsonify({"error": "No 'languageOutput' provided"}), 400
    

    text = data['text']
    languageInput = data['languageInput']
    languageOutput = data['languageOutput']

    translator = Translator(from_lang=languageInput, to_lang=languageOutput)
    translation = translator.translate(text)

    response = jsonify({"text": translation})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 201

# Rota para OPTIONS (preflight)
@app.route('/', methods=['OPTIONS'])
def options():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    return response, 200

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
