while True:

    print('-'*10)
    print('Bem vindo ao caixa eletronico!')
    print('-'*10)

    saque = int(input('Digite o valor que deseja sacar: '))

    if saque == 0:
        print('-'*10)
        print('Caixa encerrado!')
        print('-'*10)
        break

    n50 = 0
    n20 = 0
    n10 = 0
    n1 = 0

    resto = saque

    if resto // 50 > 0:
        n50 = saque // 50
        resto = resto % 50

    if resto // 20 > 0:
        n20= resto // 20
        resto = resto % 20

    if resto // 10 > 0:
        n10 = resto // 10
        resto = resto % 10

    if resto // 1 > 0:
        n1 = resto

    print(f'Você terá {n50} cedulas de 50')
    print(f'Você terá {n20} cedulas de 20')
    print(f'Você terá {n10} cedulas de 10')
    print(f'Você terá {n1} cedulas de 1')
