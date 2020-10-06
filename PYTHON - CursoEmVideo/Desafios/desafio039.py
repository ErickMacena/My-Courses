from datetime import date
anoAtual = date.today().year
idade = anoAtual - int(input('Digite seu ano de nascimento: '))

if idade < 18:
    print('Ainda não está na hora de se alistar, faltam {} anos!!'.format(18 - idade))
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    print('Ja passou da hora de se alistar! Você está {} anos atrasado!'.format(idade - 18))
