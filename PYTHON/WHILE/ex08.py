numero=0
resposta='S'
media=0
cont=0
soma=0
while resposta == 'S':
    numero=float(input('Digite um número: '))
    resposta=str(input('Quer continuar? [s/n] ')).upper().strip()[0]
    cont=cont+1
    soma= soma + numero
    if cont == 1:
        maior =  menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media= soma / cont
print('Você digitou {} numeros e a média foi {:.2f}'.format(cont,media))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))