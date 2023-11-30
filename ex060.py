# Faça um programa que leia um número
# qualquer e mostre o seu fatorial. Exemplo:
#
# 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial
from time import sleep

print('=' * 25)
print('Vamos calcular o fatorial')
print('=' * 25)

while True:
    num = int(input('Digite um número:\nPara sair digite 0\n'))
    if num == 0:
        break
    fat = factorial(num)
    print('O fatorial de {} é {}'.format(num, fat))
    sleep(1)
print('Encerrando...')
