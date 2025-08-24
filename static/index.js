let numero1 = '';
let numero2 = '';
let operacao = '';
let isSecond = false;
const display = document.getElementById('display');
const botoes = document.querySelectorAll('button');
botoes.forEach(btn => {
    btn.addEventListener('click', () => {
    let valor = btn.innerText;
    if (!isNaN(valor) || valor === '.') {
    if (!isSecond) {
        if(numero1 != '')
        {
            if (valor === '.' && !numero1.includes('.'))
            {   
                numero1 += valor;
                display.value = numero1; 
            }else if(valor != '.')
            {
                numero1 += valor;
                display.value = numero1;
            }
        }else if(valor != '.'){
            numero1 += valor;
            display.value = numero1;
        }
    } else {
        if(numero2 != '')
        {
            if (valor === '.' && !numero2.includes('.'))
            {   
                numero2 += valor;
                display.value = numero2; 
            }else if(valor != '.')
            {
                numero2 += valor;
                display.value = numero2;
            }
        }else if(valor != '.'){
            numero2 += valor;
            display.value = numero2;
        }
    }
    } else if (['+', '−', '×', '÷'].includes(valor)) {
        if(operacao == '')
        {
            operacao = valor;
            isSecond = true;
        }
    }
        else if (valor === 'C') {
        numero1 = '';
        numero2 = '';
        operacao = '';
        isSecond = false;
        display.value = '';
    } else if (valor === '=') {
        fetch('/calcular', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            numero1: parseFloat(numero1),
            numero2: parseFloat(numero2),
            operacao: operacao
         })
        })
        .then(res => res.json())
        .then(data => {
        display.value = data.resultado;
        numero1 = data.resultado;
        numero2 = '';
        operacao = '';
        isSecond = false;
        })
        .catch(err => {
        display.value = 'Erro';
        console.error(err);
        });
    }
    });
});
