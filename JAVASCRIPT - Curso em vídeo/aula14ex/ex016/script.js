function contagem()
{
    var vI = document.getElementById('inicio')
    var vF = document.getElementById('fim')
    var vP = document.getElementById('passo')
    var ok = 1

    console.log(`1: ${vI.value}<br>2: ${vF.value}<br>3: ${vP.value}`)

    if(vI.value == '')
    {
        alert('Insira o valor de INICIO, por favor!')
        ok = 0
    }
    else if(vF.value == '')
    {
        alert('Insira o valor FINAL, por favor!')
        ok = 0
    }
    else if(vP.value == '')
    {
        alert('Insira o valor para PASSO. Considerando passo = 1...')
        vP.value = 1
    }

    if(ok == 1)
    {
        var res = document.getElementById('resultado')
        var i = Number(vI.value)
        var f = Number(vF.value)
        var p = Number(vP.value)

        res.innerHTML = `Contando:<br>${vI.value}`

        if(i < f)
        {   
            

            alert(`PASSO INVALIDO! Considerando Passo = ${p}...`)
        }
        else if(i > f)
        {
            if(p == 0)
            {
                p = -1
            }
            else
            {
                p = -p
            }

            alert(`PASSO INVALIDO! Considerando Passo = ${p}...`)
        }

        while(i + p <= f)
        {
            res.innerHTML += ` \u{1F449} ${i}`
        }

        res.innerHTML += ` \u{1f3c1}`
    }
}