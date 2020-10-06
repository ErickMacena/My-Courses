while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    i = 1
    print('-' * 30)
    while i <= 10:
        print(f'{n} x {i} = {n * i}')
        i += 1
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO, volte sempre!')