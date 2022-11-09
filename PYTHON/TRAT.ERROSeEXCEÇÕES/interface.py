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


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    cont = 0
    for c in lista:
        cont+=1
        print(f'\033[33m{cont}\033[m - \033[36m{c}\033[m')
    print(linha())
    opc = leiaInt('\033[32mSua Opção:\033[m ')
    return opc
        
    