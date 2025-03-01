from flask import Flask, jsonify
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Função para obter uma palavra aleatória
def get_palavra_do_dia():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
        word = response.json()[0]

        # Buscar definição e exemplo na Dictionary API
        dict_response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        dict_data = dict_response.json()

        if isinstance(dict_data, list):
            meaning = dict_data[0]['meanings'][0]['definitions'][0]['definition']
            example = dict_data[0]['meanings'][0]['definitions'][0].get('example', "Sem exemplo disponível.")
        else:
            meaning, example = "Definição não encontrada.", "Exemplo não disponível."

        return {"palavra": word, "significado": meaning, "exemplo": example}
    except Exception as e:
        return {"error": str(e)}

@app.route('/palavra', methods=['GET'])
def palavra():
    return jsonify(get_palavra_do_dia())

if __name__ == '__main__':
    app.run(debug=True)
