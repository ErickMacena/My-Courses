n = int(input('Digite um número inteiro: '))
conversao = int(input('''Qual será a conversão?
Digite 1 para \033[4:34mBinário\033[m
Digite 2 para \033[4:33mOctal\033[m
Digite 3 para \033[4:32mHexadecimal\033[m
'''))

if conversao == 1:
    print('{} em \033[4:34mbinário\033[m é igual a {}.'.format(n, bin(n)[2:]))
elif conversao == 2:
    print('{} em \033[4:33moctal\033[m é igual a {}.'.format(n, oct(n)[2:]))
else:
    print('{} em \033[4:33mhexadecimal\033[m é igual a {}.'.format(n, hex(n)[2:]))
