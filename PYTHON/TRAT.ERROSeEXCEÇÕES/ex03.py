from interface import *
from time import sleep
from arquivo import *

arq = 'cursoemvídeo.txt'

if not arquivoExiste(arq):
    criaArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar novas pessoas','Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[031mERRO! Digite uma opção válida!\033[m')
    sleep(2)
        

