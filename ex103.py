# Faça um programa que tenha uma função
# chamada ficha(), que receba dois parâmetros
# opcionais: o nome de um jogador e quantos gols
# ele marcou. O programa deverá ser capaz de mostrar
# a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.

def ficha(nome="<desconhecido>", gols=0):
    return print(f'O jogador {nome} fez {gols} gols no campeonato.')


jogador = str(input('Nome do jogador: ')).strip()
num_gols = str(input('Número de gols: '))
if num_gols.isnumeric():
    num_gols = int(num_gols)
else:
    num_gols = 0

if jogador.strip() == '':
    ficha(gols=num_gols)
else:
    ficha(jogador, num_gols)
