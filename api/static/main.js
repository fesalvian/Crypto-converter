
function converter() {
    const valor = document.getElementById("valor").value;
    const moeda = document.getElementById("moeda").value;

    fetch('http://127.0.0.1:5000/converter', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            valor: parseFloat(valor),
            moeda: moeda
        }),
    })
    .then(response => response.json())
    .then(data => {
        let resultados = document.getElementById("resultados");
        resultados.innerHTML = '';
        for (let [moeda, valor] of Object.entries(data)) {
            let valorFormatado = valor.toLocaleString('en-US', { style: 'currency', currency: getCurrencyCode(moeda) });
            resultados.innerHTML += `<div class="resultado">${moeda}: ${valorFormatado}</div>`;
        }
    })
    .catch((error) => {
        console.error('Erro:', error);
    });
}

// Função para mapear as moedas com seus códigos de moeda ISO
function getCurrencyCode(moeda) {
    switch(moeda) {
        case 'Real':
            return 'BRL';
        case 'Dollar':
            return 'USD';
        case 'Libra esterlina':
            return 'GBP';
        case 'Bitcoin':
            return 'BTC';
        case 'Etherum':
            return 'ETH';
        case 'BNB':
            return 'BNB';
        case 'Solana':
            return 'SOL';
        default:
            return 'USD'; // Padrão
    }
}