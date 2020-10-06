from datetime import date

anoAtual = date.today().year

idade = anoAtual - int(input('Digite seu ano de Nascimento: '))

print('O atleta tem {} anos. Classificação:'.format(idade))

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
