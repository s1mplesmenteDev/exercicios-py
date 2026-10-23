"""
Descrição:
Este programa lê o comprimento de três retas e informa ao usuário se elas podem ou não formar um triângulo.
"""

r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimento da segunda reta: '))
r3 = int(input('Digite o comprimento da terceira reta: '))

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('Com o comprimento dessas retas é possível fazer um triangulo!')
else:
    print('Com o comprimento dessas retas não é possível fazer um triangulo!')
