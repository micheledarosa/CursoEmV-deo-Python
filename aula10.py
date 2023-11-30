nome = str(input('Qual é seu nome? '))
if nome == 'Michele':
    print('Que nome lindo :D')
else:
    print('Eita :(')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 6.0:
    print('Sua média foi boa! Parabéns')
else:
    print('Sua média foi ruim! Estude mais')
print('A sua média foi {:.1f}'.format(media))

#  print('parabéns' if media >=6 else 'estude mais')