from random import randint
from time import sleep
computador = randint(1,3)
usuario=int(input('Suas opções:\n[1] PEDRA\n[2] PAPEL\n[3] TESOURA\nQual a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
Pedra='PEDRA'
Papel='PAPEL'
Tesoura='TESOURA'
if usuario == 1 and computador == 3:
    print('O computador escolheu {}\nJogador escolheu {}\nVocê VENCEU!'.format(Tesoura,Pedra))
elif usuario == 1 and computador == 2:
    print('O computador escolheu {}\nJogador escolheu {}\nVocê PERDEU!'.format(Papel,Pedra))
elif usuario == 1 and computador == 1:
    print('O computador escolheu {}\nJogador escolheu {}\nEMPATE!'.format(Pedra,Pedra))
elif usuario == 2 and computador == 2:
    print('O computador escolheu {}\nJogador escolheu {}\nEMPATE!'.format(Papel,Papel))
elif usuario == 2 and computador == 1:
    print('O computador escolheu {}\nJogador escolheu {}\nVocê VENCEU!'.format(Pedra,Papel))
elif usuario == 2 and computador == 3:
    print('O computador escolheu {}\nJogador escolheu {}\nVocê PERDEU!'.format(Tesoura,Papel))
elif usuario == 3 and computador == 2:
    print('O computador escolheu {}\nJogador escolheu {}\nVocê VENCEU!'.format(Papel,Tesoura))
elif usuario == 3 and computador == 3:
    print('O computador escolheu {}\nJogador escolheu {}\nEMPATE!'.format(Tesoura,Tesoura))
elif usuario == 3 and computador == 1:
    print('O computador escolheu {}\nJogador escolheu {}\nVocê PERDEU!'.format(Pedra,Tesoura))
else:
    print('Inválido!')



