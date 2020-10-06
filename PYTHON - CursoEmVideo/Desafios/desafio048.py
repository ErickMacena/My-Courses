print('A soma entre todos os números impares, multiplos de 3 entre 1 e 500 é ', end='')

resultado = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        resultado += i

print('{}.'.format(resultado))
