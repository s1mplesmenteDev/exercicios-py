"""
Descrição:
Este programa gera um número inteiro aleatório entre 1 e 10 e pede para o usuário adivinhar qual foi o número sorteado, repetindo até que o usuário acerte.
"""

from random import randint

print('Jogo de Adivinhação')
numero = randint(1, 10)

while True:
    chute = int(input('Qual numero você acha que foi sorteado? '))
    if chute == numero:
        print('Você acertou!')
        print('O número sorteado é {}.'.format(numero))
        break
    else:
        print('Tente novamente!')
