from random import randint         #Resolvi 70% 
from time import sleep
from operator import itemgetter
dado={'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6) }
ranking = list()
print('Valores sorteados:')
for c, v in dado.items():
    print(f'{c} tirou {v} no dado.')
    sleep(1)

print('-='*50)
print(f'{"    == RANKING DOS JOGADORES =="}')
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
for c, v in enumerate(ranking):
    print(f'    {c+1}º lugar: {v[0]} com {v[1]}.')
  
        





