n=int(input('Digite um número: ')),int(input('Digite outro número: ')),int(input('Digite mais um número: ')),int(input('Digite o último número: '))
print(f'O valor 9 apareceu {n.count(9)} vezes') # .count(9) conta quantas vezes o 9 aparece
if 3 in n:
        print(f'O valor 3 apareceu na {n.index(3)+1}ª posição') #.index(3) mostra a posição do n° 3 na memória
else:
        print('O número 3 não foi encontrado')
print(f'Os valores pares digitados foram ', end='')
for c in n:
        if c %2==0:
                print(c)







              

             


        


 