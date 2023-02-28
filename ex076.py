"""Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular."""

produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90,
            'Régua', 5.00)

print('-' * 40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-' * 40)

for produto in range(0, len(produtos)):
    if produto % 2 == 0:
        print(f'{produtos[produto]:.<30}', end='')
    else:
        print(f'R${produtos[produto]:>7.2f}')

print('-' * 40)
