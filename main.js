function adicionar(valor) {
    document.getElementById('tela').value += valor;
}

function limpar() {
    document.getElementById('tela').value = '';
}

function apagar() {
    let tela = document.getElementById('tela');
    tela.value = tela.value.slice(0, -1);
}

function calcular() {
    let tela = document.getElementById('tela');
    try {
        tela.value = eval(tela.value) || '';
    } catch {
        tela.value = 'Erro';
        setTimeout(() => tela.value = '', 1500);
    }
}