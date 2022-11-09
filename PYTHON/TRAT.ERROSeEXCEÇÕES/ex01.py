def leiaInt(numero):
    while True:
        try:
            n = int(input(numero))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n
    

def leiaFloat(numero):
    while True:
        try:
            n = float(input('Digite um número real: '))
        except (TypeError, ValueError):
            print('\033[31mERRO! Por favor digite um número Real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar')
            return 0
        else:
            return n


n1 = leiaInt('Digite um número Iteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print( f'O valor inteiro digitador foi {n1} e o Real foi {n2}')