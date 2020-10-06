v = float(input('Digite a velocidade do carro em Km/h: '))

if v > 80:
    print('''==== Se fodeu ====
============
==== Desembolse R${:.2f} ===='''.format((v - 80) * 7.0))
else:
    print('==== Tudo certo, patrão ====')
