n = int(input('Digite um numero: '))
if n%1 == 0 and n%n == 0:
    print('O numero {}, é um numero primo!'.format(n))
else:
    print('O numero {}, não é primo!'.format(n))
