print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)
listagem=('Lápis',1.75,'Borraha',2.00,'Caderno',15.90,'Estojo',25.00,'Tranferidor',4.20,
            'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
for c in range(0,len(listagem)):
    if c %2==0:
        print(f'{listagem[c]:.<30}',end='') #(:.<30) coloca o '.'  a direita 30 caracteres
    else:
        print(f'R${listagem[c]:>7.2f}') #(:>7.2f) coloca a variável {listagem[c]} à 7 casas a direita e (.2f) adiciona 2 casas depois do . 
print('-'*40)

