"""Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""

print('-' * 20)
print('LOJA SUPER BARATÃO!')
print('-' * 20)

total = maiorqmil = menor = cont = 0
barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        maiorqmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N]')).strip()

    if resposta in 'Nn':
        print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
        print(f'O total da compra foi R${total:.2f}')
        print(f'Temos {maiorqmil} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
        break
