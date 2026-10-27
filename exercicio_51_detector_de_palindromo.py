frase = input('Digite uma frase: ')
frase = frase.lower()
fraseFormat = frase.strip()[::-1]
if frase == fraseFormat:
    print('A frase {} é um políndromo!'.format(frase))
else:
    print('A frase {} não é um políndromo!'.format(frase))
