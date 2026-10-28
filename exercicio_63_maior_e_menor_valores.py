lista = []
i = 0
r = 10
while i < r:
    n = int(input('Digite os numeros'))
    lista.append(n)
    i = i + 1
    if i == r:
        p = input('Você quer digitar mais 5 valores? [S/N] ')
        p.lower()
        if p == 's':
            i = i - 5
        else:
            print('Essa é a média dos valores digitados: {:.2f}'.format(sum(lista)/len(lista)))
            print('Esse é o menor numero: {}'.format(min(lista)))
            print('Esse é o maior numero: {}'.format(max(lista)))
