lista=[]
ímpar=list()
par=list()
while True:
    lista.append(int(input('Digite um número: ')))
    resp=str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for c, v in enumerate(lista):
    if v %2 ==0:
        par.append(v)
    if v %2==1:
        ímpar.append(v)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {ímpar}')