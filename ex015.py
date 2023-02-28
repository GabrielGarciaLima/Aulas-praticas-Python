# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Qual a quilometragem que foi rodada? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
p1 = km * 0.15
p2 = dias * 60
print('Considerando {:.2f}Km rodados em {} dias, o valor total a pagar é R${:.2f}'.format(km, dias, p1 + p2))
