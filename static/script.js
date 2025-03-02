document.addEventListener("DOMContentLoaded", function () {
    const palavraContainer = document.querySelector(".container");
    palavraContainer.style.opacity = 0;
    
    setTimeout(() => {
        palavraContainer.style.transition = "opacity 1.5s ease-in-out";
        palavraContainer.style.opacity = 1;
    }, 500);

    const botao = document.getElementById("nova-palavra");

    if (botao) {
        botao.addEventListener("click", function () {
            fetch("/nova-palavra")
                .then(response => response.json())
                .then(data => {
                    document.getElementById("palavra").innerText = data.palavra;
                    document.getElementById("significado").innerText = `Significado: ${data.significado}`;
                    document.getElementById("exemplo").innerText = `Exemplo: ${data.exemplo}`;
                });
        });
    }
});
