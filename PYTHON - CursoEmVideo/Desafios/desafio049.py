n = int(input('Digite um número para saber sua tabuada: '))
print('A tabuada de {} é:'.format(n))

for i in range(0, 10):
    print('{:1} X {:2} = {}'.format(n, i, n * i))
