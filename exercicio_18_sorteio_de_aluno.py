"""
Descrição:
Este programa lê o nome de quatro alunos e sorteia aleatoriamente um deles para apagar o quadro.
"""

import random

alunos = []
for i in range(1, 5):
    nome = str(input('Digite o nome do aluno: '))
    alunos.append(nome)

print('O aluno escolhido é: {}'.format(random.choice(alunos)))
