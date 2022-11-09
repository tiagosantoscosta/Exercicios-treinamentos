tupla=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    numero=int(input(f'Digite um número entre 0 e 20: '))
    if numero >= 0 and numero <= 20: # O número está entre 0 e 20
        break
    print('Tente novamente')
print(f'Você digitou o número {tupla[numero]}')