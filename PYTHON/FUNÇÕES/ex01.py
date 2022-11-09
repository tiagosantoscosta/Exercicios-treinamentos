def área(l, c):                              # RESOLVI 100% :D
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m².')


print('Controle de terrenos')
print('-'*30)
a=float(input('LARGURA (m): '))
b=float(input('COMPRIMENTO (m): '))
área(a, b)
