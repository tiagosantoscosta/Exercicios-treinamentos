from time import sleep                  #RESOLVI 100% :D
from random import randint
numeros=list()
def sorteia():
    print(f'Sorteando 5 valores da lista: ',end='')
    for cont in range(0,5):
        n = randint(0,10)
        numeros.append(n)
        print(n,end=' ',flush=True)
        sleep(0.3)
    print('PRONTO!')
    

def somaPar():
    print(f'Somando os valores pares de {numeros}, temos ', end='')
    soma=par=0
    for valores in numeros:
        if valores %2 == 0:
            par = valores
            soma+= par
    print(soma)
    print()


sorteia()
somaPar()
