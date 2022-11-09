print('*'*30)
print('    Sequência de Fibonacci')
print('*'*30)
n=int(input('quanto termos você quer mostrar: '))
t1=0
t2=1
print('{} - {}'.format(t1,t2), end='')
cont = 3
while cont <= n:
    cont= cont +1
    t3=t1+t2
    t1=t2
    t2=t3
    print(' - {}'.format(t3), end='')
print(' - FIM')