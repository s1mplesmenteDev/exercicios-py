while True:
    s = input('Digite seu Sexo [M/F]: ')
    s.upper()

    if s == 'm' or s == 'f':
        break
    else:
        print('Valor Invalido! Tente novamente...')
