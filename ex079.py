# Crie um programa onde o usuário possa
# digitar vários valores numéricos e cadastre-os em
# uma lista. Caso o número já exista lá dentro, ele
# não será adicionado. No final, serão exibidos todos
# os valores únicos digitados, em ordem crescente.

lista_valores = []

while True:
    num = int(input('Digite um valor: '))
    if num not in lista_valores:
        lista_valores.append(num)
    else:
        print('Não é possível adicionar um valor duplicado.')
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Gostaria de adicionar outro valor? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break

lista_valores.sort()
print(f'Os valores digitados foram: {lista_valores}')
