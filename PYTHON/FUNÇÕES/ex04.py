def maior(*nun):                         #RESOLVI 100%
    print('-='*30)                    #* PODE-SE USAR IF OU O MÉTODO MAX() PRA SABER O MAIOR VALOR
    print('Analisando os valores passados...')
    maio=cont=0
    for c in nun:
        print(c, end=' ')
        if cont == 0:
            maio = c
        else:
            if c > maio:
                maio = c
        cont+=1
    print(f'Foram informado {len(nun)} valores ao todo.')
    print(f'O maior valor informado foi {maio}.')


maior(5,2,3,4,8,9,10)
maior(2,8,7)
maior(8,0,8)
maior()