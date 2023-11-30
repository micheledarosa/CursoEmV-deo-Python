#  Desenvolva um programa que pergunte a distância de uma
#  viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
#  para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input('Distância da viagem em Km: '))
print('Você está prestes a começar uma viagem de {}Km.'.format(km))
if km > 200:
    ticket = km * 0.45
else:
    ticket = km * 0.50
print('E o preço da sua passagem será de R${:.2f}'.format(ticket))

#  ticket = km * 0.50 if km <= 200 else km * 0.45 (maneira simplificada)
