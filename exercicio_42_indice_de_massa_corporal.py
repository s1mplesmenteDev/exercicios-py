"""
Descrição:
Este programa lê o peso e a altura de uma pessoa, calcula o seu Índice de Massa Corporal (IMC) e exibe o status:
Abaixo de 18.5: Abaixo do Peso | Entre 18.5 e 25: Peso Ideal | 25 a 30: Sobrepeso | 30 a 40: Obesidade | Acima de 40: Obesidade Morbida.
"""

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
