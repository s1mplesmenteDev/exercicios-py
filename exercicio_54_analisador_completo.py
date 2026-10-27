lista_usuarios=[]
media_idade = 0
contador = 0
for i in range (1,5):
    usuario = {}
    usuario['nome'] = input('digite seu nome: ')
    usuario['idade'] = int(input('digite sua idade: '))
    usuario['sexo'] = input('digite seu sexo: ')
    
    lista_usuarios.append(usuario)

media_idade = sum(usuario.get('idade',0) for usuario in lista_usuarios)/4
cMulher = len([usuario for usuario in lista_usuarios if usuario['sexo'] == 'F' and usuario['idade'] <= 20])
Homens = [usuario for usuario in lista_usuarios if usuario['sexo'] == 'M']
Homem_max = max(Homens, key=lambda usuario: usuario.get('idade',0))
print('A média de idade do grupo é {}'.format(media_idade))
print('O homem mais velho do grupo é o {}'.format(Homem_max['nome']))
print('No grupo, {} mulheres tem menos de 20 anos de idade.'.format(cMulher))
