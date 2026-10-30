lista = []
cadastro = {}
while True:
    cadastro['idade'] = int(input('Digite sua idade: '))
    cadastro['sexo'] = input('Digite o sexo [M/F]: ').strip().lower()
    lista.append(cadastro)
    p = input('Você quer cadastrar mais pessoas? [S/N] ')
    p.lower()
    if p == 'n':
        print('{} pessoas tem mais de 18 anos!'.format(len([cadastro for cadastro in lista if cadastro.get('idade') >= 18])))
        print('{} homens foram cadastrados!'.format(len([cadastro for cadastro in lista if cadastro.get('sexo') == 'm'])))
        print('{} mulheres tem menos de 18 anos!'.format(len([cadastro for cadastro in lista if cadastro.get('idade') < 18 and cadastro.get('sexo') == 'f'])))
        break
