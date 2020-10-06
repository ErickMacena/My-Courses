n = int(input('Digite um número: '))
r = int(input('Digite uma razão de PA: '))
i = 0
print('{} '.format(n), end='')
while i < 10:
    n += r
    print('-> {} '.format(n), end='')
    i += 1
