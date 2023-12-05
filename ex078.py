# Faça um programa que leia 5 valores numéricos
# e guarde-os em uma lista. No final, mostre qual foi
# o maior e o menor valor digitado e as suas respectivas
# posições na lista.

valores_escolhidos = []
num_maior = 0
num_menor = 0

for c in range(0, 5):
    valores_escolhidos.append(int(input(f'Digite o valor da posição {c}: ')))
    if c == 0:
        num_maior = num_menor = valores_escolhidos[c]
    else:
        if valores_escolhidos[c] > num_maior:
            num_maior = valores_escolhidos[c]
        if valores_escolhidos[c] < num_menor:
            num_menor = valores_escolhidos[c]

print('-' * 30)
print(f'Valores digitados: {valores_escolhidos}')
print(f'O maior valor digitado foi {num_maior} na posição ', end='')
for i, v in enumerate(valores_escolhidos):
    if v == num_maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {num_menor} na posição ', end='')
for i, v in enumerate(valores_escolhidos):
    if v == num_menor:
        print(f'{i}...', end='')
print()
