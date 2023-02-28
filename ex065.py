"""Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e
qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

cond = 's'
soma = cont = media = maior = menor = 0

while cond in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cond = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
media = soma / cont
print('Você digitou {} números e a média entre eles é {}'.format(cont, media))
print('O maior valor é {} e o menor valor é {}'.format(maior, menor))
