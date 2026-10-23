"""
Descrição:
Este programa demonstra operações de fatiamento (slicing) e busca simples em cadeias de caracteres (strings).
"""

frase = "Curso em Vídeo Python"
print(frase[13:20])
print(frase[:14])
print(frase[13:])
print('Curso' in frase)

frase = frase.replace('Python', 'JavaScript')
print(frase)

frase = "Curso em Vídeo Python"
frase = frase.split()
frase = '-'.join(frase)
print(frase)
