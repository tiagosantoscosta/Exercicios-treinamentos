from random import randint
n=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)) #Variável composta(TUPLA)
print('\nOs valores sorteados foram: ',end='')
for c in n:
    print(f'{c}',end=' ')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')



#Esse foi o que eu fiz sem saber dos métodos MAX e MIN em tuplas
'''n1=randint(0,10)
n2=randint(0,10)
n3=randint(0,10)
n4=randint(0,10)
n5=randint(0,10)
numeros=n1,n2,n3,n4
print(f'Os valores soteados foram: {n1} {n2} {n3} {n4} {n5}' )
if n1 > n2 and n1 > n3 and n1 > n4:
    maior=n1
    print(f'O maior valor sorteado foi {maior} ')
elif n2 > n1 and n2 > n3 and n2 > n4:
    maior=n2
    print(f'O maior valor sorteado foi {maior} ')
elif n3 > n1 and n3 > n2 and n3 > n4:
    maior=n3
    print(f'O maior valor sorteado foi {maior} ')
elif n4 > n1 and n4 > n3 and n4 > n2:
    maior=n4
    print(f'O maior valor sorteado foi {maior} ')'''




