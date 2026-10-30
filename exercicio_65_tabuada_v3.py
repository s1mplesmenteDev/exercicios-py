while True:
    n = int(input('Digite o numero que vamos gerar a tabuada: '))
    if n < 0:
        print('Você encerrou o programa!')
        break
    else:
        for i in range(0,11):
            print(f'{n} x {i} = {n*i}')
