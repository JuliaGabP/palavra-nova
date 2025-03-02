from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Função para obter uma palavra aleatória da API
def obter_palavra_api():
    try:
        # Buscar uma palavra aleatória
        resposta = requests.get("https://api.dicionario-aberto.net/random")
        if resposta.status_code != 200:
            return {"palavra": "Erro", "significado": "Não foi possível obter uma palavra."}

        dados = resposta.json()
        palavra = dados.get('word', 'Desconhecido')

        # Buscar definição da palavra
        resposta_def = requests.get(f"https://api.dicionario-aberto.net/word/{palavra}")
        if resposta_def.status_code == 200:
            definicoes = resposta_def.json()

            if definicoes and 'xml' in definicoes[0]:  # Extrair significado do XML
                from xml.etree import ElementTree as ET
                xml_content = definicoes[0]['xml']
                root = ET.fromstring(xml_content)
                significado = root.find(".//def").text if root.find(".//def") is not None else "Significado não encontrado."
            else:
                significado = "Significado não encontrado."

        else:
            significado = "Sem definição disponível."

        return {
            "palavra": palavra.capitalize(),
            "significado": significado.strip().replace("\n", " ")
        }

    except Exception as e:
        return {"palavra": "Erro", "significado": f"Erro na API: {str(e)}"}

@app.route('/')
def index():
    palavra_do_dia = obter_palavra_api()
    return render_template('index.html', palavra=palavra_do_dia)

@app.route('/nova-palavra')
def nova_palavra():
    palavra_aleatoria = obter_palavra_api()
    return jsonify(palavra_aleatoria)

if __name__ == '__main__':
    app.run(debug=True)
