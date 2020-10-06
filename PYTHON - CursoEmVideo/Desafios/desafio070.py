tGasto = mmil = i = brtP = 0
brt = ''
res = ''
while True:
    i += 1
    nome = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Digite o preço do produto: '))
    tGasto += preco

    if i == 1 or preco < brtP:
        brtP = preco
        brt = nome
    if preco > 1000:
        mmil += 1

    while True:
        res = str(input('Quer continuar? [S/N] ')).replace(' ', '')[0].upper()
        if res in 'SN':
            break

    if res == 'N':
        break

print('\033[:33m', end='')
print('-=' * 30)
print('\033[m', end='')

print(f'''Total gasto na compra: \033[:36mR${tGasto:.2f}\033[m
\033[:36m{mmil}\033[m produtos custaram mais de 1,000 R$
\033[:36m{brt} custou R${brtP:.2f}\033[m e foi o produto mais barato que você comprou!''')

print('\033[:33m', end='')
print('-=' * 30)
print('\033[m', end='')