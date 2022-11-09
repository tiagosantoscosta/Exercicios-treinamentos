salario=float(input('\nDigite o salário: '))
if salario >1250:
    print('Você teve um aumento de 10% então passa a receber: {:.2f} R$'.format((salario * 10) / 100 + salario))
else:
    print('Você teve um aumento de 15% então passa a receber: {:.2f} R$'.format((salario * 15) / 100 + salario))
