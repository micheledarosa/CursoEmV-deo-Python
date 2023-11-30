# Crie um programa que leia o nome e o preço
# de vários produtos. O programa deverá perguntar se
# o usuário vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.

import emoji

total = qtd_1000 = menor_preco = qtd_produtos = 0
barato = ''

print('''\033[35m--------------
LOJA  DA MISHA
--------------\033[m''')
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$'))
    if preco > 1000:
        qtd_1000 += 1
    qtd_produtos += 1
    if qtd_produtos == 1 or preco < menor_preco:
        menor_preco = preco
        barato = produto
    total += preco
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Registrar outro produto? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break

print(emoji.emojize(f'''\033[34m--------------------------\033[m
Total da compra: R${total:.2f}
{qtd_1000} produtos custam acima de R$1.000
{barato} foi o produto mais barato, com custo de R${menor_preco:.2f}
Obrigado pela compra! Volte sempre! :shopping_bags:'''))
