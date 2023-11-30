#  Faça um algoritmo que leia o preço de um produto e
#  mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$'))
desc = preco - (preco * 0.05)
print('O preço deste produto com 5% de desconto é de: R${:.2f}'.format(desc))

#  ou usar assim 200*10/100 (preço*porcentagem/100)