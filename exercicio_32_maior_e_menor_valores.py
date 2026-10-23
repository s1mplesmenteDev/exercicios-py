"""
Descrição:
Este programa lê 3 números digitados pelo usuário e exibe qual é o maior e qual é o menor valor entre eles.
"""

numeros = []
for i in range(1, 4):
    n = int(input('Digite um numero: '))
    numeros.append(n)

for numero in range(len(numeros)):
    if numeros[numero] > numeros[numero - 1]:
        maior = numeros[numero]
    elif numeros[numero] < numeros[numero - 1]:
        menor = numeros[numero]

print('Seguindo a lista {}.'.format(numeros))
print('O maior numero da lista é {}.'.format(maior))
print('O menor numero da lista é {}.'.format(menor))
