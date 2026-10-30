lista = []
while True:
    cadastro = {}
    cadastro['nome'] = input('Digite o nome do produto: ').lower()
    cadastro['preco'] = float(input('Digite o valor do produto: '))
    lista.append(cadastro)
    p = input('Você quer cadastrar mais produtos? [S/N] ').lower()
    print(lista)
    if p == 'n':
        print('Sua compra custou {}'.format(sum([cadastro.get('preco') for cadastro in lista])))
        print('O produto mais caro custa {}'.format(max([cadastro.get('preco') for cadastro in lista])))
        prodMin = min(lista, key=lambda cadastro: cadastro.get('preco'))
        print('O produto mais barato é {}'.format(prodMin.get('nome')))
        break
