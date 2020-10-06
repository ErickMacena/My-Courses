i = s = n = 0

while True:
    n = int(input('Digite um número [999 para]? '))
    if n == 999:
        break
    s += n
    i += 1
print(f'Foram digitados {i} números e a soma entre eles é {s}')
