#   Desenvolva um programa que leia seis números
#   inteiros e mostre a soma apenas daqueles que forem
#   pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
print('Digite seis(6) números')
for c in range(1, 7):
    num = int(input('{}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('{} números digitados são pares. A soma deles é {}'.format(cont, soma))
