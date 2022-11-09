a = int(input('\nPrimeiro numero: '))
b  = int(input('Segundo numero : '))
c = int(input('Terceiro numero: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi: {}'.format(maior))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi: {}'.format(menor))
