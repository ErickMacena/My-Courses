salario = float(input('Digite seu salário atual: '))

if salario > 1250:
    salario = salario * 1.1
else:
    salario = salario * 1.15

print('Seu novo salário será R${:.2f}.'.format(salario))