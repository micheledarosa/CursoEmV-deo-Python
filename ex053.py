#  Crie um programa que leia uma frase qualquer
#  e diga se ela é um palíndromo, desconsiderando os espaços.
#  Exemplos de palíndromos:

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inv = junto[::-1]

'''inv = ''
for letra in range(len(junto)-1, -1, -1):
    inv += junto[letra]'''

print('O inverso de {} é {}'.format(junto, inv))
if inv == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
