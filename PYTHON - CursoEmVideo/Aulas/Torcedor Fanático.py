import sys

entradas = input().split()

c = int(entradas[0])
t = int(entradas[1])
a = int(entradas[2])
l = int(entradas[3])
e = int(entradas[4])

uFlasco = 100

if c == 1:
    if t == 1:
        uFlasco += 33.21
    elif t == 2:
        uFlasco += 10.51
    else:
        uFlasco -= 20.7

    if a > 40000:
        uFlasco += (a * 0.0008)
    else:
        uFlasco -= (a * 0.0008)

    if e > 0:
        uFlasco += e * 2.7
    else:
        uFlasco += e * 1.8

else:
    if t == 2 or t == 3:
        uFlasco = 0
        print('''A chance de vitoria do flamengo e de {}
        '''.format(uFlasco))
        sys.exit()
    else:
        uFlasco -= 10.87

    if a > 45000:
        uFlasco -= (a * 0.0003)
    else:
        uFlasco -= (a * 0.0001)

    if e > 0:
        uFlasco += e * 5.2
    else:
        uFlasco -= e * 1.5

uFlasco -= (l * 2.7)

print('''A chance de vitoria do flamengo e de {:.2f}
'''.format(uFlasco))
