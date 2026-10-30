lista = []
count = 0
while True:
    n = int(input('Digite um valor (digite 999 para sair!): '))
    if n == 999:
        print(f'A soma dos {count} foi {sum(lista)}')
        break
    lista.append(n)
    count = count + 1
