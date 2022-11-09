velocidade=float(input('\nDigite a velocidade medida: '))
multa= (velocidade -80) * 7
if velocidade > 80:
    print('Você foi multado! Sua multa é: {:.2f} R$ '.format(multa))    

else:
    print('Está na velocidade da via.')
print('Tenha um bom dia,dirija com segurança')