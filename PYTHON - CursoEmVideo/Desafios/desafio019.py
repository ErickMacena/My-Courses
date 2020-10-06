from random import randint

alunos = [input('Digite o nome do {} aluno: '.format('primeiro')),
          input('Digite o nome do {} aluno: '.format('segundo')),
          input('Digite o nome do {} aluno: '.format('terceiro')),
          input('Digite o nome do {} aluno: '.format('quarto'))
          ]

print('O aluno escolhido para limpar o quadro é: {}'.format(alunos[randint(0, 3)]))
