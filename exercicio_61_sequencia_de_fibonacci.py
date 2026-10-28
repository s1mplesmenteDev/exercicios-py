n = int(input('Digite o numero de elementos que você quer ver da sequencia de Fibonacci: '))
nSequence = 0
nSequence1 = 1
f = 0
count = 0
while count < n:
    print('{}'.format(nSequence))
    f = nSequence + nSequence1
    nSequence = nSequence1
    nSequence1 = f
    count = count + 1
