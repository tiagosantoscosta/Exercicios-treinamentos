from random import randint
computador = randint(1,10)
r=0
cont=0
print('\nSou o seu computador...\nAcabei de pensar em um número entre 1 e 10, será que você adinvinha qual foi?' )
while r != computador:
    cont=cont +1
    r=int(input('\nQual o seu palpite: '))
    if r < computador:
        print('\nMAIS...Tente mais uma vez.')
    if r > computador:
        print('\nMENOS...Tente mais uma vez.')
    if r == computador:
        print('\nCERTO, parabéns! O computador pensou no número \033[1;32m>> {} <<\033[m'.format(computador))
print('\nVocê precisou de {} palpites para vencer.'.format(cont))
print('FIM')