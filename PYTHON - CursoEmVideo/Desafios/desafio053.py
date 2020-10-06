frase = input('Digite uma frase: ').replace(' ', '')
ePalin = 1
for i in range(0, len(frase)):
    if frase[i] != frase[len(frase) - i - 1]:
        ePalin = 0

if ePalin == 0:
    print('Esta frase não é um palíndromo!')
else:
    print('Esta frase é um palíndromo!')
