#  Crie um programa que leia quanto dinheiro uma pessoa
#  tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dol = real / 4.96
euro = real / 5.25
yen = real / 0.033
print('Com R${:.2f} você pode comprar US${:.2f}, €{:.2f},¥{:.2f}'.format(real, dol, euro, yen))
