let num = [5, 9, 3, 5]

num.push(9)

num.sort()

console.log(num)

console.log(`Vetor: num\nTamanho: ${num.length}`)

let pos = num.indexOf(9)

if(pos == -1)
{
    console.log('O valor não foi encontrado')
}
else
{
    console.log(`O valor está na posição ${pos}`)
}