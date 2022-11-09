def voto(a):                       #RESOLVI 100% usando o print
    from datetime import date           #MAS DA PRA USAR O RETURN TBM 
    print('-'*30)
    idade = date.today().year - a
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.' #retorna a frase, 
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    if idade >= 65 or idade >= 16 and idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL.'


ano=int(input('Em que ano você nasceu? '))
print(voto(ano))

