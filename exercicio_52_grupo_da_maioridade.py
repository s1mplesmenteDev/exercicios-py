a = []
mi = 0
for i in range (1,8):
    a = int(input('Digite o seu ano de nascimento: '))
    if 2026 - a >= 21:
        mi = mi + 1
    else:
        continue
print('{} são maiores de idade!'.format(mi))
