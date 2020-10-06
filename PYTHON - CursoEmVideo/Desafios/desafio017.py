from math import sqrt, pow

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

hi = sqrt(pow(co, 2) + pow(ca, 2))

print('A hipotenusa resultante dos catetos é {}.'.format(hi))
