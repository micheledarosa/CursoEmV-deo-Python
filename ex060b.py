num = int(input('Digite um número para calcular o fatorial: '))
fat = 1

for c in range(1, num + 1):
    fat *= c

print(f'O fatorial de {num} é {fat}')  # nova formatação
