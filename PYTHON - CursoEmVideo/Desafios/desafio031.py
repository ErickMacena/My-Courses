d = float(input('Digite a distância da viagem em Km: '))

if d > 200:
    passagem = 0.45
else:
    passagem = 0.50

print('O preço da passagem é {:.2f}'.format(d * passagem))
