"""
Descrição:
Este programa lê o nome de uma cidade e verifica se ela começa ou não com a palavra "Santo".
"""

n = input('Digite o nome da cidade: ').strip()
c = n.find("Santo")

if c == 0:
    print('A cidade {} começa com "Santo"'.format(n))
else:
    print('A cidade {} não começa com "Santo"'.format(n))
