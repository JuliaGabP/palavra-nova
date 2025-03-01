from flask import Flask, jsonify
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)

def get_palavra_rara():
    try:
        response = requests.get("https://api.datamuse.com/words?sp=?&max=1&md=d&v=enwiki")
        words = response.json()

        if words:
            word = words[0]['word']
            meaning = words[0].get('defs', ["Sem definição disponível."])[0].split('\t')[-1]
            return {"palavra": word, "significado": meaning, "exemplo": "Exemplo não disponível."}
        else:
            return {"error": "Nenhuma palavra encontrada."}
    except Exception as e:
        return {"error": str(e)}

@app.route('/palavra', methods=['GET'])
def palavra():
    return jsonify(get_palavra_rara())

if __name__ == '__main__':
    app.run(debug=True)
