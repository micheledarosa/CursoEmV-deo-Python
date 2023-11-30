# Crie um programa que leia vários números inteiros
# pelo teclado. No final da execução, mostre a média
# entre todos os valores e qual foi o maior e o menor
# valores lidos. O programa deve perguntar ao usuário se
# ele quer ou não continuar a digitar valores.

maior = num = media = soma = cont = menor = 0

continua = 'S'

while continua in 'Ss':
    num = int(input('Digite um número inteiro: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continua = str(input('Deseja digitar mais números? S/N ')).strip().upper()[0]

media = soma / cont
print(f'A média dos {cont} valores digitados é {media:.2f}\nNúmero maior: {maior}\nNúmero menor: {menor}')
