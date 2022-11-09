from random import randint
from time import sleep
lista=list()
jogos=list()
print('-'*30)
print('{:^30}'.format('JOGO DA MEGASENA'))
print('-'*30)
nun=int(input('Quantos jogos quer sortear? '))
tot=1
while tot<=nun:
    cont=0
    while True:
        computador=randint(1,60)
        if computador not in lista:
            lista.append(computador)
            cont+=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print('-='*3, f'SORTEANDO {nun} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)


    






