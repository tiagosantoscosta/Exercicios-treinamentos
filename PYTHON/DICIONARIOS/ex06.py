dicio={}
lista=[]                           #https://www.youtube.com/watch?v=mw1So0r317Y
time=[] 
while True:
    dicio.clear()                                  # RESOLVI 60% 
    dicio['nome']=str(input('Nome do jogador: '))
    partidas=int(input(f'Quantos partidas {dicio["nome"]} jogou? '))
    lista.clear()
    for c in range(1,partidas+1):   
        lista.append(int(input(f'   Quantos gols na partida {c} ? ')))

    soma=sum(lista)
    dicio['gols']=lista[:]
    dicio['total'] = sum(lista)  # sum(lista, função q soma tudo q está na lista (lista)
    time.append(dicio.copy())
    while True:
        resp=str(input('Quer continuar: [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*40)  
print(f'{"cod nome":<4}{"gols":>18}{"total":>16}') 
print('='*45)
for k, v in enumerate(time):
    print(f'{k:>2}', end='')
    for d in v.values():
        print(f'  {str(d):<15}', end='')
    print()
print('='*50)
while True:
    resp2=int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if resp2 == 999:
        break
    if resp2 >= len(time):
        print(f'ERRO! não existe jogador código {resp2}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[resp2]["nome"]}:')
        for c, v in enumerate(time[resp2]['gols']):
            print(f'No jogo {c+1} fez {v} gols.')
        print('='*50)
print('='*50)
print(f'{"PROGRAMA ENCERRADO":^50}')

        
                
   

   