"""
Descrição:
Este programa lê o nome de uma pessoa e identifica se ela possui o sobrenome "Silva" em qualquer parte do nome.
"""

name = input('Digite seu nome: ')

if 'Silva' in name:
    print('{} tem Silva no nome.'.format(name))
else:
    print('{} não tem Silva no nome.'.format(name))
