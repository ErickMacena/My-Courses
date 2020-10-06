nome = input('Digite seu nome completo: ').split()

print('''Muito prazer em te conhecer!
Seu primeiro nome é {}.
Seu ultimo nome é {}.'''.format(nome[0], nome[len(nome) - 1]))
