matriz=[[0, 0, 0], [0, 0, 0], [0, 0, 0]] #CRIANDO UMA MATRIZ 3X3
somapares=maior=somacolu3=0
for l in range (0,3):
    for c in range(0,3):        
        matriz[l][c]=int(input(f'Digite um valor para [{l}, {c}]: '))        
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
        if matriz[l][c] %2==0:
            somapares+=matriz[l][c]
    print()
print(f'A soma dos valores pares é: {somapares}')
for l in range(0,3):
    somacolu3= somacolu3 + matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {somacolu3} ')
print(f'O maior valor da 2º coluna é: {max(matriz[1])}')

