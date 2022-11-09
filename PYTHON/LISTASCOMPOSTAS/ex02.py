nún=[[], []]
valor=0
for c in range(1,8):
    valor=int(input(f'Digite o {c}º valor: '))
    if valor %2==0:
        nún[0].append(valor)
    else:
        nún[1].append(valor)
nún[0].sort()
nún[1].sort()
print(f'Os valores pares digitados foram: {nún[0]}')
print(f'Os valores ímpares digitados foram: {nún[1]}')
    

