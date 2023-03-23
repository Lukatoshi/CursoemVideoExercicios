#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

alunos = []
alunos.append(input('Aluno 1: '))
alunos.append(input('Aluno 2: '))
alunos.append(input('Aluno 3: '))
alunos.append(input('Aluno 4: '))

shuffle(alunos)

print(f'A ordem das apresentações serão: {alunos}')
