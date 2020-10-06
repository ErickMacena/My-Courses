v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))

print('-=' * 19)
print('-=' * 8, 'MENU', '-=' * 8)
print('-=' * 19)
user = int(input('''\033[1:31m[1]\033[m \033[4mSOMAR\033[m
\033[1:31m[2]\033[m \033[4mMULTIPLICAR\033[m
\033[1:31m[3]\033[m \033[4mMAIOR\033[m
\033[1:31m[4]\033[m \033[4mNOVOS NÚMEROS\033[m
\033[1:31m[5]\033[m \033[4mSAIR\033[m
O que você deseja fazer? '''))

while user >= 1 and user < 5:
    if user == 4:
        print('')
        v1 = int(input('Digite um valor: '))
        v2 = int(input('Digite outro valor: '))
        print('')
        print('-=' * 19)
        print('-=' * 8, 'MENU', '-=' * 8)
        print('-=' * 19)
    elif user == 1:
        print('\033[1:34m{} + {} = {}\033[m'.format(v1, v2, v1 + v2))
        print('')
    elif user == 2:
        print('\033[1:34m{} X {} = {}\033[m'.format(v1, v2, v1 * v2))
        print('')
    elif user == 3:
        if v1 > v2:
            print('\033[1:34m{} é maior que {}\033[m'.format(v1, v2))
        else:
            print('\033[1:34m{} é maior que {}\033[m'.format(v2, v1))
        print('')

    user = int(input('''\033[1:31m[1]\033[m \033[4mSOMAR\033[m
\033[1:31m[2]\033[m \033[4mMULTIPLICAR\033[m
\033[1:31m[3]\033[m \033[4mMAIOR\033[m
\033[1:31m[4]\033[m \033[4mNOVOS NÚMEROS\033[m
\033[1:31m[5]\033[m \033[4mSAIR\033[m
O que você deseja fazer? '''))
print('\033[1:33mAté mais, amigo!\033[m')
