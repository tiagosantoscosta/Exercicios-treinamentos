print('\nDigite 2 números inteiros para comparar. ')
num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))
if num1 > num2:
    print('O primeiro valor é \033[1;31mMAIOR\033[m: {}'.format(num1))    #  *FOI ADICIONADO CORES \033[1;31m
elif num2 > num1:                                                          
    print('O segundo valor é \033[1;31mMAIOR\033[m: {}'.format(num2))
elif num1 == num2:
    print('Não existe valor maior, os dois são \033[1;31mIGUAIS\033[m.')



    

