from random import randint

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

while True:
    print('Os numeros escolhidos são {} e {}'.format(n1,n2))

    print('Você deve escolher uma de opções:')
    print('[1] Somar ')
    print('[2] Multiplicar')
    print('[3] maior ')
    print('[4] Novos numeros')
    print('[5] Sair do programa')

    x = int(input('Escolha uma das opções acima: '))

    match x:
        case 1:
            print(n1+n2)
        case 2:
            print(n1*n2)
        case 3:
            if n1 > n2:
                print('{} é maior que {}'.format(n1,n2))
            else:
                print('{} é maior que {}'.format(n2,n1))
        case 4:
            n1 = int(input('Digite um numero: '))
            n2 = int(input('Digite outro numero: '))
            print('Os novos numeros são {} e {}'.format(n1,n2))
        case 5:
            print('Programa Finalizado!')
            break
