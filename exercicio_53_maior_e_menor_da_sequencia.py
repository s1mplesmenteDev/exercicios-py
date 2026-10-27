p = []
maior = 0
menor = 0
for i in range (1,6):
    peso = float(input('Digite o peso: '))
    p.append(peso)

for i in range(0,len(p)):
    if p[i] > p[i -1]:
        maior = p[i]
    elif p[i] < p[i -1]:
        menor = p[i]
    else:
        continue
print('O maior peso é {}, e o menor peso é {}'.format(maior,menor))
