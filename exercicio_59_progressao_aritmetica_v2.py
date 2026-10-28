r = int(input('Digite a razão da progressao aritmetica: '))
p = int(input('Digite o primeiro termo da progressão aritmetica: '))
pa = p
contagem = 0
d = 10
while contagem != d:
    print('1º progressão aritmetica é : {}'.format(pa))
    pa = pa + r
    contagem = contagem + 1
