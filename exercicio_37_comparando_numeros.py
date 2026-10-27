"""
Descrição:
Este programa lê dois números inteiros e compara-os, mostrando uma mensagem informando se o primeiro é maior, se o segundo é maior ou se não existe valor maior (são iguais).
"""

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('O PRIMEIRO número é maior!')
elif n2 > n1:
    print('O SEGUNDO número é maior!')
else:
    print('Não existe valor maior, os dois são IGUAIS!')
