from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

def obter_taxas():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,binancecoin,solana",
        "vs_currencies": "usd,brl,gbp"
    }
    resposta = requests.get(url, params=params)
    return resposta.json()

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/converter', methods=['POST'])
def converter():
    data = request.json
    valor = data['valor']
    moeda_origem = data['moeda']

    taxas = obter_taxas()
    taxas_conversao = {
        'usd_brl': taxas['bitcoin']['brl'] / taxas['bitcoin']['usd'],
        'usd_gbp': taxas['bitcoin']['gbp'] / taxas['bitcoin']['usd'],
        'usd_btc': 1 / taxas['bitcoin']['usd'],
        'usd_eth': 1 / taxas['ethereum']['usd'],
        'usd_bnb': 1 / taxas['binancecoin']['usd'],
        'usd_solana': 1 / taxas['solana']['usd']
    }

    if moeda_origem == "real":
        valor_usd = valor / taxas_conversao['usd_brl']
    elif moeda_origem == "dollar":
        valor_usd = valor
    elif moeda_origem == "libra":
        valor_usd = valor / taxas_conversao['usd_gbp']
    elif moeda_origem == "bitcoin":
        valor_usd = valor * taxas_conversao['usd_btc']
    elif moeda_origem == "ethereum":
        valor_usd = valor * taxas_conversao['usd_eth']
    elif moeda_origem == "bnb":
        valor_usd = valor * taxas_conversao['usd_bnb']
    elif moeda_origem == "solana":
        valor_usd = valor * taxas_conversao['usd_solana']

    valores_convertidos = {
        "Real": valor_usd * taxas_conversao['usd_brl'],
        "Dollar": valor_usd,
        "Libra": valor_usd * taxas_conversao['usd_gbp'],
        "Bitcoin": valor_usd / taxas_conversao['usd_btc'],
        "Ethereum": valor_usd / taxas_conversao['usd_eth'],
        "BNB": valor_usd / taxas_conversao['usd_bnb'],
        "Solana": valor_usd / taxas_conversao['usd_solana']
    }

    return jsonify(valores_convertidos)

if __name__ == '__main__':
    app.run(debug=True)
