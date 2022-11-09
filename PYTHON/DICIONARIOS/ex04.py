dicio={}
lista=[]                                       # RESOLVI 100% :D
dicio['nome']=str(input('Nome do jogador: '))
partidas=int(input(f'Quantos partidas {dicio["nome"]} jogou? '))
for c in range(1,partidas+1):   
    lista.append(int(input(f'   Quantos gols na partida {c} ? ')))
soma=sum(lista)
dicio['gols']=lista
dicio['total'] = sum(lista)  # sum(lista, função q soma tudo q está na lista (lista)
print('-='*40)   
print(dicio)
print('-='*40) 
for c, v in dicio.items():
    print(f'O campo {c} tem o valor {v}')
print('-='*40) 
print(f'O jogador {dicio["nome"]} jogou {partidas} partidas.')
for c, v in enumerate(lista):
    print(f'  => Na partida {c+1}, fez {v} gols.')
print(f'Foi um total de {soma} gols.\n')

   
        



    