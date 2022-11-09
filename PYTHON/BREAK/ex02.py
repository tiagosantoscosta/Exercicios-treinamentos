
while True:
    numero=int(input('Quer ver a tabuada de qual valor? '))
    if numero <0:
        break
    print('*'*37)
    for c in range(1,11):
        print(f'{numero} x {c} = {c*numero}')
    print('*'*37)
print('Tabuada encerrado')
    

    