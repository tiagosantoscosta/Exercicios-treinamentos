r = 1
while r != 'M' and r != 'F':
    r=str(input('Digite o sexo [M/F]: ')).strip().upper()
    if r == 'M' or r == 'F':
        print('Sexo {} registrado.'.format(r))
    if r != 'M' and r != 'F':
        print('Dados inválidos, iforme seu sexo novamente:')
print('FIM')
    