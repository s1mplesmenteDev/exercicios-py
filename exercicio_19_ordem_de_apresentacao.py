"""
Descrição:
Este programa lê o nome de quatro alunos e sorteia a ordem de apresentação dos trabalhos, embaralhando a lista.
"""

import random

alunos = []
for i in range(1, 5):
    nome = input('Digite o nome do aluno: ')
    alunos.append(nome)

random.shuffle(alunos)
print('Embaralhou a ordem dos alunos:')
for i, aluno in enumerate(alunos, start=1):
    print('{}- {}'.format(i, aluno))
