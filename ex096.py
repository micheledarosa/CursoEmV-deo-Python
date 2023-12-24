# Faça um programa que tenha uma função chamada
# área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    res = largura * comprimento
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {res:.2f}m².')


# Programa principal
print('''CONTROLE DE TERRENOS
---------------------''')
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)
