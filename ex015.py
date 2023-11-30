#  Escreva um programa que pergunte a quantidade de
#  Km percorridos por um carro alugado e a quantidade de dias
#  pelos quais ele foi alugado. Calcule o preço a pagar,
#  sabendo que o carro custa R$60 por dia e R$0,15 por Km
#  rodado.

km = float(input('Qual foi a quantidade de Km rodados? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
valor_carro = 60 * dias
valor_km = km * 0.15
total = valor_carro + valor_km
print('O carro com o valor de R$60 por dia, alugado por {} dia(s), ficou no valor de R${:.2f}.\nO valor dos Km rodados,'
      ' sendo R$0,15 por Km, ficou no valor de R${:.2f}.\nTotal de R${}.'.format(dias, valor_carro, valor_km, total))

#  caso queira mostrar apenas o total fazer total = (dias * 60) + (km * 0.15)
