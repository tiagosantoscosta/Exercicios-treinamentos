somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho= ''
totmulher20=0
for p in range(1,5):
    print('-----{}° PESSOA-----'.format(p))
    nome=str(input('Nome: ')).strip()
    idade=float(input('Idade: '))
    sexo=str(input('Sexo (M/F): ')).strip()
    somaidade = somaidade + idade

    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Fm' and idade < 20:
        totmulher20= totmulher20 +1
        
mediaidade = somaidade / 4
print('A média do grupo é de {:.2f} anos'.format(mediaidade))
print('O homem mais veho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
    
    

