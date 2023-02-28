# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Preço do produto: R$'))
desconto = preço * 0.05
print('\nO preço do produto com desconto fica R${:.2f}'.format(preço - desconto))
