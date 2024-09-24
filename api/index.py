from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from translate import Translator

translator = Translator(from_lang="pt", to_lang="en")

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def index():
    return 'Hello, World!'

@app.route('/', methods=['POST'])
@cross_origin()
def home():
    data = request.get_json()

    if not data or 'texto' not in data:
        return jsonify({"error": "Dados inválidos ou incompletos"}), 400

    texto = data['texto']
    translation = translator.translate(texto)

    return jsonify({"texto": translation}), 201

# Iniciando o servidor
if __name__ == '__main__':
    app.run(debug=True)
