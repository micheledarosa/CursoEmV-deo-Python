# Crie um programa que vai ler vários
# números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista_num = []

while True:
    lista_num.append(int(input('Adicione um número: ')))
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Gostaria de adicionar outro número na lista? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break

lista_num.sort(reverse=True)
print(f'\n{len(lista_num)} números foram adicionados na lista.')
print(f'Lista na ordem decrescente: {lista_num}')

if 5 in lista_num:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
