print('Digite 6 números inteiros para saber a soma dos que forem pares!')

res = 0

for i in range(0, 6):
    n = int(input('Digite o {}° número: '.format(i + 1)))
    if n % 2 == 0:
        res += n
print('O resultado é: {}'.format(res))
