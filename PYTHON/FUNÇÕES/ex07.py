def fatorial(n, show=False):                       #RESOlVI MAS DE FORMA DIFERENTE
    """-> Calcula o fatorial de um número.
        :param n: O número a ser calculado                  #ISSO É UMA DOCSTRING 
        :param show: (opcional) mostrar ou não a conta.
        :return: O valor do fatorial de un n."""
    print('='*30)
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f = f * c       
    return f


print(fatorial(15, show=True))
help(fatorial)

