let num = document.getElementById('txtnum')
let lista = document.getElementById('oplist')
let resposta = document.getElementById('res')
let numeros = []

function adicionar()
{
    resposta.innerHTML = ''

    if(num.value < 1 || num.value > 100)
    {
        alert('Digite um número entre 1 e 100, por favor!')

        return;
    }
    
    if(numeros.indexOf(num.value) != -1)
    {
        alert('O número digitado já está na lista!')

        return;
    }

    numeros.push(num.value)

    let item = document.createElement('option')
    
    item.text = `Valor ${num.value} adicionado`
    item.value = num.value

    lista.appendChild(item)

    num.value = ''
    num.focus()
}

function analisar()
{
    if(numeros.length == 0)
    {
        alert('Adicione valres à lista, por favor!')
    }
    else
    {
        var maior = 0
        var menor = numeros[0]
        var soma = 0
        var media = 0
    
        for(i in numeros)
        {
            if(numeros[i] > maior)
            {
                maior = numeros[i]
            }
        }
    
        for(i in numeros)
        {
            if(numeros[i] < menor)
            {
                menor = numeros[i]
            }
        }
    
        for(i in numeros)
        {
            soma += Number(numeros[i])
        }
    
        media = soma / numeros.length
    
        resposta.innerHTML = ''
    
        resposta.innerHTML = `Ao todo, temos ${numeros.length} números cadastrados.`
    
        resposta.innerHTML += `<br><br>O maior valor informado foi ${maior}.`
    
        resposta.innerHTML += `<br><br>O menor valor informado foi ${menor}.`
    
        resposta.innerHTML += `<br><br>Somando todos os valores, temos ${soma}.`
    
        resposta.innerHTML += `<br><br>A média dos valores digitados é ${media}.`
    }
}