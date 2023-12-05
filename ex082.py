# Crie um programa que vai ler vários
# números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os
# valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três
# listas geradas.

lista_num = []
lista_par = []
lista_impar = []

while True:
    num = int(input('Adicione um número: '))
    lista_num.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Gostaria de adicionar mais números? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break

lista_num.sort(), lista_par.sort(), lista_impar.sort()

print('\033[35m='*44)
print(f'''\033[mLista completa: {lista_num}
Apenas números pares: {lista_par}
Apenas números ímpares: {lista_impar}''')
