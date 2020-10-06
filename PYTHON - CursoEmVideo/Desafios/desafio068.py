from random import randint

print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 30)
i = 0
while True:
    jN = int(input('Digite um valor: '))
    jE = input('Par ou Ímpar? [P/I] ').replace(' ', '')[0].upper()

    pcN = randint(0, 10)
    soma = jN + pcN
    res = 'PAR' if soma % 2 == 0 else 'IMPAR'

    print('-' * 30)
    print(f'Você jogou {jN} e o computador {pcN}. Total de {soma} deu {res}')
    print('-' * 30)

    if res == 'IMPAR' and jE == 'P' or res == 'PAR' and jE == 'I':
        break


    print('Você VENCEU!')
    print('Vamos jogar novamente...')

    i += 1
print(f'GAME OVER! Você venceu {i} vezes.')
