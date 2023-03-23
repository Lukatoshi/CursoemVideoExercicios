#Desenvolva um programa que leia as duas notas de um aluno, calucule e mostre a sua média;
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

print('A média de {:.1f} e {:.1f} é {:.1f}'.format(nota1, nota2, (nota1 + nota2) / 2))