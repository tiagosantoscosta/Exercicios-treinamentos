soma=0
for c in range(1,7):
    n=int(input('Digite o {}° número : '.format(c)))
    if n % 2 == 0:
        soma = soma + n
print('A soma dos números pares é: {}'.format(soma))
    
