lista=[]


for c in range(0,5):
    nun=int(input('Digite um valor: '))
    if c == 0:
        lista.append(nun)
        print('Adicionado ao final da lista...')
    elif nun > lista[-1]:
        lista.append(nun)
        print('Adicionado ao final da lista...')
    else:
        pos = 0 
        while pos < len(lista):
            if nun <= lista[pos]:
                lista.insert(pos,nun)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos = pos +1 
print(lista)