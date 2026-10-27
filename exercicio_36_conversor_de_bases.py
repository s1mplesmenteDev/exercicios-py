"""
Descrição:
Este programa lê um número inteiro qualquer e pede para o usuário escolher a base de conversão:
1 para Binário, 2 para Octal e 3 para Hexadecimal.
"""

num = int(input('Digite um número inteiro: '))
print("""[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL""")

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
