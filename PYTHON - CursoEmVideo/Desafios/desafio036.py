casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Quantos anos você vai pagar? '))

mensalidade = casa / (anos * 12)

print('O valor da sua mensalidade será de R${:.2f}.'.format(mensalidade))

if mensalidade > (salario * 0.3):
    print('EMPRESTIMO NEGADO!')
else:
    print('EMPRESTIMO ACEITO!')
