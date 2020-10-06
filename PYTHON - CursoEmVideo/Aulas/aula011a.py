#Style = [0, 1, 4, 7]
#Text =  [30:37]
#Background = [40:47]
nome = 'Carimbo'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

print('Olá, {}{}{}!'.format(cores['pretoebranco'], nome, cores['limpa']))
