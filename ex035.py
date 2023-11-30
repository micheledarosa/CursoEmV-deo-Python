#  Desenvolva um programa que leia o
#  comprimento de três retas e diga ao usuário
#  se elas podem ou não formar um triângulo.

r1 = float(input('Digite o comprimento da \033[4;35mprimeira\033[m reta: '))
r2 = float(input('Digite o comprimento da \033[4;32msegunda\033[m reta: '))
r3 = float(input('Digite o comprimento da \033[4;36mterceira\033[m reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\033[1;34mPode\033[m formar um triângulo!')
else:
    print('\033[1;31mNão pode\033[m formar um triângulo com esses valores.')

