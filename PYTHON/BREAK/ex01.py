soma=0
numero=0
cont=0
while numero != 999:
    numero=int(input('Digite um número: '))
    if numero == 999:
        break
    cont=cont +1
    soma= soma + numero
print(f'A soma dos {cont} valores foi {soma}.')

