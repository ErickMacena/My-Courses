from random import randint

pc = randint(0, 10)
vezes = 1
user = int(input('Você consegue descobrir que número de 0 a 10 que o computador pensou? '))

while user != pc:
    if user > pc:
        iaiPo = 'Menos'
    else:
        iaiPo = 'Mais'
    vezes += 1
    user = int(input('{}, tenta de novo: '.format(iaiPo)))

print('Boa, você venceu na {}° tentativa!'.format(vezes))
