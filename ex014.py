# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Qual a temperatura em graus Celsius? '))
fahrenheit = (celsius * 1.8) +32
print('\nA temperatura de {:.0f}°C equivale a {:.0f}°F.'.format(celsius, fahrenheit))
