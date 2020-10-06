n = int(input('Digite um número: '))

if n == 0 or n == 1:
    print('{} não é primo.'.format(n))
elif n == 2:
        print('2 é primo!')
else:
    ePrimo = 1
    for i in range(2, n):
        if n % i == 0:
            ePrimo = 0

    if ePrimo == 1:
        print('{} é primo!'.format(n))
    else:
        print('{} não é primo!'.format(n))