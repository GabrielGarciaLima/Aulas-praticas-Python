"""Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais"""

primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))
if primeiro > segundo:
    print('O PRIMEIRO número é maior!')
elif primeiro < segundo:
    print('O SEGUNDO número é maior!')
else:
    print('Os dois números são IGUAIS!')
