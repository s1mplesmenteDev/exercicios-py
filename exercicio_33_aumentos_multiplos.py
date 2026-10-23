"""
Descrição:
Este programa calcula o aumento de salário de um funcionário: para salários superiores a R$ 1.250,00, calcula um aumento de 10%; para salários inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Digite o valor do seu salário: '))
if salario > 1250:
    print('O seu novo salário é {:.2f}'.format(salario * 1.10))
elif salario <= 1250:
    print('O seu novo salário é {:.2f}'.format(salario * 1.15))
