from datetime import date
nascimento=int(input('\nInforme seu ano de nascimento: '))
ano = date.today().year
soma = ano - nascimento
if soma < 18:
    anoalistamento = nascimento + 18
    falta = 18 - soma
    print('Você tem {} anos e falta {} anos para se alistar.'.format(soma,falta))
    print('Seu alistamento vai ser em {}.'.format(anoalistamento))
elif soma == 18:
    print('Você tem {} anos, é a hora de se alistar.'.format(soma))
elif soma > 18:
    anoalistamento = nascimento + 18
    passou = (ano - nascimento) - 18
    print('Você tem {} anos e passou {} anos do tempo do alistamento.'.format(soma,passou))
    print('Seu alistamento foi em {}.'.format(anoalistamento))

