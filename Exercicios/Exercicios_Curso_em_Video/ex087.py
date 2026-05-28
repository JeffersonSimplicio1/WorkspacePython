# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
import random
from operator import itemgetter
from time import sleep

jogos ={}
ranking=[]


print('Valores sorteados')
jogos['jogador1'] = random.randint(1,6)
jogos['jogador2'] = random.randint(1,6)
jogos['jogador3'] = random.randint(1,6)
jogos['jogador4'] = random.randint(1,6)

for i,v in jogos.items():
    print(f'{i} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogos.items(),key=itemgetter(1), reverse=True)

print('-='*30)
print('    ==  RANKING DOS JOGADORES  ==    ')
for i,v in enumerate (ranking):
    print(f'          {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)