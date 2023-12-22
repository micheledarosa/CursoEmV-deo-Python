# Crie um programa que leia nome, sexo e idade
# de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dados = dict()
cadastros = list()
acima_da_media = list()
soma_idade = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: ')).strip()
    sexo = ' '
    while sexo not in 'MF':
        print('Digite apenas M ou F')
        sexo = str(input('Sexo: ')).strip().upper()[0]
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    soma_idade += dados['idade']
    cadastros.append(dados.copy())
    continua = ' '
    while continua not in 'SN':
        print('S - Cadastrar outra pessoa\nN - Finalizar cadastros')
        continua = str(input('S/N: ')).strip().upper()[0]
    if continua == 'N':
        break

media = soma_idade / len(cadastros)
for pessoa in cadastros:
    if pessoa['idade'] > media:
        acima_da_media.append(pessoa.copy())

# acima_da_media = [pessoa for pessoa in cadastros if pessoa['idade'] > media]

print('\033[33m-\033[m' * 40)
print(f'Foram cadastradas {len(cadastros)} pessoas.')
print(f'A média das idades cadastradas é {media:.1f}.')
print(f'As mulheres cadastradas foram ', end='')
for pessoa in cadastros:
    if pessoa['sexo'] in 'F':
        print(f'{pessoa["nome"]} ', end='')
print()
if not acima_da_media:
    print(f'Não há pessoas acima da média.')
else:
    print(f'Lista com as pessoas acima da média: {acima_da_media}')
