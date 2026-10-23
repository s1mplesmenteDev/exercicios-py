"""
Descrição:
Este programa lê um número inteiro qualquer e exibe na tela se ele é PAR ou ÍMPAR.
"""

n = int(input('Digite um numero: '))
if n % 2 == 0:
    print('O numero {} é par'.format(n))
else:
    print('O numero {} é ímpar'.format(n))
