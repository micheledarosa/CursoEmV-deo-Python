# Crie um programa que tenha uma tupla
# com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra,
# quais são as suas vogais.

linguagens = ('JavaScript',
              'Java',
              'Python',
              'TypeScript',
              'Ruby',
              'Swift',
              'Scala',
              'Kotlin',
              'Rust',
              'Dart')

for p in linguagens:
        print(f'\nNa palavra {p} temos', end=' ')
        for letra in p:
            if letra.lower() in 'aeiou':
                print(letra, end=' ')
