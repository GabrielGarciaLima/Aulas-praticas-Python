"""Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
a média de idade do grupo,
qual é o nome do homem mais velho e
quantas mulheres têm menos de 20 anos."""

media = 0
maisvelho = 0
nomemaisvelho = 0
mulheres = 0
for p in range(1, 5):
    print('{}ª PESSOA'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    media += idade
    if sexo == 'm':
        maisvelho = idade
        nomemaisvelho = nome
    elif sexo == 'f' and idade < 20:
        mulheres += 1
print('A média de idade do grupo é de {} anos.'.format(media / 4))
print('O homem mais velho do grupo tem {} anos e se chama {}.'.format(maisvelho, nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres))
