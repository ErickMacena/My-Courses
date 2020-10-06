n = int(input('Digite um número: '))
r = int(input('Digite uma razão de PA: '))
decimo = n + ((10 - 1) * r)
for i in range(n, decimo + r, r):
    print('{} '.format(i), end='-> ')
