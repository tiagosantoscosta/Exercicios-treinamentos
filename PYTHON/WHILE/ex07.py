
numero=0
cont=0
soma=0
numero=int(input('Digite um número: '))
while numero != 999:
    cont= cont +1
    soma= soma + numero
    numero=int(input('Digite um número: '))    
print('A soma total é {}.'.format(soma))
print('\nForam digitados {} números.'.format(cont))

