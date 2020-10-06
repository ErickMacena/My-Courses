from random import shuffle

alunos = [input('Digite o nome do {} aluno: '.format('primeiro')),
          input('Digite o nome do {} aluno: '.format('segundo')),
          input('Digite o nome do {} aluno: '.format('terceiro')),
          input('Digite o nome do {} aluno: '.format('quarto'))]
#comentario ...

shuffle(alunos)

print('A ordem de apresentação será:')

print('{}° - {}'.format('1', alunos[0]))
print('{}° - {}'.format('2', alunos[1]))
print('{}° - {}'.format('3', alunos[2]))
print('{}° - {}'.format('4', alunos[3]))
