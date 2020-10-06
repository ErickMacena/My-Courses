from random import randint

num = randint(0, 5)

user = int(input('Você consegue descobrir que número de 0 a 5 que o computador pensou? '))

if user == num:
    print('Boa, você venceu!')
else:
    print('Errooooow. Era {} :v'.format(num))
