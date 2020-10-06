n = int(input('Digite um número: '))
r = int(input('Digite uma razão de PA: '))

t = int(input('Quantos termos dessa progressão você quer ver? '))
tot = t
while t > 0:
    i = 0
    print('{} '.format(n), end='')
    while i < t:
        n += r
        i += 1
        print('-> {} '.format(n), end='')

    print()
    t = int(input('Quantos termos dessa progressão você quer ver mais? '))
    tot += t
print('{} termos foram mostrados!'.format(tot))
print('É isso :)')
