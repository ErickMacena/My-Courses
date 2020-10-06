let valores = [8, 1, 1, 4 ,2, 9]

valores.sort()

let i = 4

for(let i = 0; i < valores.length; i++)
{
    console.log(`Posição ${i}, Valor: ${valores[i]}`)
}

console.log('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

for(i in valores)
{
    console.log(`Posição ${i}, Valor: ${valores[i]}`)
}

console.log(`i = ${i}`)

console.log(`Cadê o 1?\nAqui está: ${valores.indexOf(165465654)}`)