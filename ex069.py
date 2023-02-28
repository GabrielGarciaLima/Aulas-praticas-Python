"""Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

quer = ''
maior = homens = mulheres = 0

while True:
    if quer in 'Ss':
        print('-' * 25)
        print('   CADASTRE UMA PESSOA')
        print('-' * 25)
        idade = int(input('Idade: '))
        sexo = str(input('Sexo: [M/F]')).strip()
        print('-' * 25)
        quer = str(input('Quer continuar? [S/N]')).strip()
        if idade >= 18:
            maior += 1
        if sexo in 'Mm':
            homens += 1
        elif sexo in 'Ff' and idade < 20:
            mulheres += 1
    elif quer in 'Nn':
        print(f'Total de pessoas com mais de 18 anos: {maior}')
        print(f'Ao todo temos {homens} homens cadastrados.')
        print(f'E temos {mulheres} mulheres com menos de 20 anos.')
        break
