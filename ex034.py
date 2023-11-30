# Escreva um programa que pergunte o salário de
# um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento
# de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual é o salário do funcionário? R$'))

if sal > 1250:
    aum = (sal * 0.10) + sal
    print('O salário atual é R${:.2f} e com aumento de 10% será de R${:.2f}'.format(sal, aum))
else:
    aum = (sal * 0.15) + sal
    print('O salário atual é R${:.2f} e com aumento de 15% será de R${:.2f}'.format(sal, aum))
