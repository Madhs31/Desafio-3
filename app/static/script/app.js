window.onload = function() {
  const texto = document.getElementById('texto');

  // Mostra o texto após 5 segundos
  setTimeout(function() {
      texto.style.display = 'block';
  }, 10000);
}

// Captura o elemento div que contém os inputs de rating
const ratingDiv = document.querySelector('.rating');
  
// Adiciona um evento de clique para detectar quando um input é selecionado
ratingDiv.addEventListener('click', function(event) {
    // Verifica se o elemento clicado é um input do tipo radio
    if (event.target.tagName === 'INPUT' && event.target.type === 'radio') {
        // Obtém o valor do input selecionado
        const valorSelecionado = event.target.value;

        // Exibe o valor selecionado (apenas para verificar)
        console.log('Valor selecionado:', valorSelecionado);

        // Aqui você pode enviar o valorSelecionado para onde precisar (por exemplo, enviar para um formulário)
    }
});
