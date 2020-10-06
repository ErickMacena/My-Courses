i = 1
deMaior = homens = mulherNova = 0
text = 'CADASTRE UMA PESSOA'
while True:
    print('-' * 30)
    print(f'{text:^30}')
    print('-' * 30)
    idade = int(input(f'Digite a idade da {i}° pessoa: '))
    sexo = input(f'Digite o sexo da {i}° pessoa: [M/F] ').replace(' ', '')[0].upper()
    while sexo not in 'MF':
        sexo = input(f'Digite o sexo da {i}° pessoa: [M/F] ').replace(' ', '')[0].upper()
    print('-' * 30)

    if idade > 18:
        deMaior += 1
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        mulherNova += 1

    r = input('Quer continuar? [S/N] ').replace(' ', '')[0].upper()
    while r not in 'SN':
        r = input('Quer continuar? [S/N] ').replace(' ', '')[0].upper()
    i += 1
    if r == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'''Total de pessoas com mais de 18 anos: {deMaior}
Ao todo temos {homens} homens cadastrados
E temos {mulherNova} mulheres com menos de 20 anos''')
