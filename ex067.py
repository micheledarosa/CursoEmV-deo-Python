# Faça um programa que mostre a tabuada de
# vários números, um de cada vez, para cada
# valor digitado pelo usuário. O programa será
# interrompido quando o número solicitado for negativo.

while True:
    print('''\033[34m------------
  TABUADA
------------\033[m
Insira um número \033[30;41mnegativo\033[m para \033[30;41mencerrar\033[m o programa.''')
    num = int(input('Tabuada do número: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
print('Encerrando o programa...')
