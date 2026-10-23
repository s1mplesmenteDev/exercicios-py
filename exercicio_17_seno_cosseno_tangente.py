"""
Descrição:
Este programa lê um ângulo qualquer em graus e calcula e exibe os valores do seno, cosseno e tangente desse ângulo.
"""

import math

angulo = float(input('Digite o ângulo em graus: '))
angulo_rad = math.radians(angulo)
print('Esse são os seno: {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(
    math.sin(angulo_rad), math.cos(angulo_rad), math.tan(angulo_rad)
))
