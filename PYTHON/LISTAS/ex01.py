valores=[]
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c} :')))    
print(f'Foi criado a lista {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ',end='')
for pos, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{pos}...',end='')
print(f'\nO menor valor foi: {min(valores)} nas posições ',end='')
for pos, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{pos}...',end='')