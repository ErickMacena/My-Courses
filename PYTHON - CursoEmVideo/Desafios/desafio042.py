a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a + b > c and b + c > a and a + c > b:
    print('Os segmentos podem formar um triangulo ', end='')
    if a == b and b == c:
        tipo = 'Equilátero'
    elif a == b or b == c or a == c:
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'
    print(tipo)
else:
    print('Não pode formar triangulo!')

