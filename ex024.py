# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Nome da cidade: ')).strip().upper()
cida = cidade.split()
ci = bool(cida[0] == 'SANTO')
print('O primeiro nome da cidade {} é Santo? {}'.format(cidade, ci))
