"""
Descrição:
Este programa lê um ano qualquer e informa se ele é um ano bissexto ou não.
"""

ano = int(input('Digite o ano para saber se é bissexto: '))
if ano % 4 == 0 or ano % 400 == 0:
    print('O ano {}, é um ano bissexto!'.format(ano))
else:
    print('O ano {}, não é bissexto!'.format(ano))
