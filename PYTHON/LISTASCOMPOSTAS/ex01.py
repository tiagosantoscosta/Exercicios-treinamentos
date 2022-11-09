maior=menor=0
lista=list()              #PROGRAMA QUE ADICIONA UMA LISTA(lista) EM OUTRA LISTA(total)                                                   
total=list()              #E NO FINAL COMPARA O MAIOR E MENOR PESO E QUANTAS PESSOAS FORAM CADASTRADAS
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(total) == 0:   #IF GERADO ANTES DA LISTA (total) SER CRIADA PARA O IF SER IGUAL A 0 (True)
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior=lista[1]
        if lista[1] < menor:
            menor=lista[1]
    resp=str(input('Quer continuar? [S/N] ')).strip().upper()
    total.append(lista[:])
    lista.clear()
    if resp in 'Nn':
        break  

print(f'O maior peso foi {maior:.2f} kg, peso de ', end='')
for p in total:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi {menor:.2f} kg, peso de ', end='')
for p in total:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()
print(f'Ao todo, você cadastrou {len(total)} pessoas')
