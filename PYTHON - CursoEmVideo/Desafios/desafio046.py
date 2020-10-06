from time import sleep

print('Iniciando a contagem regressiva!')
sleep(1)

cores = ['\033[1:34m', '\033[1:33m']
for i in range(10, -1, -1):
    if i % 2 == 0:
        print(cores[0], end='')
    else:
        print(cores[1], end='')
    print('{}\033[m'.format(i))
    sleep(0.5)
print('BUUUUUUM')
