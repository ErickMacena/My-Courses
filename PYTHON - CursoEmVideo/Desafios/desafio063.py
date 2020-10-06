n = int(input('Quantos elementos da Sequência de Fibonacci você quer ver? '))

if n == 1:
    print(0)
elif n == 2:
    print('0 -> 1')
else:
    p1 = 0
    p2 = 1

    i = 3
    print('0 -> 1 ', end='')
    while i <= n:
        p3 = p1 + p2
        print('-> {} '.format(p3), end='')
        p1 = p2
        p2 = p3
        i += 1
    print()

print('\033[:33mEspero que tenha gostado :)\033[m')