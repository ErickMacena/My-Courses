n = int(input('Digite um número [999 para]: '))
i = 0
s = 0

while n != 999:
    i += 1
    s += n
    n = int(input('Digite outro número [999 para]: '))
plural = 's' if i > 1 else ''
print('A soma do{} {} número{} que você digitou é {}'.format(plural, i, plural, s))
