nomes = ['', '', '', '']
idades = [0, 0, 0, 0]
sexo = ['', '', '', '']
media = 0
velhoN = ''
velhoI = 0
novas = 0
totIdades = 0

for i in range(0, 4):
    nomes[i] = input('Digite o nome da {}° pessoa: '.format(i + 1))
    idades[i] = int(input('Digite a idade da {}° pessoa: '.format(i + 1)))
    sexo[i] = input('Digite o sexo da {}° pessoa: '.format(i + 1))

for i in range(0, 4):
    totIdades += idades[i]
    if sexo == 'f':
        if idades[i] < 20:
            novas += 1
    else:
        if idades[i] > velhoI:
            velhoI = idades[i]
            velhoN = nomes[i]

print('A média de idade do grupo é {}'.format(totIdades / 4))
if velhoN != '':
    print('O nome do homem mais velho é {}'.format(velhoN))
else:
    print('Não teve nenhum homem na lista')

if novas > 0:
    print('{} mulheres ja são maiores de idade'.format(novas))
else:
    print('Nenhuma das mulheres é maior de idade')
