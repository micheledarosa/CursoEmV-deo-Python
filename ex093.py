# Crie um programa que gerencie o
# aproveitamento de um jogador de futebol. O programa
# vai ler o nome do jogador e quantas partidas ele
# jogou. Depois vai ler a quantidade de gols feitos
# em cada partida. No final, tudo isso será guardado
# em um dicionário, incluindo o total de gols feitos
# durante o campeonato.

jogador = dict()
gols = list()

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Partidas: '))
for i in range(1, partidas + 1):
    gols.append(int(input(f'Gols na {i}ª partida: ')))
print()
jogador['gols'] = gols
jogador['total'] = sum(gols)
print(jogador)
print()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print()
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols'], 1):
    print(f' ➔ Na partida {i}, fez {v} gol(s).')
print(f'Foi um total de {jogador['total']} gols.')
