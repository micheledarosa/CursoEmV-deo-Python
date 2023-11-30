#  Faça um programa que leia um ângulo qualquer e
#  mostre na tela o valor do seno, cosseno e tangente desse
#  ângulo.

from math import sin, cos, tan, radians
ang = float(input('Digite o valor do ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('Com o valor do ângulo {}, temos o valor de seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(ang, sen, cos,
                                                                                                        tan))
