import emoji
from random import randint
from time import sleep

items = ['Pedra', 'Papel', 'Tesoura']

pessoa = int(input(emoji.emojize('''Vamos jogar pedra papel tesoura!
O que você escolhe?
:white_circle: PEDRA = \033[1:37m0\033[m
:page_facing_up: PAPEL = \033[1:30m1\033[m
:scissors: TESOURA = \033[1:31m2\033[m
O que você escolhe? ''')))

computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

print('-=' * 10)
print('Computador jogou {}.'.format(items[computador]))
print('Jogador jogou {}.'.format(items[pessoa]))
print('-=' * 10)

if pessoa == 0:
    if computador == 0:
        resultado = 2
    elif computador == 1:
        resultado = 1
    else:
        resultado = 0
elif pessoa == 1:
    if computador == 0:
        resultado = 0
    elif computador == 1:
        resultado = 2
    else:
        resultado = 1
else:
    if computador == 0:
        resultado = 1
    elif computador == 1:
        resultado = 0
    else:
        resultado = 2

if resultado == 0:
    print('PARABÉNS! Tu ganhou, mizera :v')
elif resultado == 1:
    print('EITA BIXO! Perdeste')
else:
    print('Empate, danada!')
