soma = 0
for i in range (0,6):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        soma = soma + n1
    else:
        continue
print(soma)
