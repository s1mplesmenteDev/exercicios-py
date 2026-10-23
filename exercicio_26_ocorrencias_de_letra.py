"""
Descrição:
Este programa lê uma frase pelo teclado e mostra:
1. Quantas vezes aparece a letra 'A'.
2. Em que posição ela aparece a primeira vez.
3. Em que posição ela aparece a última vez.
"""

frase = input('Digite uma frase: ')
frase_upper = frase.upper()

print('A frase "{}" contém {} a letra A'.format(frase, frase_upper.count('A')))
print('A primeira vez que apareceu a letra A foi na posição {}'.format(frase_upper.find('A')))
print('A última vez que apareceu a letra A foi na posição {}'.format(frase_upper.rfind('A')))
