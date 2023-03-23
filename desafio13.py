#Faça um algoritmo que leia o salário de um funcionárop e ,mostre seu novo salário, com 15% de aumento;

salario = float(input('Qual o seu salário? '))

aumento = (salario*15) / 100

print('Seu salário atual é R${:.2f}, com o aumento de 15% fica R${:.2f}'.format(salario, salario + aumento))