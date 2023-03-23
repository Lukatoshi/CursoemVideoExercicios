#Faça um programa que leia um nímero inteiro e mostre na tela o seu sucessor e seu antecessor;

ni = int(input('Digite um número: '))

print('O sucessor de {} é {}, e seu antecessor é {}'.format(ni, (ni + 1), (ni - 1)))
