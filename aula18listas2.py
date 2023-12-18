teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])  # [:] faz uma cópia
teste[0] = 'Michele'
teste[1] = '29'
galera.append(teste[:])
print(teste)

#  ---------------------------------------------------------------------------------------------------------------------

pessoal = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoal[0])  # mostra João e 19
print(pessoal[0][0])  # mostra apenas João
for p in pessoal:
    print(f'{p[0]} tem {p[1]} anos de idade')

#  ---------------------------------------------------------------------------------------------------------------------

pessoas = list()
dado = list()
maior_idade = menor_idade = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()  # se não gerar a cópia [:] no momento que der clear, irá gerar listas vazias, pois as listas
    # estão ligadas

for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior_idade += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor_idade += 1
print(f'Temos {maior_idade} maiores e {menor_idade} menores de idade.')
