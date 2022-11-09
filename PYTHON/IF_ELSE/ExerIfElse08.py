print('**'*15)
print('   Analisador de triângulos')
print('**'*15)



reta1=float(input('\n\033[4mDigite o primeiro comprimento:\033[m5 '))
reta2=float(input('Digite o segundo comprimento: '))
reta3=float(input('Digite o terceiro comprimento: ' ))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('\nÉ possível formar um triangulo\n')
else:
    print('\nNão forma triangulo\n')
