#  Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
#  foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Digite a velocidade do carro: '))

if vel > 80:
    multa = (vel - 80) * 7
    print('Você ultrapassou os 80Km/h permitidos. A multa foi de R${:.2f}.'.format(multa))
else:
    print('Parabéns! Você estava dentro da velocidade permitida.')
