print('*'*30)
print(f'{"BEM VINDO AO RADAR":^30}')
print('*'*30)
print('Digite uma velocidade para saber se foi multado e saber o valor da multa.\n')
valmulta=130
veloci = 0
limite = 60
limi_adic = (10 * limite / 100) + limite
while veloci != 999:
    print(f'LIMITE {limite} Km !')
    veloci=int(input('Velocidade: Digite 999 para sair Km '))
    if veloci <= limite:
        print(f'\n{veloci}Km! PARABÉNS dentro do limite de velocidade \n')
    elif veloci > limite and veloci <= limi_adic:
        print(f'\n{veloci}Km! ATENÇÃO acima do limite de velocidade, mas entre {limite} e {limi_adic:.0f} para não ser multado.\n')
    elif veloci > limi_adic and veloci < 999:
        print(f'\n{veloci}Km! Acima dos limites de velocidade, você foi multado.\n')
        print(f'MULTA R${valmulta},00 \n')
print('\nFim do programa >>VOLTE SEMPRE!<<')
