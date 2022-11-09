numero=int(input('Digite um número: '))
soma = 0
for c in range(1,numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ') 
        soma = soma +1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível por {} vezes'.format(numero,soma))
if(soma == 2):
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')
