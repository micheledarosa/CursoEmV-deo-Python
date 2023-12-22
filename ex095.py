from prettytable import PrettyTable
from time import sleep
from emoji import emojize

jogador = dict()
cadastro_jogadores = list()


def mostrar_emoji(emote):
    emoji = emojize(emote)
    return emoji


def finalizar_programa():
    print('...')
    sleep(1)
    print('Finalizando o programa...', end='')
    sleep(1)
    print(mostrar_emoji("✔️"))


while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Partidas: '))
    gols = list()
    for i in range(1, partidas + 1):
        gols.append(int(input(f'Gols na {i}ª partida: ')))
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    cadastro_jogadores.append(jogador.copy())
    while True:
        continua = str(input('Adicionar outro jogador? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
        print('Responda com "S" ou "N"')
    if continua == 'N':
        break
print()
tabela = PrettyTable()
tabela.field_names = ["Cod", "Nome", "Gols", "Total"]

for codigo, jogador in enumerate(cadastro_jogadores, 1):
    tabela.add_row([codigo, jogador['nome'], jogador['gols'], jogador['total']])
print(tabela)
print()
dados = str(input('Gostaria de ver os dados de algum jogador? [S/N] ')).strip().upper()[0]
if dados == 'S':
    while True:
        cod = int(input('Digite o código do jogador: '))
        if 1 <= cod <= len(cadastro_jogadores):
            jogador_escolhido = cadastro_jogadores[cod - 1]
            print('\033[34m-\033[m' * 30)
            print(f'{mostrar_emoji("⚽")} DETALHES DO JOGADOR {cod} {mostrar_emoji("⚽")}')
            print(f'  -Nome: {jogador_escolhido["nome"]}')
            print(f'  -Gols por partida: {jogador_escolhido["gols"]}')
            print(f'  -Total de gols: {jogador_escolhido["total"]}')
            print('\033[34m-\033[m' * 30)
            while True:
                nova_escolha = str(input('Gostaria de ver os dados de algum jogador? [S/N] ')).strip().upper()[0]
                if nova_escolha in 'SN':
                    break
            if nova_escolha == 'N':
                finalizar_programa()
                break
        else:
            print('Código inválido.')
            continue
else:
    finalizar_programa()
