"""
Descrição:
Este programa lê a velocidade de um carro. Se ultrapassar 80 km/h, exibe uma mensagem dizendo que o veículo foi multado e calcula o valor da multa (R$ 7,00 por cada km acima do limite).
"""

vel = int(input('Digite a velocidade que o carro passou no radar: '))
if vel > 80:
    print('O carro estava a {:.0f}Km/h e excedeu o limite de velocidade!'.format(vel))
    print('O valor da multa é de R${:.2f}'.format((vel - 80) * 7))
else:
    print('O carro estava a {:.0f}Km/h, e está dentro do limite de velocidade!'.format(vel))
