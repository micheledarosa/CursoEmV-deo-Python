# Crie um programa onde 4 jogadores
# joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

game_results = dict()

for player in range(1, 5):
    dice_result = randint(1, 6)
    game_results[f'jogador {player}'] = dice_result

ranking = dict(sorted(game_results.items(), key=lambda x: x[1], reverse=True))

print('\033[35mValores sorteados:\033[m')
for k, v in game_results.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('-' * 30)
print('\033[35mRaking dos jogadores:\033[m')
for i, (k, v) in enumerate(ranking.items(), start=1):
    print(f'{i}º lugar: {k} com {v} pontos')
    sleep(1)
