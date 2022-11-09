print('*'*30)
print('{:^30}'.format('LOJA DA ULTILIDADE'))            
print('*'*30)
total=0
maior=0
menor=0
cont=0
barato=''
while True:
    produto=str(input('Nome do produto: '))
    preço=float(input('Preço: R$ '))
    resposta=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    total=total+preço
    cont+=1
    
    if cont == 1:
        menor = preço
        barato= produto
    else:
        if preço < menor:
            menor = preço
            barato=produto
               
    if preço > 1000:
        maior+=1
    



    if resposta == 'N':
        break
    
print(f'O total da compra foi: R${total:.2f}')
print(f'Temos {maior} produto(s) custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} custando R${menor:.2f}')



