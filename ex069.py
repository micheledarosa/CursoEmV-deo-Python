# Crie um programa que leia a idade e o sexo
# de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer
# ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.

from time import sleep as pausa

cadastro = maior = homem = mulher = 0
print('''\033[34m--------
CADASTRO
--------\033[m''')

while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher += 1
    cadastro += 1
    print('Cadastrado com sucesso.')
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Gostaria de continuar cadastrando? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('\033[31mFinalizando os cadastros...\033[m')
pausa(2)
print(f'''------------------------------
No total foram cadastradas {cadastro} pessoas.
Dessas {cadastro} pessoas, {maior} são maiores de idade.
{homem} pessoas são do sexo masculino.
{mulher} mulher(es) tem menos de 20 anos de idade.''')
