"""
Descrição:
Este programa calcula o preço de uma passagem com base na distância percorrida em km. Cobra R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.
"""

dist = int(input('Digite quantos kilometros de viagem vão ser percorridos: '))
if dist > 200:
    print('Percorrer {}km, custará R${}.'.format(dist, dist * 0.45))
else:
    print('Percorrer {}km, custará R${}.'.format(dist, dist * 0.50))
