def ficha(nome=0, gols=0):
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato.')
    return nome
                                       #REOLVI 70%

print('-'*40)
nome=str(input('Nome do jogador: '))
gols=str(input('Números de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    nome = str('<desconhecido>')
ficha(nome, gols)



