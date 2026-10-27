"""
Descrição:
Este programa lê duas notas de um aluno, calcula a sua média e exibe se o aluno foi APROVADO (média >= 7.0), em RECUPERAÇÃO (entre 5.0 e 6.9) ou REPROVADO (média < 5.0).
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))

if media >= 7.0:
    print('O aluno está APROVADO!')
elif 5.0 <= media < 7.0:
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('O aluno está REPROVADO!')
