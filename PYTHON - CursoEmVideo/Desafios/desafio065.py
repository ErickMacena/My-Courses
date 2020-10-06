n = int(input('Digite um número: '))
maior = n
menor = n
i = 1
media = n
res = input('Quer continuar [S/N]? ').upper()
while res == 'S':
    n = int(input('Digite um número: '))
    i += 1
    if maior < n:
        maior = n
    elif menor > n:
        menor = n
    media += n
    res = input('Quer continuar [S/N]? ').upper()

media = media / i

print('\033[:33m' + '-=' * 20 + '\033[m')
print('\033[:33m' + '-=' * 20 + '\033[m')

print('''\033[:30mMédia dos {} valores: {}
Maior valor: {}
Menor valor: {}\033[m'''.format(i, media, maior, menor))

print('\033[:33m' + '-=' * 20 + '\033[m')
print('\033[:33m' + '-=' * 20 + '\033[m')
