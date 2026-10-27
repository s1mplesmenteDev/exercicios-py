"""
Descrição:
Este programa avalia a aprovação de um empréstimo bancário para a compra de uma casa.
Calcula a prestação mensal (valor da casa / (anos * 12)) e verifica se ultrapassa 30% do salário do comprador.
"""

casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos vai pagar? '))

prestacao = casa / (anos * 12)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))

if prestacao > (salario * 0.30):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONCEDIDO!')
