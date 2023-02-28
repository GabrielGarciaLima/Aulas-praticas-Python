# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
num = float(input('Digite qualquer número: '))
print('O número {} tem a porção inteira {}'.format(num, trunc(num)))
