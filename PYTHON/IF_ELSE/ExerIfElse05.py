from datetime import date
ano=int(input('\nDigite o ano, ou digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print(f'O ano {ano} não é bissexto')