# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
pri = str(input('Informe o primeiro aluno: '))
seg = str(input('Informe o segundo aluno: '))
ter = str(input('Informe o terceiro aluno: '))
qua = str(input('Informe o quarto aluno: '))
nome = choice([pri, seg, ter, qua])
print('\nO aluno escolhido foi {}'.format(nome))
