from random import randint #Faz o computador "pensar" em um número
from time import sleep
computador = randint (0, 5)

jogador=int(input('\nDigite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabén você venceu!')
else :
    print('Infelizmente você perdeu, pensei no número {} e não no {}.'.format(computador, jogador))
print('FIM!')

