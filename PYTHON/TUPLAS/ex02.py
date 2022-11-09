tabela=('Palmeiras','Corinthians','Fluminense','Atletico-MG','Athetico-PR','Flamengo','Internacional'
,'Bragantino','Santos','São Paulo','Botafogo','Ceará','Coritiba'
,'Goiás','América-MG','Avaí','Cuiabá','Atl.Goianense','Juventude','Fortaleza') #ISSO È UMA TUPLA(TUPLAS 
                                                                                    #SÃo IMUTÁVEIS)'''
print('=-'*30)
print(f'Os 5 primeiros times são {tabela[:5]}')
print('=-'*30)
print(f'Os últimos 4 colocados são {tabela[-4:]}') #Fatiamento da tupla (-1,-2,-3,-4)
print('=-'*30)
print(f'Times em ordem alfabética {sorted(tabela)}')
print('=-'*30)
print('O Bragantino está na {}ª posição.'.format(tabela.index('Botafogo')+1))