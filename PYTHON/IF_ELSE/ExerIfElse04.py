distancia=float(input('\nDigite a distancia total: '))
if distancia <= 200:
    print('Preço da passagem: {:.2f} R$'.format(distancia * 0.50))
else:
    print('Preço da passagem: {:.2f} R$'.format(distancia * 0.45))