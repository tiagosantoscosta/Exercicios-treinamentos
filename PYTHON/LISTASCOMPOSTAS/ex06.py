ficha = list()
while True:
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp=str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*40)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
print('-'*40)
while True:
    resp2 = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if resp2 == 999:
        break
    if resp2 <= len(ficha) -1:
        print(f'Notas de {ficha[resp2][0]} são {ficha[resp2][1]}')
        