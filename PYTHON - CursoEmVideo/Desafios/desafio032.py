from datetime import date

ano = int(input('Digite um ano ou digite 0 para analisar o ano atual: '))
bissexto = 'não é'

if ano == 0:
    ano = date.today().year

if (ano % 100) == 00:
    if ano % 400 == 0:
        bissexto = 'é'
else:
    if ano % 4 == 0:
        bissexto = 'é'

print('O ano de {} {} Bissexto!'.format(ano, bissexto))
