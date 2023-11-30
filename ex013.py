#  Faça um algoritmo que leia o salário de um funcionário
#  e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário: R$'))
aum = salario + (salario * 0.15)  # ou salario * 15 / 100
print('O novo salário com aumento de 15% é: R${:.2f}'.format(aum))

produto = float(input('Digite o preço do produto: R$'))
av = produto - (produto * 0.1)  # 10% de desconto
ap = produto + (produto * 0.08)  # 8% de aumento
print('O preço do produto é de R${:.2f}.\nÀ vista com 10% de desconto o valor do produto fica R${:.2f}.\nÀ prazo com '
      '8% de juros o valor do produto fica R${:.2f}'.format(produto, av, ap))
