# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
an = float(input('Informe o ângulo: '))
seno = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('\nDado o ângulo de {:.2f}°: '.format(an))
print('\nSENO: {:.2f}\nCOSSENO: {:.2f}\nTANGENTE: {:.2f}'.format(seno, cos, tan))
