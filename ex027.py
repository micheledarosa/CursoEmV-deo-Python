#  Faça um programa que leia o nome completo de
#  uma pessoa, mostrando em seguida o primeiro e o último
#  nome separadamente.

nome = str(input('Nome completo: ')).strip()
separa = nome.split()
print('Primeiro nome: {}'.format(separa[0]))
print('Último nome: {}'.format(separa[-1]))
