pesos = [0, 0, 0, 0, 0, 0, 0]

for i in range(0, 7):
    pesos[i] = int(input('Digite o peso da {}° pessoa: '.format(i + 1)))

maior = pesos[0]
menor = pesos[5]

for i in range(0, 7):
    if pesos[i] > maior:
        maior = pesos[i]
    if pesos[i] < menor:
        menor = pesos[i]

print('O maior peso peso entre estes for {} e o menor foi {}.'.format(maior, menor))
