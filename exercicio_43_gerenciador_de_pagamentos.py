"""
Descrição:
Este programa calcula o valor a ser pago por um produto considerando o seu preço normal e a condição de pagamento escolhida:
1: à vista dinheiro/cheque (10% de desconto)
2: à vista no cartão (5% de desconto)
3: em até 2x no cartão (preço formal)
4: 3x ou mais no cartão (20% de juros)
"""

print('=' * 20 + ' LOJAS GUANABARA ' + '=' * 20)
preco = float(input('Preço das compras: R$ '))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 0.10)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 0.20)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
