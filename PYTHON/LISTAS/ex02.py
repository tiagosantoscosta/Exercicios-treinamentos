lista=[]

while True:
    nun=int(input('Digite um valor: '))
    if nun not in lista: # Se nun não estiver na lista ou seja repetir,ele vai ser adicionado na lista
        lista.append(nun)
        print('Numero adicionado com sucesso!')
    else:  #Se ja estiver na lista ele não será adicionado
        print('Esse número já existe, não vou adicionar! ')
    resposta=str(input('Quer continuar? [S/N]')).strip().upper()
    if resposta == 'N':
        break
print(sorted(lista))


