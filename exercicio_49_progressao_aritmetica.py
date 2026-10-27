a = int(input('Digite o primeiro termo da progressão aritmetica: '))
r = int(input('Digite a razão da progressão aritmetica: '))
p = a+r
for i in range (0,10):
    print('{}º termo da progressão aritmetica é {}'.format(i+1,p))
    p = p + r
