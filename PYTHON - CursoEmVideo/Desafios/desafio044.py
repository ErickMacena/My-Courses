print('{:-^40}'.format(' LOJAS TILIBRAS '))

preco = float(input('Qual é o preço do produto? R$ '))

pagamento = int(input('''Qual será a forma de pagamento?
Digite \033[4:36m1\033[m para \033[4:36mÁ vista no dinheiro/cheque\033[m
Digite \033[4:31m2\033[m para \033[4:31mÀ vista no Cartão\033[m
Digite \033[4:33m3\033[m para \033[4:33mAté 2x no Cartão\033[m
Digite \033[4:35m4\033[m para \033[4:35m3x ou mais no Cartão\033[m
'''))

porcentagem = 1

if pagamento == 1:
    porcentagem = 0.9
elif pagamento == 2:
    porcentagem = 0.95
elif pagamento == 3:
    porcentagem = 1
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format((preco * porcentagem) / 2))
elif pagamento == 4:
    porcentagem = 1.2
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, (preco * porcentagem) / parcelas))
else:
    porcentagem = 0
    print('OPÇÃO INVALIDA DE PAGAMENTO. TENTE NOVAMENTE!')

print('O valor total será R${:.2f}.'.format(preco * porcentagem))
