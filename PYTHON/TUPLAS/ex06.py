listagem=('APRENDER','PROGRAMAR','LINGUAGEM',
'PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR',
'TRABALHAR','MERCADO','PROGRAMADOR','FUTURO',)
for p in listagem:
    print(f'\nNa palavra {p.lower()} temos',end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(),end=' ')
    