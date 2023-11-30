#  Elabore um programa que calcule o valor a
#  ser pago por um produto, considerando o seu preço
#  normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format('MISHA ATELIÊ'))
preco = float(input('Qual é o preço do produto? R$'))
print('-=-' * 10)
print('Escolha o método de pagamento')
print('-=-' * 10)
print('''[1] À vista dinheiro/ cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros\n''')

op = int(input('Qual é a opção? 1, 2, 3 ou 4\n'))

if op == 1:
    pag = preco - (preco * 0.1)
    print('O produto com valor de R${:.2f} com 10% de desconto ficou no valor de R${:.2f}'.format(preco, pag))
elif op == 2:
    pag = preco - (preco * 0.05)
    print('O produto com valor de R${:.2f} com 5% de desconto ficou no valor de R${:.2f}'.format(preco, pag))
elif op == 3:
    pag = preco / 2
    print('Valor do produto: R${:.2f}\nValor das parcelas: 2x de R${:.2f}'.format(preco, pag))
elif op == 4:
    esc = int(input('Em quantas vezes gostaria de parcelar? (Escolha entre 3 até 12)\n'))
    if esc > 12:
        print('Escolha inválida.')
    else:
        pag = preco + (preco * 0.2)
        par = pag / esc
        print('Valor do produto: R${:.2f} + 20% de juros: R${:.2f}\nValor das parcelas: {}x de R${:.2f}'.format(preco,
              pag, esc, par))
else:
    print('Opção inválida.')
