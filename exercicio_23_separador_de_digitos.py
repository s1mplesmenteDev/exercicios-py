"""
Descrição:
Este programa lê um número de 1 a 9999 e mostra na tela cada um dos seus dígitos separados (unidade, dezena, centena e milhar).
"""

while True:
    n = input('Digite um número de 1 a 9999: ')
    if n.isdigit() and len(n) <= 4 and int(n) >= 1:
        n = n.zfill(4)
        break
    else:
        print('Erro: Por favor, digite apenas números inteiros!')

print('O número é {}'.format(n))
print('Sua unidade é {}'.format(n[3]))
print('Sua dezena é {}'.format(n[2]))
print('Sua centena é {}'.format(n[1]))
print('Seu milhar é {}'.format(n[0]))
