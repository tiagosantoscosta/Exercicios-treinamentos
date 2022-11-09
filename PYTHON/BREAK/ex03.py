from random import randint 
print('*'*25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('*'*25)
cont=0
while True:
    numero=int(input('\nDigite um valor: '))
    r=str(input('Par ou ímpar? [P/I] ')).strip().upper()
    cont+= 1
    computador= randint(0,10)
    soma=numero+computador
    if r == 'P' and soma %2 ==0:
        print(f'\nVocê jogou {numero} e o computador {computador},a soma deu {soma}.\nVocê VENCEU!')
    elif r == 'P' and soma %1 ==0:
        print(f'\nVocê jogou {numero} e o computador {computador},a soma deu {soma}.\nVocê PERDEU!')
        break
    elif r == 'I' and soma %2 ==0:
        print(f'\nVocê jogou {numero} e o computador {computador},a soma deu {soma}.\nVocê PERDEU!')
        break
    elif r == 'I' and soma %1 ==0:
        print(f'\nVocê jogou {numero} e o computador {computador},a soma deu {soma}.\nVocê VENCEU!')
print('\nVocê venceu {} vezes'.format(cont-1))
print('{:^40}'.format('GAME OVER'))


