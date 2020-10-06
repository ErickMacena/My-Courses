function gerar()
{
    let num = document.getElementById('txtn')
    let tab = document.getElementById('seltab')

    if(num.value == '')
    {
        alert('Por favor, digite um número!')
    }
    else
    {
        let n = Number(num.value)

        //tab.innerHTML = `Digite um número acima`
        for(let c = 0; c <= 10; c++)
        {
            let item = document.createElement('option')
            item.text = `${n} x ${c} = ${n * c}`
            item.value = `tab${c}`
            tab.appendChild(item)
        }
    }
}