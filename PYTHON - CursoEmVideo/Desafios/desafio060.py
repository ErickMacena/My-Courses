n = int(input('Digite um número para saber seu fatorial: '))
res = n

print('{}! = {}'.format(n, n), end='')

while n > 1:
    n = n - 1
    res *= n
    print(' x {}'.format(n), end='')
if res > 1:
    print(' = {}'.format(res))
