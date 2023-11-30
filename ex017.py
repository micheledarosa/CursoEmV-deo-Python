#  Faça um programa que leia o comprimento do cateto oposto
#  e do cateto adjacente de um triângulo retângulo.
#  Calcule e mostre o comprimento da hipotenusa.

from math import hypot

cateto_op = float(input('Digite o comprimento do cateto oposto: '))
cateto_ad = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(cateto_op, cateto_ad)
print('A hipotenusa vai medir {:.2f}'.format(hip))

#  hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
