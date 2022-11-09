from time import sleep
def contador(i, f ,p):              #RESOLVI 70%
    print('-='*25)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2)
    if p < 0:
        p *= -1
    if p ==0:
        p = 1
    if i < f:
        cont = i
        while cont < f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont = cont + p    
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont = cont - p    
        print('FIM!')
        print('-='*25)



contador(0, 100 , 10)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
início=int(input('Início: '))
fim=int(input('Fim: '))
passo=int(input('Passo: '))
contador(início, fim, passo)