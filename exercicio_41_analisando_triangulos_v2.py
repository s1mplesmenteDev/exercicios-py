"""
Descrição:
Este programa analisa o comprimento de três retas para verificar se podem formar um triângulo e classifica a forma:
EQUILÁTERO (todos os lados iguais), ISÓSCELES (dois lados iguais) ou ESCALENO (todos os lados diferentes).
"""

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
