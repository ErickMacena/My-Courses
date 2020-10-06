a = float(input('Digite a primeira aresta: '))
b = float(input('Digite a segunda aresta: '))
c = float(input('Digite a terceira aresta: '))

if(a + b > c and b + c > a and a + c > b):
    print('Forma triangulo!')
else:
    print('Não forma triangulo!')
