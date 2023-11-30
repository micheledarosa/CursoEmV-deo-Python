# Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

C = float(input('Digite a temperatura em Celsius: '))
F = C*1.8 + 32  # ((9*c)/5)+32 ou 9 * c / 5 + 32
print('A temperatura {}ºC convertida para Fahrenheit é {}ºF'.format(C, F))
