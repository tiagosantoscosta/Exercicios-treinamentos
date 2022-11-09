ficha={}                                 
lista=[]
soma=media=0
mulheres=0
while True:
    ficha['nome']=str(input('Nome: '))
    while True:
        ficha['sexo']=str(input('Sexo: [M/F] ')).upper()[0]
        if ficha['sexo'] in 'MF' :
            break
        print('ERRO! Responda apenas M ou F.')   
    ficha['idade']=int(input('Idade: '))
    soma = soma + ficha['idade']
    lista.append(ficha.copy())
    while True:
        resp=str(input('quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp != 'S':
        break   
media=soma / len(lista)
print(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for c in lista:
    if c['sexo'] == 'F':
        print(f'{c["nome"]} ', end='')
print()
print('D) A lista das pessoas que estão acima da média:')
for c in lista:
    if c['idade'] > media:
        print(f'  nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]};',)
print('** ENCERRADO **')




