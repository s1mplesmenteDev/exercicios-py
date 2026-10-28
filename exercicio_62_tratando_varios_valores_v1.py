lista = []
count = 0
while True:
    n = int(input('Digite os numeros '))
    lista.append(n)
    count = count + 1
    if n == 999:
        print('Você digitou {} numeros e a soma dos numeros é {}'.format(count - 1, sum(lista)-999))
        break
