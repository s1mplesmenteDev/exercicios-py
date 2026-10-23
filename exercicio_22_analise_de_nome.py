"""
Descrição:
Este programa lê o nome completo de uma pessoa e mostra:
1. O nome com todas as letras maiúsculas.
2. O nome com todas as letras minúsculas.
3. Quantas letras ao todo (sem considerar espaços).
4. Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite seu nome completo: ')).strip()

print('O nome em lower: {}'.format(nome.lower()))
print('O nome em upper: {}'.format(nome.upper()))
print('O nome tem {} letras'.format(len(nome.replace(' ', ''))))

nome_split = nome.split()
print('O primeiro nome tem {} letras'.format(len(nome_split[0])))
