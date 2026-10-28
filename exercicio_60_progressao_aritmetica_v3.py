r = int(input('Digite a razão da progressao aritmetica: '))
p = int(input('Digite o primeiro termo da progressão aritmetica: '))
pa = p
contagem = 0
d = 10
while contagem != d:
    print('1º progressão aritmetica é : {}'.format(pa))
    pa = pa + r
    contagem = contagem + 1
    if contagem == d:
        novod = int(input('Você quer ver mais quantas progressões? '))
        if novod == 0:
            print('Você encerrou a progressão!')
            break
        elif novod != 0:
            d = d + novod
            continue
