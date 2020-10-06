from datetime import date
anoAtual = date.today().year
deMaior = 0

for i in range(0, 7):
    idade = anoAtual - int(input('Digite a data de nascimento da {}° pessoa: '.format(i + 1)))
    if idade >= 21:
        deMaior += 1

print('Destas, {} pessoas são menor de idade e {} já são de maior!'.format((deMaior - 7) * - 1, deMaior))
