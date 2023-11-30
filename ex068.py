# Faça um programa que jogue par ou ímpar
# com o computador. O jogo só será interrompido
# quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep as pausa

print('''~~~~~~~~~~
Vamos jogar?
~~~~~~~~~~''')

vitoria = 0
soma = 0

while True:
    print('1...')
    pausa(0.5)
    print('2...')
    pausa(0.5)
    print('3...')
    pausa(0.5)
    escolha = ' '  # validação
    while escolha not in 'PI':  # validação
        escolha = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    num = int(input('Digite um número de 0 até 5: '))
    if num > 5:
        print('Número inválido.')
        num = int(input('Digite um número de 0 até 5: '))
    pausa(0.5)
    pc = randint(0, 5)
    soma = num + pc
    if soma % 2 == 0 and escolha in 'Pp':
        print(f'''-------------------------------
Ganhou!
Eu pensei no número {pc}. Parabéns!
Vamos jogar novamente...''')
        vitoria += 1
        pausa(0.5)
    if soma % 2 == 0 and escolha in 'Ii':
        print(f'''-------------------------------
Perdeu!
Eu pensei no número {pc}.''')
        break
    if soma % 2 == 1 and escolha in 'Ii':
        print(f'''-------------------------------
Ganhou!
Eu pensei no número {pc}. Parabéns!
Vamos jogar novamente...''')
        vitoria += 1
        pausa(0.5)
    if soma % 2 == 1 and escolha in 'Pp':
        print(f'''-------------------------------
Perdeu!
Eu pensei no número {pc}.''')
        break
print(f'Você teve um total de {vitoria} vitória(s) consecutiva(s)!')
