# Faça um programa que tenha uma função chamada
# escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva(texto):
    tam = len(texto) + 4
    linha = '\033[32m~\033[m' * tam
    print(linha)
    print(f'{texto:^{tam}}')
    print(linha)


escreva('Olá, Mundo!')

txt = str(input('Digite uma frase qualquer: '))
escreva(txt)
