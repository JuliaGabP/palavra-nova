document.addEventListener("DOMContentLoaded", async function () {
    try {
        let response = await fetch("http://127.0.0.1:5000/palavra");
        let data = await response.json();

        document.getElementById("palavra").innerText = data.palavra;
        document.getElementById("significado").innerText = `Significado: ${data.significado}`;
        document.getElementById("exemplo").innerText = `Exemplo: "${data.exemplo}"`;
    } catch (error) {
        console.error("Erro ao buscar a palavra:", error);
    }
});
