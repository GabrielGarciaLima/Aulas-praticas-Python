# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
m2 = largura * altura
print('\nA área da parede é de {:.2f}m².\nSão necessários {:.2f}l de tinta para pintá-la.'.format(m2, m2/2))
