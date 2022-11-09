cont_sexo=0
cont_idade=0
cont_mulher_idade=0
while True:
    print('-'*30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-'*30)
    idade=int(input('Idade: '))
    sexo=str(input('Sexo: [M/F] ')).strip().upper()
    r=str(input('Quer continuar? [S/N] ')).strip().upper()
    if idade > 18:
        cont_idade+=1 
    if sexo == 'M':
        cont_sexo+=1
    if sexo == 'F' and idade < 20:
        cont_mulher_idade+=1
    if r == 'N':
        break    
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {cont_idade}')
print(f'Ao todo temos {cont_sexo} homens cadastrados')
print(f'E temos {cont_mulher_idade} mulheres com menos de 20 anos')
