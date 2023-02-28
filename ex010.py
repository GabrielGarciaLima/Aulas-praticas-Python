# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dólar = real / 4.8
print('\nCom R${:.2f} você pode comprar US${:.2f}'.format(real, dólar))
