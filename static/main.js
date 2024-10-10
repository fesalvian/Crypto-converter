
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
            resultados.innerHTML += `<div class="resultado">${moeda}: ${valor.toFixed(2)} $</div>`;
        }
    })
    .catch((error) => {
        console.error('Erro:', error);
    });
}