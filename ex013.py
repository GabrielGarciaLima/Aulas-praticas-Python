# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario + (salario * 15 / 100)
print('O salário de R${:.2f} do funcionário, reajustado em 15%, será R${:.2f}'.format(salario, aumento))
