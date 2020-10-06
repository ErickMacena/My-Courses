print('=' * 30)
print('{:^30}'.format('Bem vindo'))
print('=' * 30)

valor = int(input('Qual valor você deseja sacar? R$'))
n50 = n20 = n10 = n1 = 0

if valor > 0:
    while True:
        if valor > 0:
            if valor >= 50:
                n50 += 1
                valor -= 50
            elif valor >= 20:
                n20 += 1
                valor -= 20
            elif valor >= 10:
                n10 += 1
                valor -= 10
            else:
                n1 += 1
                valor -= 1
        else:
            break

if n50 > 0:
    print(f'Total de {n50} cédulas de R$50')

if n20 > 0:
    print(f'Total de {n20} cédulas de R$20')
if n10 > 0:
    print(f'Total de {n10} cédulas de R$10')
if n1 > 0:
    print(f'Total de {n1} cédulas de R$1')


print('=' * 30)
print('{:^30}'.format('Volte Sempre'))
