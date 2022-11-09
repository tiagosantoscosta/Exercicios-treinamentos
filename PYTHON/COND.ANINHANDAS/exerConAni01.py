
print('\nEmpréstimo imobiliário')
valorcasa = float(input('Digite o valor da casa a ser financiada: '))
salario = float(input('Informe o seu salário: '))
prazo = float(input('Em quantos anos você pagará a casa? '))

parcela = (valorcasa / prazo) / 12

print('Para pagar um imóvel de {:.2f} em {:.0f} ano(s) a prestacão será de : {:.2f} R$'.format(valorcasa,prazo,parcela))

aprovacao = 30 * salario / 100
if parcela >= aprovacao:
    print('Seu financiamento foi REPROVADO!')
else:
    print('Você foi APROVADO')

