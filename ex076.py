# Crie um programa que tenha uma tupla
# única com nomes de produtos e seus respectivos
# preços, na sequência. No final, mostre uma listagem
# de preços, organizando os dados em forma tabular.

skincare = (('Cleasing Oil', 70),
            ('Sabonete', 6.99),
            ('Esfoliante', 24.90),
            ('Tônico', 21.70),
            ('Vitamina C', 65.50),
            ('Creme para olhos', 34.90),
            ('Hidratante', 26),
            ('Filtro Solar', 55.80),
            ('Protetor Labial', 15.90))

print('-' * 40)
print(f'{"ROTINA SKINCARE":^40}')
print('-' * 40)

for produto, preco in skincare:
    print(f'{produto:.<32}R${preco:>5.2f}')

print('-' * 40)
