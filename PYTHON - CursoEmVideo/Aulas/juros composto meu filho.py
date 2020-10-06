parcela = float(input('Digite o preço da parcela, BB: '))
jurosComposto = float(input('Digite o juros composto: '))
tempo = float(input('Digite o numero de meses: '))

total = parcela * ((1 + jurosComposto)**2)

print('Segure a lapada: R${}'.format(total))
