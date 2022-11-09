from datetime import date
ano= date.today().year                    # RESOLVI 100% :D
func = {}
func['nome'] =str(input('Nome: '))
func['idade'] =int(input('Ano de nascimento: '))
func['ctps']=int(input('Carteira de trabalho [0 não tem]: '))
idade = ano - func['idade']
func['idade'] = idade
aposentadoria = 70 - idade 
if func['ctps'] > 0:
    func['contratação'] = int(input('Ano de contratação: '))
    func['salário']= int(input('Salário : R$'))
    func['aposentadoria'] = aposentadoria
print('='*30)
for c, v in func.items():
    print(f'-{c} tem o valor {v}')



