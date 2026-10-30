from random import randint
while True:
    p = input('Par ou impar? ')
    p.lower()
    if p == 'par' or p == 'impar':
        n = int(input('Digite um numero: '))
        chute = randint(0,9)

        if (n + chute) % 2 == 0 and p == 'par':
            print('Você ganhou!')
        elif (n + chute) % 2 != 0 and p == 'impar':
            print('Você ganhou!')
        else:
            print('Você perdeu!')
            break
