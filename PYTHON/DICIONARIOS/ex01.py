ficha={}                                 #CONSEGUI FAZER 100% :)
ficha['Nome']=str(input('Nome: '))
ficha['Média']=float(input(f'Média de {ficha["Nome"]}: '))
print('='*40)
if ficha['Média'] >= 7:
    ficha['Situação'] = 'Aprovado'
elif ficha['Média'] <= 5:
    ficha['Situação'] = 'Reprovado'
else:
    ficha['Situação'] = 'Recuperação'
for c,v in ficha.items():
    print(f'-{c} é igual a {v}')
