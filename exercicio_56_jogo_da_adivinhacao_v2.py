from random import randint

print('Adivinhe o numero!')
print('Você consegue adivinhar o numero sorteado entre 0 e 10?')

numerosorteado = randint(0,10)
contador = 0
while True:
    chute = int(input('Dê seu palpite: '))

    if numerosorteado == chute:
        print('Parabens você acertou!')
        print('Você realizou {} chutes até acertar!'.format(contador))
        break
    else:
        print('Você está quase lá!')
        contador = contador + 1
