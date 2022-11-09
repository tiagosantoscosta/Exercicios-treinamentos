numero = int(input('\nDigite um número inteiro qualquer para converter: '))
coversao = int(input('    Digite:\n-1 para binário\n-2 para octal\n-3 para hexadecimal\n'))


if coversao == 1:
    print('Binário: {}'.format(bin(numero)[2:]))
elif coversao == 2:
    print('Octal: {}'.format(oct(numero)[2:]))
elif coversao == 3:
    print('Hexadecimal: {}'.format(hex(numero)[2:]))