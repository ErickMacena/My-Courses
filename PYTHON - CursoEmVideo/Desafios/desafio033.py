n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux
    if n2 > n3:
        aux = n2
        n2 = n3
        n3 = aux
    if n1 > n2:
        aux = n1
        n1 = n2
        n2 = aux
if n2 > n3:
    aux = n2
    n2 = n3
    n3 = aux
    if n1 > n2:
        aux = n1
        n1 = n2
        n2 = aux

print('O Menor número é {} e o Maior é {}!'.format(n1, n3))
