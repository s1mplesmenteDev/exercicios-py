dAluguel = int(input('Digite o numero de dias que você ficou com o carro: '))
kmRodado = float(input('Digite quantos km você rodou: '))

print('Você alugou o carro {} dias e rodo {} km. O total a pagar vai ser R${:.2f} !'.format(dAluguel,kmRodado,dAluguel*60+kmRodado*0.15))