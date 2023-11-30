nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:20}'.format(nome))

#  {:=^20}
#  {:<20}
#  {:>20}
#  {:^20}

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))
#  usa-se variável quando precisar do resultado depois

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' >>>> ')
print('Divisão inteira {} e potência {}'.format(di, e))

#  \n para quebrar a linha
#  end='' para não quebrar
#  pode adicionar o que quiser dentro das '', ex: end= ' >>>> '

