# Crie uma tupla preenchida com os 20 primeiros
# colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time da Chapecoense. (troquei por algum que está na tabela)

tabela = ('Palmeiras', 'Botafogo', 'Atlético-MG', 'Flamengo',
          'Grêmio', 'Bragantino', 'Fluminense', 'Athletico-PR',
          'São Paulo', 'Internacional', 'Fortaleza', 'Cuiabá',
          'Corinthians', 'Cruzeiro', 'Santos', 'Vasco da Gama',
          'Bahia', 'Goiás', 'Coritiba', 'América-MG')

print(f'Lista de times do Brasileirão: {tabela}')
# for times in tabela:
#    print(times)

print('~' * 15)
print(f'5 primeiros times: {tabela[:5]}')
print('~' * 15)
print(f'Últimos 4 colocados: {tabela[-4:]}')
print('~' * 15)
print(f'Ordem alfabética: {sorted(tabela)}')
print('~' * 15)
print(f'Grêmio está na {tabela.index("Grêmio")+1}ª posição')  # 1ª posição é zero, então adiciona +1 para ficar certo
