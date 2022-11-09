
termo=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a progreção: '))
decimo= termo + (10) * razao
for c in range(termo,decimo,razao):
    print('{}'.format(c), end=' ➡  ')
print('ACABOU')

