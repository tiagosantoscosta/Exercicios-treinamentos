from time import sleep 
valor1=int(input('\nDigite o primeiro valor: '))
valor2=int(input('Digite o segundo valor: '))
menu=0
while menu != 5:
    menu=int(input('\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa\n>>> Qual é a sua opção? '))
    if menu == 1:
        soma=valor1+valor2
        print(f'\nSOMAR... Resultado entre {valor1} + {valor2} é: {soma}')
        sleep(1)
    elif menu == 2:
        mult=valor1*valor2
        print(f'\nMULTIPLICAR... Resultado entre {valor1} X {valor2} é: {mult}')
        sleep(1)
    elif menu == 3:
        if valor1 > valor2:
            print(f'\nMAIOR... Resultado entre {valor1} e {valor2} é: {valor1}')
        elif valor1 == valor2:
            print('\nOs valores são iguais')
        else:
            print(f'\nMAIOR... Resultado entre {valor1} e {valor2} é: {valor2}')
        sleep(1)
    elif menu == 4:
        print('\nInforme os números novamente:')
        valor1=int(input('\nDigite o primeiro valor: '))
        valor2=int(input('Digite o segundo valor: '))
    elif menu >= 6:
        print('\nOpção invalida, tente novamente')
    print('=-='*14)
print('Finalizando...')
sleep(1)
print('FIM')