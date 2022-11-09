from datetime import date
ano = date.today().year
totalmaior=0
totalmenor=0
for c in range(1,8):
    nascimento=int(input('Em que ano a {} ° pessoa nasceu? '.format(c)))
    soma = ano - nascimento
    if soma >=21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todo tivemos {} pessoas maiores'.format(totalmaior))
print('Ao todo tivemos {} pessoas menores'.format(totalmenor))


        
    

