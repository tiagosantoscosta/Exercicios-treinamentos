lista=[]
while True:
    lista.append(int(input('Digite um valor: ')))
    r=str(input('Quer continuar? [S/N]')).strip().upper()   
    if r == 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em decrescente são {lista} ')
if 5 in lista:
    print('O numero 5 ESTÁ na lista')
else:
    print('O número 5 NÃO está na lista')