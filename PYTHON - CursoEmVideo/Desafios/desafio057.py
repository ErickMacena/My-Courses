sexo = input('Digite seu sexo [F/M]: ').strip()[0]
while sexo not in 'MmFf':
    print('Resposta invalida, digite F para feminino ou M para masculino!')
    sexo = input('Digite seu sexo [F/M]: ').upper()
if sexo == 'F':
    print('Benina')
else:
    print('Binino')
