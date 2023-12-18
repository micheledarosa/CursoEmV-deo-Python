# Aprimore o desafio anterior, mostrando no
# final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_coluna3 = maior_linha2 = 0

for l in range(0, 3):  # l = linha
    for c in range(0, 3):  # c = coluna
        matriz[l][c] = (int(input(f'Digite o número na posição {l}, {c}: ')))
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma de todos os valores pares é {soma_par}')
for l in range(0, 3):
    soma_coluna3 += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna3}')
for c in range(0, 3):
    if c == 0:
        maior_linha2 = matriz[1][c]
    elif matriz[1][c] > maior_linha2:
        maior_linha2 = matriz[1][c]
print(f'O maior valor da segunda linha é {maior_linha2}')
