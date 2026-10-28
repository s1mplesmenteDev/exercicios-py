n = int(input('Digite um numero: '))
count = n
f = 1
while n > 1:
    f = f * n
    n = n - 1
print('O fatorial do numero é {}'.format(f))
