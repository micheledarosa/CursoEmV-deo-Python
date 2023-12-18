pessoas = {'nome': 'Michele', 'sexo': 'F', 'idade': 29}

print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print()

print(pessoas.keys())  # nome, sexo e idade
print(pessoas.values())  # Michele, F e 29
print(pessoas.items())  # mostra toda a composição
print()

for k in pessoas.keys():  # mostra apenas as chaves
    print(k)
print()

for k, v in pessoas.items():  # mostra a chave(k) e valor(v)
    print(f'{k} = {v}')
print()

#  del pessoas['sexo']
pessoas['nome'] = 'Misha'  # modificando
pessoas['peso'] = 62.5  # adicionando

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Rio Grande do Sul', 'sigla': 'RS'}
brasil.append(estado1)
brasil.append(estado2)

print(estado2)
print(brasil)
print()

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  # copy = [:]

for e in brasil:  # e = estado
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
    print()

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
