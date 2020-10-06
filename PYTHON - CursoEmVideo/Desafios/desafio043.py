peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    resultado = 'Abaixo do Peso'
elif imc < 25:
    resultado = 'Peso ideal'
elif imc < 30:
    resultado = 'Sobrepeso'
elif imc <= 40:
    resultado = 'Obesidade'
else:
    resultado = 'Obesidade mórbida'

print('Seu IMC é de {:.1f}. \033[1:33m{}\033[m'.format(imc, resultado))
