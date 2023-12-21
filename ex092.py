# Crie um programa que leia nome, ano de
# nascimento e carteira de trabalho e cadastre-o
# (com idade) em um dicionário. Se por acaso a CTPS
# for diferente de ZERO, o dicionário receberá também
# o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a
# pessoa vai se aposentar.

from datetime import datetime

cadastro = dict()

cadastro['nome'] = str(input('Nome: ')).strip()
ano_nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = datetime.now().year - ano_nasc
cadastro['ctps'] = int(input('Carteira de trabalho [0 = Não possui]: '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratação'] + 35) - datetime.now().year)

print('\033[34m-=' * 15)
for k, v in cadastro.items():
    print(f'\033[m{k}: {v}')
